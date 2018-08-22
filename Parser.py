#Open source file
#Remove extrinsict data
#Identify block start (define?)
#Collect llvm instructions within block
#Identify block end
#Repeat for remaining blocks
import json
import re
from collections import OrderedDict
from LDistance import minimumEditDistance

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
"llvm.memcpy", "llvm.memmove",
    }

#find first word, stop searching that line

data = []
finalData = {}
def parse(f):
    #Go through the file, appending any words that appear in the worldlist to the data list
    #p = len(f.read().split())
    #print(p)
    for words in f.read().split():
        #print(words)
        #for wordss in wordList:
            #if wordss == words:
        if words in wordList:
            data.append(words)
######
    function = data.count("define")#Count number of functions in file
    print("Number of functions: ",function)
    first = True
    counter = 0
    for i in range(function):#nested loop that will go through data and append words until define is reached
    #for the items in data
    #if the item is define, move on
    #else, add it to the dictionary at index i
        finalData[i] = []
        for n in range(len(data)):
            counter = counter+1
            if data[0] == "define" and not first:
                del data[0]
                break
            elif data[0] == "define" and first:
                first = not first
                del data[0]
                continue
            else:
                finalData[i].append(data[0])
                del data[0]

    return finalData

#dictionary with words and their assigned numbers
#compare blocks to one another using string similarity
#"AAAAAAA" - placeholder
numbers = OrderedDict((("ret","1"),("br","2"),("switch","3"),("indirectbr","4"),("invoke","5"),("resume","6"),("catswitch","7"),("catchret","8"),("cleanupret","9"),("unreachable","10"),("add","11"),
                       ("fadd","12"),("fadd","13"),("sub","14"),("fsub","15"),("mul","16"),("fmul","17"),("udiv","18"),("sdiv","19"),("fdiv","20"),("urem","21"),("srem","22"),
                       ("frem","23"),("shl","24"),("lshr","25"),("ashr","26"),("and","27"),("or","28"),("xor","29"),("extractelementm","30"),("insertelement","31"),("shufflevector","32"),("extractvalue","33"),
                       ("insertvalue","34"),("alloca","35"),("load","36"),("store","37"),("fence","38"),("cmpxchg","39"),("atomicrmw","40"),("getelementptr","41"),("trunc","42"),("zext","43"),("sext","44"),
                       ("fotruncm","45"),("fpnext","46"),("fptoui","47"),("fptosi","48"),("uitofp","49"),("sitofp","50"),("ptroint","51"),("inttoptr","52"),("bitcast","53"),("addrspacecast","54"),("icmp","55"),
                       ("fcmp","56"),("phi","57"),("select","58"),("call","59"),("va_arg","60"),("landingpad","61"),("catchpad","62"),("cleanuppad","63"),("llvm.va_start","64"),("llvm.va_end","65"),("llvm.va_copy","66"),
                       ("llvm.gcroot","67"),("llvm.gcread","68"),("llvm.gcwrite","69"),("llvm.returnaddress","70"),("llvm.addressofreturnaddress","71"),("llvm.frameaddress","72"),("llvm.localescape","73"),("llvm.write_localrecover","74"),
                       ("llvm.write_register","75"),("llvm.stacksave","76"),("llvm.stackrestore","77"),("llvm.get.dynamic.area.offset","78"),("llvm.prefetch","79"),("llvm.pcmaker","80"),("llvm.readcyclecounter","81"),("llvm.clear_cache","82"),("llvm.instropf_increment","83"),
                       ("llvm.instrprof_increment_step","84"),("llvm.instrprof_value_profile","85"),("llvm.thread.pointer","86"),("llvm.memcpy","87"),("llvm.memmove","88"),("AAAAAAA","89"),("AAAAAAA","90"),("AAAAAAA","91"),("AAAAAAA","92"),("AAAAAAA","93"),("AAAAAAA","94"),
                       ("AAAAAAA","95"),("AAAAAAA","96"),("AAAAAAA","97"),("AAAAAAA","98"),("AAAAAAA","99"),("AAAAAAA","100"),("AAAAAAA","101"),("AAAAAAA","102"),("AAAAAAA","103"),("AAAAAAA","104"),("AAAAAAA","105"),
                       ("AAAAAAA","106"),("AAAAAAA","107"),("AAAAAAA","108"),("AAAAAAA","109"),("AAAAAAA","110"),("AAAAAAA","111"),("AAAAAAA","112"),("AAAAAAA","113"),("AAAAAAA","114"),("AAAAAAA","115"),("AAAAAAA","116"),
                       ("AAAAAAA","117"),("AAAAAAA","118"),("AAAAAAA","119"),("AAAAAAA","120"),("AAAAAAA","121"),("AAAAAAA","122"),("AAAAAAA","123"),("AAAAAAA","124"),("AAAAAAA","125"),("AAAAAAA","126"),("AAAAAAA","127"),
                       ("AAAAAAA","128"),("AAAAAAA","129"),("AAAAAAA","130"),("AAAAAAA","131"),("AAAAAAA","132"),("AAAAAAA","133"),("AAAAAAA","134"),("AAAAAAA","135"),("AAAAAAA","136"),("AAAAAAA","137"),("AAAAAAA","138")))

toEvaluate = []
def assignInt():
    global toEvaluate
    orderedFinalData = OrderedDict(sorted(finalData.items(), key=lambda x:x[1], reverse = True))
    for func in range(len(finalData)):#For the number of functions
        toEvaluate.append([])
        for items in range(len(finalData[func])):#individual words in the function
            #for each word that is inside the function, iterate through the "numbers" until a match is reached. replace the key in the
            #dictionary with the numeric value
            for words in numbers:
                if words == orderedFinalData[func][items]:
                    toEvaluate[func].append(numbers[words][0])
        #convert list with numbers into an integer
        toEvaluate[func] = ''.join(toEvaluate[func])
    return toEvaluate

clones = []
def evaluate():
    for func in range(len(toEvaluate)):#for the amt of functions
        for func2 in range(func + 1, len(toEvaluate)):
            #if minimumEditDistance(toEvaluate[func],toEvaluate[func2]) == 0:#type-1 clone exact copy
            #    clones["Type-1"].append("%s and %s" % (func+1,func2+1))#add 1 to account for index numbers, to print correct function number
            if minimumEditDistance(toEvaluate[func],toEvaluate[func2]) <= 500:
                clones.append("%s and %s" % (func+1,func2+1))
                print("- Comparing Function ",func+1," ",toEvaluate[func]," and Function ",func2+1," ",toEvaluate[func2],)
                print("Similarity(Lower is closer): ",minimumEditDistance(toEvaluate[func],toEvaluate[func2]))
            #elif minimumEditDistance(toEvaluate[func],toEvaluate[func2]) >= 10:
             #   clones["Type-3"].append("%s and %s" % (func+1,func2+1))
            #print("- Comparing Function ",func+1," ",toEvaluate[func]," and Function ",func2+1," ", toEvaluate[func2])
            #print("Similarity(Lower is closer): ",minimumEditDistance(toEvaluate[func],toEvaluate[func2]))
    print('\nClones:') 
    printClones = re.sub("[{'}]", '', str(clones))
    print(printClones)
    print("Total potential clones: ",len(clones))


#llvm instructions(186)

#Similarity between the two: 23

#There is smaller similarity between other functions that are not clones

###When assigning an operation to an integer:
#br 2
#add 11
#similarity returned is 2, but really should be 1 just to signify they are different

#fix: assign to ascii values not integers; or just look to see if they are different or the same?
