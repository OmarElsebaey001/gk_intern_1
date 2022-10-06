
import pdfplumber
import pandas as pd
from typing import Callable


class Data:
    def __init__(self,pdf:str,password:str='',dataFrameColumns:list=[]) -> None:
        self.pdf=pdfplumber.open(pdf,password=password)
        self.columns=dataFrameColumns

    def getColumns(self)->list:
        return self.columns

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
