
import pdfplumber
import pandas as pd
from typing import Callable


class Data:
    def __init__(self,pdf:str,password:str='') -> None:
        self.pdf=pdfplumber.open(pdf,password=password)

    __columns=['Order No.','OrderTime','TradeNo.','TradeTime',
            'Company Name','Buy(B) /Sell(S)','Quantity','Gross Rate/trade price per Unit(Rs)'
            ,'Brokerage perUnit','NetRate perUnit(Rs)','ClosingRatePerUnit(Rs)'
            ,'NetTotal(BeforeLevies)(Rs.)','remark','Contract No','TradeDate',
            'Trading','UCC','Name'
            ,'ISIN',
            ]

    def getColumns(self)->list:
        return self.__columns

    def getPages(self)->list:
        return self.pdf.pages

    def useText(self,action:Callable[[str,list],None])->list:
        finalResult=[]
        for i in self.getPages():
            action(i.extract_text(),finalResult)
        return finalResult

    def useTables(self,action:Callable[[list],pd.DataFrame])->pd.DataFrame:
        dataList=[]
        for i in self.getPages():
            target=i.extract_table(table_settings={'vertical_strategy':'lines_strict'})
            if target:
                dataList+=target
        return action(dataList)
