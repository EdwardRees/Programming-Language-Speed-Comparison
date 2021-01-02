from sys import argv


def parse(file):
    data = {}
    with open(file, "r") as f:
        for line in f:
            line = line.strip()
            if("#" in line):
                continue
            [functionName, c, cpp, java, ts, js, lua, py, ruby] = line.split(",")
            data[functionName.strip()] = {"C": float(c.strip()), "C++": float(cpp.strip()),
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


def writeFastestShortest(data):
    fastest = getFastestLanguagesPerFunction(data)
    slowest = getSlowestLanguagesPerFunction(data)
    with open("analysis.md", "w") as f:
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
            print("-p: Print fastest and shortest data to console *default*")
            print("-r: Write readme")
            print("-o: Write fastest and slowest to analysis.md file")
            print("-u: Update both README.md and analysis.md")
        elif(argv[1] == "-r"):
            writeReadme(data)
            print("Updated README.md file")
        elif(argv[1] == '-p'):
            printFastestShortest(data)
        elif(argv[1] == '-o'):
            writeFastestShortest(data)
            print("Updated analysis.md file")
        elif(argv[1] == '-u'):
            writeFastestShortest(data)
            print("Updated README.md file")
            writeReadme(data)
            print("Updated analysis.md file")
        else:
            print("Options are:")
            print("-h: This help menu")
            print("-p: Print fastest and shortest data to console *default*")
            print("-r: Write readme")
            print("-o: Write fastest and slowest to analysis.md file")
            print("-u: Update both README.md and analysis.md")


def writeReadme(data):
    with open("README.md", "w") as f:
        f.write("# Programming Language Speeds\n")
        f.write("\n")
        f.write("## Data\n")
        f.write("\n")
        f.write("Data in seconds\n")
        f.write("\n")
        f.write("|         Function         |     C     |   C++    |     Java     |    TypeScript     |    JavaScript    |    Lua    | Python | Ruby |\n")
        f.write("| :----------------------: | :-------: | :------: | :----------: | :-------: | :------: | :------: | :------: | :------: | \n")
        for func in data:
            vals = data[func]
            py = f'{vals["Python"]:.6f}'
            lua = f'{vals["Lua"]:.6f}'
            ruby = f'{vals["Ruby"]:.6f}'
            if(func == '50th Recursive Fibonacci'):
              lua = str(lua) + "<sup>[1]</sup>"
              py = str(py) + "<sup>[2]</sup>"
              ruby = str(ruby) + "<sup>[3]</sup>"
            f.write(
                f"| {func} | {vals['C']:.6f} | {vals['C++']:.6f} | {vals['Java']:.6f} | {vals['TypeScript']:.6f} | {vals['JavaScript']:.6f} | {lua} | {py} | {ruby} | \n")
        f.write("\n<sup>[1]</sup> Estimation: Note, 50th Recursive Fibonacci for Lua was calculated based on how long it takes to run through 1000000 numbers, as it would theoretically run 2<sup>50</sup> times. The calculation was <code>(2<sup>50</sup> / 1000000 / 8)</code> to calculate the estimated duration. This number is an estimate as it, in itself, was not completing on my machine or repl, so I calculated the estimated duration instead. </sub>")
        f.write("\n<sup>[2]</sup> Estimation: Note, 50th Recursive Fibonacci for Python was calculated based on how long it takes to run through 1000000 numbers, as it would theoretically run 2<sup>50</sup> times. The calculation was <code>((2<sup>50</sup> / 1000000 / 10) / 12)</code> to calculate the estimated duration. This number is an estimate as it, in itself, was not completing on my machine or repl, so I calculated the estimated duration instead. </sub>")
        f.write("\n<sup>[3]</sup> Estimation: Note, 50th Recursive Fibonacci for Ruby was calculated based on how long it takes to run through 1000000 numbers, as it would theoretically run 2<sup>50</sup> times. The calculation was <code>(2<sup>50</sup> / 1000000 / 11)</code> to calculate the estimated duration. This number is an estimate as it, in itself, was not completing on my machine or repl, so I calculated the estimated duration instead. </sub>")
    f.close()


main()
