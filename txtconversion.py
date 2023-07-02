import PyPDF2
i=1
while i<849:
    a=PyPDF2.PdfFileReader('document'+str(i)+'.pdf')
    pages=a.getNumPages()
    strr=""
    for j in range(1,pages):
        strr+=a.getPage(j).extractText()
    with open("document"+str(i)+".txt","w",encoding='utf-8') as f:
        f.write(strr)
    i=i+1