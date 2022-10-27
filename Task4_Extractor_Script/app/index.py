


from metaDateExtractor import getMetaData
from tableExtractor import getTableData
import glob
import pandas as pd


allPdfs=glob.glob('PDFS/*')


main=[]
for pdf in allPdfs:
    print(f'Extracting {pdf}...')
    tableData=getTableData(pdf)
    metaData=getMetaData(pdf)
    for i in tableData:
        i+=metaData
        i.append(pdf.replace('Task4_Extractor_Script/PDFS/', ''))
        main.append(i)

dfColumns=['Order No.','OrderTime','TradeNo.','TradeTime',
            'Buy(B) /Sell(S)','Quantity','Gross Rate/trade price per Unit(Rs)',
            'Brokerage perUnit','NetRate perUnit(Rs)',
            'NetTotal(BeforeLevies)(Rs.)','Symbol','ISIN',
            'Company Name','Average Total(BeforeLevies)(Rs.)',
            'Total Buy','Total Sell','Name','ucc','pan','date','contNo','file'
            ]

pd.DataFrame(main,columns=dfColumns).to_csv('result.csv',index=False)
