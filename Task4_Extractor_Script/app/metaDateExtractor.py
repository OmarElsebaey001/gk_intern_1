import pdfplumber
import re



# Regex patterns
patterns={
'nameRegex':'Name of the Client\s?:\s?[A-Z]+\s[A-Z]+\S',
'uccRegex':'UCC & Client Code\s*:\s*[A-Z0-9]+',
'panRegex':'PAN of Client\s*:\s*[A-Z0-9]+',
'dateRegex':'Trade Date\s*:\s*[0-9]{2}/[0-9]{2}/[0-9]{4}',
'contNoRegex':'CONTRACT NOTE NO\s*:\s*[0-9]+',
}
# remove useless strings
removeOutliers=lambda target:target.replace('Name of the Client :','')\
    .replace('UCC & Client Code :', '')\
    .replace('PAN of Client :','')\
    .replace('Trade Date :','')\
    .replace('CONTRACT NOTE NO :', '')


# Extractor
def getMetaData(pdf):
    # read pdf
    reader=pdfplumber.open(pdf)

    # the array to be returned
    finalResult=[]

    # extraction operation
    for i in reader.pages:
        for _,v in patterns.items():
            t=re.findall(v,i.extract_text(),re.IGNORECASE)
            if len(t)>0 and len(finalResult)!=5:
                finalResult+=[removeOutliers(t[0])]

    return finalResult
