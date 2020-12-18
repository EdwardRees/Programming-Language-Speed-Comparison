from sys import argv


def parse(file):
    data = {}
    with open(file, "r") as f:
        for line in f:
            line = line.strip()
            if("#" in line):
                continue
            [functionName, c, cpp, java, ts, js, py] = line.split(",")
            data[functionName.strip()] = {"c": float(c.strip()), "c++": float(cpp.strip()),
                                          "java": float(java.strip()), "ts": float(ts.strip()), "js": float(js.strip()), "py": float(py.strip())}
    return data


def analyzeFunction(functionName, data):
    functionData = data.get(functionName, None)
    if(functionData == None):
        return f"No function named {functionName}"
    fastestValue = min(functionData.values())
    fastestKey = ""
    slowestValue = max(functionData.values())
    slowestKey = ""
    for key in functionData:
        if(functionData[key] == fastestValue):
            fastestKey = key
        if(functionData[key] == slowestValue):
            slowestKey = key
    return {functionName: {"Fastest": {fastestKey: fastestValue}, "Slowest": {slowestKey: slowestValue}}}


def getFastestLanguagesPerFunction(data):
    functionNames = data.keys()
    fastest = {}
    for functionName in functionNames:
        stats = analyzeFunction(functionName, data)
        fastest[functionName] = stats[functionName]["Fastest"]
    return fastest


def getSlowestLanguagesPerFunction(data):
    functionNames = data.keys()
    slowest = {}
    for functionName in functionNames:
        stats = analyzeFunction(functionName, data)
        slowest[functionName] = stats[functionName]["Slowest"]
    return slowest


def printDictionary(data):
    # Assume data is a nested dictionary
    for key in data:
        print(
            f"{key}: {list(data[key].keys())[0]} at {data[key][list(data[key].keys())[0]]} seconds")


def printFastestShortest(data):
    print("Fastest: ")
    printDictionary(getFastestLanguagesPerFunction(data))
    print()
    print("Slowest: ")
    printDictionary(getSlowestLanguagesPerFunction(data))

def writeFastestShortest(data):
  fastest = getFastestLanguagesPerFunction(data)
  slowest = getSlowestLanguagesPerFunction(data)
  with open("analysis.md", "w") as f:
        f.write("# Programming Language Speeds Analysis\n")
        f.write("\n")
        f.write("## Fastest\n\n")
        for key in fastest:
            f.write(f"- {key}: {list(fastest[key].keys())[0]} at {fastest[key][list(fastest[key].keys())[0]]} seconds\n\n")
        f.write("## Slowest\n\n")
        for key in slowest:
            f.write(f"- {key}: {list(slowest[key].keys())[0]} at {slowest[key][list(slowest[key].keys())[0]]} seconds\n\n")




def main():
    data = parse("data.csv")
    if(len(argv) == 1):
        print("Defaulting to printing fastest and shortest values")
        print("-" * 10)
        printFastestShortest(data)
    else:
        if(argv[1] == "-h"):
            print("Options are:")
            print("-h: This help menu")
            print("-r: Write readme")
            print("-o: Write fastest and slowest to analysis.md file")
            print("-p: Print fastest and shortest data to console *default*")
        elif(argv[1] == "-r"):
            writeReadme(data)
            print("Updated README.md file")
        elif(argv[1] == '-p'):
            printFastestShortest(data)
        elif(argv[1] == '-o'):
            writeFastestShortest(data)
            print("Updated analysis.md file")
        else:
            print("Options are:")
            print("-h: This help menu")
            print("-r: Write readme")
            print("-o: Write fastest and slowest to analysis.md file")
            print("-p: Print fastest and shortest data to console *default*")


def writeReadme(data):
    with open("README.md", "w") as f:
        f.write("# Programming Language Speeds\n")
        f.write("\n")
        f.write("## Data\n")
        f.write("\n")
        f.write("Data in seconds\n")
        f.write("\n")
        f.write("|         Function         |     C     |   C++    |     Java     |    TS     |    JS    |    Py    |\n")
        f.write("| :----------------------: | :-------: | :------: | :----------: | :-------: | :------: | :------: |\n")
        for func in data:
            vals = data[func]
            f.write(
                f"| {func} | {vals['c']} | {vals['c++']} | {vals['java']} | {vals['ts']} | {vals['js']} | {vals['py']} |\n")
    f.close()


main()
