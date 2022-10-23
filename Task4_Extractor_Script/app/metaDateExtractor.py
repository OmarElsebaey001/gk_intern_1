import pdfplumber
import re



# Regex patterns
patterns={'nameRegex':'Name of the Client\s?:\s?[A-Z]+\s[A-Z]+\S',# remove Name of the Client :
'uccRegex':'UCC Code\s*:\s*[A-Z0-9]+', # remove UCC Code :
'panRegex':'PAN of Client\s*:\s*[A-Z0-9]+',
'dateRegex':'Trade Date\s*:\s*[0-9]{2}/[0-9]{2}/[0-9]{4}', # remove Trade Date :
'contNoRegex':'contract no.\s*[0-9]+'}

# remove useless strings
removeOutliers=lambda target:target.replace('Name of the Client :','')\
    .replace('UCC Code :', '')\
    .replace('PAN of Client :','')\
    .replace('Trade Date :','')\
    .replace('contract no.', '')


# Extractor
def getMetaData(pdf):
    # read pdf
    reader=pdfplumber.open(pdf)

    # the array to be returned
    finalResult=[]

    # extraction operation
    for i in reader.pages:
        ans={}
        for key,v in patterns.items():
            t=re.findall(v,i.extract_text(),re.IGNORECASE)
            if len(t)>0 and len(finalResult)!=5:
                # finalResult+=[removeOutliers(t[0])]
                ans[key]=removeOutliers(t[0])
        for k,_ in patterns.items():
            finalResult+=ans[k]

    return finalResult
