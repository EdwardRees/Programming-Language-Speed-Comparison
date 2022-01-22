from sys import argv

def parse(file):
    data = {}
    with open(file, "r") as f:
        for line in f:
            line = line.strip()
            if("#" in line):
                continue
            [functionName, c, cpp, cs, java, ts,
                js, lua, py, ruby] = line.split(",")
            data[functionName.strip()] = {"C": float(c.strip()), "C++": float(cpp.strip()), "C#": float(cs.strip()),
                                          "Java": float(java.strip()), "TypeScript": float(ts.strip()), "JavaScript": float(js.strip()), "Python": float(py.strip()), "Lua": float(lua.strip()), "Ruby": float(ruby.strip())}
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


def writeFastestShortest(data, filename):
    fastest = getFastestLanguagesPerFunction(data)
    slowest = getSlowestLanguagesPerFunction(data)
    with open(filename, "w") as f:
        f.write("# Programming Language Speeds Analysis\n")
        f.write("\n")
        f.write("## Fastest\n\n")
        for key in fastest:
            f.write(
                f"- **{key}**: <u>{list(fastest[key].keys())[0]}</u> at {fastest[key][list(fastest[key].keys())[0]]:.6f} seconds\n\n")
        f.write("## Slowest\n\n")
        for key in slowest:
            f.write(
                f"- **{key}**: <u>{list(slowest[key].keys())[0]}</u> at {slowest[key][list(slowest[key].keys())[0]]:.6f} seconds\n\n")


def writeReadme(data):
    with open("README.md", "w") as f:
        f.write("# Programming Language Speeds\n")
        f.write("\n")
        f.write("## Data\n")
        f.write("\n")
        f.write("Data in seconds\n")
        f.write("\n")
        f.write("### Intel\n")
        f.write('\n')
        f.write("|         Function         |     C     |   C++    |   C# |  Java     |    TypeScript     |    JavaScript    |    Lua    | Python | Ruby |\n")
        f.write("| :----------------------: | :-------: | :------: | :---: | :----------: | :-------: | :------: | :------: | :------: | :------: | \n")
        for func in data["intel"]:
            vals = data["intel"][func]
            py = f'{vals["Python"]:.6f}'
            lua = f'{vals["Lua"]:.6f}'
            ruby = f'{vals["Ruby"]:.6f}'
            f.write(
                f"| {func} | {vals['C']:.6f} | {vals['C++']:.6f} | {vals['C#']:6f} | {vals['Java']:.6f} | {vals['TypeScript']:.6f} | {vals['JavaScript']:.6f} | {lua} | {py} | {ruby} |\n")
      
        f.write('\n')
        f.write("### M1\n")
        f.write('\n')
        f.write("|         Function         |     C     |   C++    |   C# |  Java     |    TypeScript     |    JavaScript    |    Lua    | Python | Ruby |\n")
        f.write("| :----------------------: | :-------: | :------: | :---: | :----------: | :-------: | :------: | :------: | :------: | :------: |\n")
        for func in data["m1"]:
            vals = data["m1"][func]
            py = f'{vals["Python"]:.6f}'
            lua = f'{vals["Lua"]:.6f}'
            ruby = f'{vals["Ruby"]:.6f}'
            f.write(
                f"| {func} | {vals['C']:.6f} | {vals['C++']:.6f} | {vals['C#']:6f} | {vals['Java']:.6f} | {vals['TypeScript']:.6f} | {vals['JavaScript']:.6f} | {lua} | {py} | {ruby} |\n")
        f.write("\n")
        f.write("## Computer Specifications\n\n")
        f.write("| Type | Computer Model | Processor | Memory | Graphics | Operating System |\n")
        f.write("| :--- | :------------: | :-------: | :----: | :--------: | :----------------: |\n")
        f.write("| Intel | MacBook Pro 13in 2019 | 2.8GHz Quad-Core Intel Core i7 | 16GB | Intel Iris Plus Graphics 655 | macOS Big Sur |\n")
        f.write("| M1 | MacBook Pro 14in 2021 | Apple M1 Pro 10-CPU  | 32GB | Apple M1 Pro 16-GPU | macOS Monterey |\n")
        f.write("")
    f.close()





def main():
    intel = parse("intel.csv")
    m1 = parse("m1.csv")
    data = {}
    data["intel"] = intel
    data["m1"] = m1
    if(len(argv) == 1):
        print("Defaulting to printing fastest and shortest values")
        print("-" * 10)
        print("Intel")
        printFastestShortest(data["intel"])
        print()
        print("M1")
        printFastestShortest(data["m1"])
    else:
        if(argv[1] == "-h"):
            print("Options are:")
            print("-h: This help menu")
            print("-p: Print fastest and shortest data to console *default*")
            print("-r: Write readme")
            print("-o: Write fastest and slowest to analysis.md file")
            print("-u: Update both README.md and analysis.md")
        elif(argv[1] == "-r"):
            writeReadme(data)
            print("Updated README.md file")
        elif(argv[1] == '-p'):
            print("Intel")
            printFastestShortest(data["intel"])
            print()
            print("M1")
            printFastestShortest(data["m1"])
        elif(argv[1] == '-o'):
            writeFastestShortest(data['intel'], "intel-analysis.md")
            writeFastestShortest(data['m1'], "m1-analysis.md")
            print("Updated analysis files")
        elif(argv[1] == '-u'):
            writeFastestShortest(data['intel'], "intel-analysis.md")
            writeFastestShortest(data['m1'], "m1-analysis.md")
            print("Updated analysis files")
            writeReadme(data)
            print(f"Updated README.md file")
        else:
            print("Options are:")
            print("-h: This help menu")
            print("-p: Print fastest and shortest data to console *default*")
            print("-r: Write readme")
            print("-o: Write fastest and slowest to analysis.md file")
            print("-u: Update both README.md and analysis.md")
main()