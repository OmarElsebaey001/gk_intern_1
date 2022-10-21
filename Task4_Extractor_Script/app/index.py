


from metaDateExtractor import getMetaData
from tableExtractor import getTableData
import glob





# allPdfs=glob.glob('Task4_Extractor_Script/PDFS/*')



# main=[]
# for pdf in allPdfs:
#     # print(pdf)
#     tableData=getTableData(pdf)
#     metaData=getMetaData(pdf)
#     for i in tableData:
#         i+=metaData
#     for i in tableData:
#         main.append(i)

# print(*main,sep='\n')



tabledata=getTableData('Task4_Extractor_Script/PDFS/CN_FG08579_GRP1_961500.PDF')

# for i in tabledata:
#     print(len(i))

# print(*tabledata,sep='\n')