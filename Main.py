#Removing the printing of functions in Parser.py will speedup runtime (line 102)
import Parser
import os
uInput = ''
fileList = []
functionNames = []
fileCount = 0

while True:
    while uInput != 'done':
        found = False
        print('Total Files loaded: ',fileCount)
        print("\nInput directory then type 'done': ")
        uInput = input()
        print('Loading files.')
        for root, dirs, files in os.walk(uInput):
            for file in files:
                if file.endswith(".ll"):
                    found = True
                    fileCount = fileCount + 1
                    fileList.append(os.path.join(root,file))
        if not found and uInput != 'done':
            print('No files found.')
    print('Reading files.\n')
    with open ("file.txt","wb") as outfile:
        for f in fileList:
            with open(f, "rb")as infile:
                outfile.write(infile.read())
    f = open("file.txt", "r")
    Parser.parse(f,fileList,functionNames)
    Parser.evaluateLEV(functionNames)
    Parser.finalData = {}
    uInput = ''
    fileCount = 0
    Parser.data,Parser.toEvaluate,Parser.clones,fileList,functionNames = [],[],[],[],[]
    Parser.theData = {'data':[]}
