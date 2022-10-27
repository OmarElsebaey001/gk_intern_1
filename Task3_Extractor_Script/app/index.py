
from TableDataClass import TableData
import pandas as pd
import glob

allPdfs=glob.glob('PDFS/*')


main=[]
for pdf in allPdfs:
    print(f'Extracting {pdf}...')
    extractor=TableData(pdf)
    temp=extractor.extractData()
    temp['File']=pdf.replace('Task3_Extractor_Script/PDFS/',"")
    main.append(temp)

pd.concat(main,ignore_index=True).to_csv('result.csv',index=False)
