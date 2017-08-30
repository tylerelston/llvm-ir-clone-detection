import pprint
from collections import OrderedDict
from Levenshtein import *
import time
from itertools import product
wordList = {
"define","ret", "br", "switch", "indirectbr", "invoke", "resume", "catswitch", "catchret", "cleanupret",
"unreachable", "add", "fadd", "sub", "fsub", "mul", "fmul", "udiv", "sdiv", "fdiv", "urem", "srem",
"frem", "shl", "lshr", "ashr", "and", "or", "xor", "extractelementm", "insertelement",
"shufflevector", "extractvalue", "insertvalue", "alloca", "load", "store", "fence",
"cmpxchg", "atomicrmw", "getelementptr", "trunc", "zext", "sext", "fotruncm", "fpnext",
"fptoui", "fptosi", "uitofp", "sitofp", "ptroint", "inttoptr", "bitcast", "addrspacecast",
"icmp", "fcmp", "phi", "select", "call", "va_arg", "landingpad", "catchpad", "cleanuppad",
"llvm.va_start", "llvm.va_end", "llvm.va_copy", "llvm.gcroot", "llvm.gcread",
"llvm.gcwrite", "llvm.returnaddress", "llvm.addressofreturnaddress", "llvm.frameaddress",
"llvm.localescape", "llvm.write_localrecover", "llvm.read_register", "llvm.write_register",
"llvm.stacksave", "llvm.stackrestore", "llvm.get.dynamic.area.offset", "llvm.prefetch",
"llvm.pcmaker", "llvm.readcyclecounter", "llvm.clear_cache", "llvm.instropf_increment",
"llvm.instrprof_increment_step", "llvm.instrprof_value_profile", "llvm.thread.pointer",
"llvm.memcpy", "llvm.memmove"}

numbers = OrderedDict((("define","0"),("ret","1"),("br","2"),("switch","3"),("indirectbr","4"),("invoke","5"),("resume","6"),("catswitch","7"),("catchret","8"),("cleanupret","9"),("unreachable","A"),("add","B"),
                       ("fadd","C"),("fadd","D"),("sub","E"),("fsub","F"),("mul","G"),("fmul","H"),("udiv","I"),("sdiv","J"),("fdiv","K"),("urem","L"),("srem","M"),
                       ("frem","N"),("shl","O"),("lshr","P"),("ashr","Q"),("and","R"),("or","S"),("xor","T"),("extractelementm","U"),("insertelement","V"),("shufflevector","W"),("extractvalue","X"),
                       ("insertvalue","Y"),("alloca","Z"),("load","!"),("store","@"),("fence","#"),("cmpxchg","$"),("atomicrmw","%"),("getelementptr","^"),("trunc","&"),("zext","*"),("sext","("),
                       ("fotruncm",")"),("fpnext","-"),("fptoui","="),("fptosi","a"),("uitofp","b"),("sitofp","c"),("ptroint","d"),("inttoptr","e"),("bitcast","f"),("addrspacecast","g"),("icmp","h"),
                       ("fcmp","i"),("phi","j"),("select","k"),("call","l"),("va_arg","m"),("landingpad","n"),("catchpad","o"),("cleanuppad","p"),("llvm.va_start","q"),("llvm.va_end","r"),("llvm.va_copy","s"),
                       ("ModuleID","t"),("llvm.gcread","u"),("llvm.gcwrite","v"),("llvm.returnaddress","w"),("llvm.addressofreturnaddress","x"),("llvm.frameaddress","y"),("llvm.localescape","z"),("llvm.write_localrecover","<"),
                       ("llvm.write_register","}"),("llvm.stacksave",";"),("llvm.stackrestore",":"),("llvm.get.dynamic.area.offset","'"),("llvm.prefetch",","),("llvm.pcmaker","."),("llvm.readcyclecounter","["),("llvm.clear_cache","]"),("llvm.instropf_increment","{"),
                       ("llvm.instrprof_increment_step","?"),("llvm.instrprof_value_profile","`")))

data = []

theData = {'data':[]

    }
dataCalls = {}
finalData = {}
def parse(f,file,functionNames):
    print('Parsing')
    printFunctions = ''
    counter = 1
    global function
    fileChange = True
    currentFile = ''
    currentIndex = 0
    funcCount = -1
    counter2 = 0
    listsWrite = open("list.txt","w")
    splitFile = f.readlines()
    time0 = time.time()
    for line in splitFile:
        line = line.split()
        currentWordIndex = -1
        for words in line:
            currentWordIndex +=1
            if words in numbers:
                if words == 'ModuleID':
                    currentFile = line[3]
                    fileChange = True
                if words == 'define':
                    fileChange = False
                    while '@' not in line[counter]:
                        counter = counter + 1
                        if '@' in line[counter]:
                            toEvaluate.append([])
                            wordd = currentFile + '.'+line[counter].split("(")[0]
                            functionNames.append(wordd)
                            dataCalls[wordd] = []
                            listsWrite.write("\n\n%s\n"%wordd)
                            funcCount = funcCount + 1
                            break
                if words == 'call':
                    try:
                        while '@' not in line[currentWordIndex+counter2]:# != '@':
                            counter2 = counter2 + 1
                            try:
                                if '@' in line[currentWordIndex+counter2]:
                                    dataCalls[wordd].append(line[currentWordIndex+counter2].split("(")[0])
                                    toEvaluate[funcCount].append(numbers[words])
                                    break
                            except:
                                dataCalls[wordd].append('POINTER')
                    except:
                        pass
                elif funcCount > -1 and words != "ModuleID" and not fileChange:#ensure no operation words before the declaration of the first function are added
                    toEvaluate[funcCount].append(numbers[words])
                    listsWrite.write(numbers[words])
                counter = 0
                counter2 = -1
    count = 0
    for func in toEvaluate:
        func = ''.join(func)
        theData['data'].append([functionNames[count],func])
        count += 1
    
    time1 = time.time()
    function = len(toEvaluate)
    pp = pprint.PrettyPrinter(indent=3)
    print("Number of functions: ",funcCount+1,'\n')
    print('Parse time: ', time1 - time0)
    pp.pprint(dataCalls)
    return function,data,functionNames


toEvaluate = []
clones = []
def evaluateLEV(functionNames):
    count= 0
    cloness = 0
    comparison = ''
    minSize = 20

    while type(comparison) is not float:
        print("How similar should two functions be to be considered a clone?(0.0 to 1.0)")
        print("Smaller is closer")
        try:
           comparison = float(input())
        except:
            print("Input a number.")
    while type(minSize) is not float:
        print("Minimum function block size?")
        try:
           minSize = float(input())
        except:
            print("Input a number.")
    print("\nComparing using Levenshtein Distance")
    time0 = time.time()
    for dataLength in theData:

        count = 0
        for func in range(len(theData[dataLength])):
            if len(theData[dataLength][func][1]) < minSize:
                continue  
            count +=1
            for func2 in range(func+1,len(theData[dataLength])):
                if (len(theData[dataLength][func][1])-len(theData[dataLength][func2][1]))/len(theData[dataLength][func][1]) >= 0.5:
                    continue
                if abs(len(theData[dataLength][func][1])-len(theData[dataLength][func2][1])) > 1000:
                    continue
                funcLength = len(theData[dataLength][func][1])
                func2Length = len(theData[dataLength][func2][1])
                if funcLength > func2Length:
                    maxn = funcLength
                    minn = func2
                    other = func
                else:
                    maxn = func2Length
                    minn = func
                    other = func2
                callMin = 0
                callOther = 0
                callCount = 0
                temp1 = theData[dataLength][minn][1]
                temp2 = theData[dataLength][other][1]
                for operators in range(len(theData[dataLength][minn][1])):
                    if theData[dataLength][minn][1][operators] == 'l' and theData[dataLength][other][1][operators] == 'l':
                        if dataCalls[theData[dataLength][minn][0]][callMin] != dataCalls[theData[dataLength][other][0]][callOther]:
                            callCount =+ 1
                        callMin += 1
                        callOther += 1
                for i in range(callCount):
                    temp1 = temp1.replace('l','~',1)
                    temp2 = temp2.replace('l','',1)
                editDist = distance(temp1,temp2)
                if editDist == 0:
                    cloness += 1
                    editSim = 0
                    clones.append("{} {} with [{}] similarity".format (theData[dataLength][func][0],theData[dataLength][func2][0],round(editSim,2)))
                    continue
                try:
                    editSim = editDist/maxn
                except:
                    editSim = 0
                if editSim <= comparison:
                    clones.append("{} {} with [{}] similarity".format (theData[dataLength][func][0],theData[dataLength][func2][0],round(editSim,2)))
    time1 = time.time()
    pp = pprint.PrettyPrinter(indent=3)
    pp.pprint(clones)
    with open ("resultslev.txt","w") as results:
        for clone in clones:
            results.write(clone)
            results.write("\n")
    print('Results written to resultslev.txt')
    print('time: ',time1 - time0)
    print("Total potential clone pairs: ",len(clones),'\n--------------------------\n')
