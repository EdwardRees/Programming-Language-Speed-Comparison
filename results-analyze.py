import json

data = {}

languageNames = ["c", "c++", "c#", "java", "typescript", "javascript", "lua", "python", "ruby"]

def minutesToSeconds(minutes):
  return minutes * 60

def analyze(language, data):
  with open(f"benchmarks/results/{language}.txt", 'r') as f:
    data[language] = {}
    contents = f.read()
    sections = contents.split(">> ")
    sections = sections[1:]
    for section in sections:
      section = section.split("\n")
      function = section[0]
      data[language][function] = []
      for line in section[1:]:
        if line.startswith("Time spent:"):
          time = line.split(": ")[1]
          if("ms" in time):
            time = time.replace("ms", "")
          if("," in time):
            timeSections = time.split(",")
            time = minutesToSeconds(float(timeSections[0])) + float(timeSections[1])
          if(":" in time):
            timeSections = time.split(":")
            time = minutesToSeconds(float(timeSections[0])) + float(timeSections[1]) * 60
          time = float(time)
          data[language][function].append(time)
  return data

def average(data):
  return {
    language: {
      function: sum(data[language][function]) / len(data[language][function])
      for function in data[language]
    }
    for language in data
  }

def getConfig():
  with open("config.json", 'r') as f:
    return json.load(f)

def createAnalysisFile(data):
  config = getConfig()
  functions = ["Hello World", "Factorial of 20", "Summation of 1000000", "50th Recursive Fibonacci", "50th Iterative Fibonacci", "Linear Search; Maximum in 1000000", "Print Triangle of 100 elements"]
  avgData = average(data)
  languages = []
  string = ""
  for language in avgData:
    languages.append(language)
  string += "#Function,"
  for language in languages:
    string += f"{language.capitalize()},"
  string = string[:-1]
  string += "\n"
  for i in range(len(functions)):
    string += f"{functions[i]},"
    for language in languages:
      string += f"{avgData[language][str(i)]:.7f},"
    string = string[:-1]
    string += "\n"
  print(string)

def analyzeAll(data):
  for language in languageNames:
    try:
      data = analyze(language, data)
    except FileNotFoundError:
      continue
  

analyzeAll(data)
createAnalysisFile(data)