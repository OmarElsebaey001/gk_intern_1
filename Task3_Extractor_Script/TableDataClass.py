from datetime import datetime
import pandas as pd
from MetaDataClass import MetaDataExtractor
from re import findall

class TableData(MetaDataExtractor):

    __filterationRegex='[A-Z\s?]+'
    __ISINRegex="[A-Z]+[0-9]+[A-Z]+[0-9]+[.]?[0-9]+"
    __ISINRegexType2='[-]+[A-Z]+[-]?[0-9]+'
    def __isData(self,arr:list)->bool:
        if len(arr)<4 or not arr[2]:
            return False
        res=False
        try:
            datetime.strptime(arr[1],"%H:%M:%S")
            res=True
        except :
            return False
        return arr[0].isdigit() and len(arr[0])>=8 and res

    def __filterCompanyName(self,target:str)->list:
        return findall(self.__filterationRegex,target)

    def __filterISIN(self,target:str)->list:
        res=findall(self.__ISINRegex,target)
        if len(res)==0:
            res=findall(self.__ISINRegexType2,target)
        if len(res)==0:
            return [target]
        return res

    def __createOrganizedDf(self,pages:list=[])-> pd.DataFrame:
        rows=[]
        additionalColumns=super().extractData()[0]
        for elem in pages:
           if self.__isData(elem):
                ISIN=self.__filterISIN(elem[4])
                elem[4]=self.__filterCompanyName(elem[4])[0] + "."
                rows.append(elem + additionalColumns+ISIN)
        df=pd.DataFrame(rows,columns=super().getColumns())
        return df

    def extractData(self)->pd.DataFrame:
        return super().useTables(self.__createOrganizedDf).drop(['remark','ClosingRatePerUnit(Rs)'],axis=1)\
        .replace(r'\n',' ', regex=True)
