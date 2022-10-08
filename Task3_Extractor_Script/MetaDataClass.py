

from DataClass import Data
from re import findall



class MetaDataExtractor(Data):

    __regex={
    'ContractRegex':'Contract Note No.\s[0-9]+',
    'TradeDateRegex':'Trade Date\s[0-9-a-z]+',
    'Trading':'Trading & UCC\s[0-9]+\s',
    'UCC':'[&]\s[0-9]+',
    'NameRegex':'Name\s[A-Z]+[\s]+[A-Z]+',
    }

    __replaceUseless=lambda _,target:target.replace('Contract Note No.',"") \
        .replace('Trade Date', "")\
        .replace('Trading & UCC', "").replace('Name','').replace('&','')

    def __init__(self,pdf:str,password:str='') -> None:
        super().__init__(pdf,password)

    def __mergeData(self,extractedText:str,finalResult:list)->None:
        temp=[]
        for _,v in self.__regex.items():
            temp+=[self.__replaceUseless("".join(findall(v,extractedText)))]
        finalResult.append(temp)
        temp=[]

    def extractData(self):
        return super().useText(self.__mergeData)
