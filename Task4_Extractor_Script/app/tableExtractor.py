from datetime import datetime
import pandas as pd
import pdfplumber
import re


# variables
dfColumns=['Order No.','OrderTime','TradeNo.','TradeTime',
            'Buy(B) /Sell(S)','Quantity','Gross Rate/trade price per Unit(Rs)',
            'Brokerage perUnit','NetRate perUnit(Rs)',
            'NetTotal(BeforeLevies)(Rs.)','Symbol','ISIN',
            'Company Name','Average Total(BeforeLevies)(Rs.)',
            'Total Buy','Total Sell'
            ]

expectedOrderNumberLength=10


# Regex patterns
OrderNoReg='[0-9]+\n?'
symbolRegex='Symbol[\s]?:[\s]?[A-Z0-9-?]+'
ISINRegex="[A-Z]+[0-9]+[A-Z]+[0-9]+[.]?[0-9]+"
ISINRegexType2='[-]+[A-Z]+[-]?[0-9]+'
BuySellRegex="[0-9]*\s[@]\s?[0-9]+[.][0-9]*\s?[=]\s?[0-9]*[.][0-9]"
'*\s[a-zA-Z]*[:]?\s[0-9]*[.][0-9]*'
timeRegex='[0-9]{2}:[0-9]{2}:[0-9]{2}'


# Regex extractor functions
getOrderNo=lambda target:re.findall(OrderNoReg,target)


def isOneOrder(target)->bool:
    if len(target)<5:
        return False
    return len(re.findall(timeRegex,target[1]))==1 and len(re.findall(timeRegex,target[3]))==1

def areMultipleOrders(target)->bool:
    if len(target)<5:
        return False
    return len(re.findall(timeRegex,target[1]))>1 and len(re.findall(timeRegex,target[3]))>1

isSymbolsArray=lambda target: len(re.findall(symbolRegex,target[0]))>0

extractSymbols=lambda x:re.findall(symbolRegex,x[0])

extractISIN=lambda x:re.findall(ISINRegex,x[0]) if len(re.findall(ISINRegex,x[0]))>0 else re.findall(ISINRegexType2,x[0])

extractSymbolsData=lambda target:[extractSymbols(target)[0].replace('Symbol :',''),*extractISIN(target),target[1],target[3]]

findBuySell=lambda arr:[i for i in arr if i is not None and re.findall(BuySellRegex,i)]






def turnToRows(targetList:list)->list[list]:
    # print(targetList)
    targetList.pop(4)
    cleaned=[]
    for i in targetList:
        cleaned.append(i.split('\n'))

    ans=[]
    for i in range(len(cleaned[0])):
        temp=[]
        for j in range(len(cleaned)):
            temp.append(cleaned[j][i])
        ans.append(temp)
    return ans



def getTableData(pdf):

    rows=[]
    temp=[]
    multiTemp=[]
    filteredArray=[]

    reader=pdfplumber.open(pdf)


    for i in reader.pages:
        for j in i.extract_table({'snap_tolerance':7}):
            filteredArray.append([k for k in j if k])


    for i in filteredArray:
        buySell=findBuySell(i)
        if isSymbolsArray(i):
            t=extractSymbolsData(i)
            if len(temp)==10:
                    temp+=t
            else:
                # print('called')
                for i in multiTemp:
                    i+=t
        elif isOneOrder(i):
            i.pop(4)
            # print(i)
            temp+=i
        elif areMultipleOrders(i):
            mappedArray=turnToRows(i)
            # print(*mappedArray,sep='\n')
            for j in mappedArray:
                multiTemp.append(j)
        elif len(buySell)>0:
            if len(temp)==14:
                if temp[4]=="B":
                    temp+=[buySell[0],None]
                else:
                    temp+=[None,buySell[0]]
            else:
                for i in multiTemp:
                    if i[4]=="B":
                        i+=[buySell[0],None]
                    else:
                        i+=[None,buySell[0]]
                # print(*multiTemp,sep='\n')
        print(temp)
        if len(temp)==16:
            rows.append(temp)
            temp=[]
        if len(multiTemp)>0 and len(multiTemp[0])==16:
            for i in multiTemp:
                rows.append(i)
            multiTemp=[]
    return rows
