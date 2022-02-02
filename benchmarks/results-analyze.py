data = {}

functionNames = ["Hello World", "Factorial 20", "Sum 1000000", "Recursive Fibonacci 50", "Iterative Fibonacci 50", "Maximum Search 1000000", "Triangle 100"]

def analyze(language, data):
  with open(f"results/{language}.txt", 'r') as f:
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
      

analyze("c", data)
analyze("cpp", data)
# print(data)
print(average(data))