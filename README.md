# Programming Language Speeds

## Information

This project was originally created to see how long it would take for various programming languages to run through similar to identical programs. However, over time, the goal of this project has changed. Now, the idea is to see how programming language run times differ on various machines and hardware. This project now includes a simple run bash script to run the code on a machine running MacOS. Future versions may include simple scripts to automatically run everything on other operating systems.

## Dependencies

- Mono; used for C Sharp to compile and execute
- Java
- Node; JavaScript executor
- TS-Node; NodeJS TypeScript executor
- Ruby
- Python3
- Lua

## Instructions to Run

In order to run the various tests, permissions for both `run.sh` and `run-all.sh` must be set to executable. This can be done by the following: `chmod +x run.sh` and `chmod +x run-all.sh`.

To run all language projects, `run-all.sh all` can be run. This would run all of the language projects using the `run.sh` file, with each language automatically being put in, with the output going to the `results` folder. If only one language needs to be run, `./run-all.sh {language}` can be run with `{language}` being the specified language to run.

To delete or reset the output files, `./run.sh reset all` can be run. If only one language needs to be reset, `./run.sh reset {language}` can be inputted, which would delete the specified language output file.

To analyze the outputs, run `python3 results-analyze.py`. This will analyze the outputted files in the `results` folder and provide the average times.

## Data

Current data in seconds

### Intel

|         Function         |     C     |   C++    |   C# |  Java     |    TypeScript     |    JavaScript    |    Lua    | Python | Ruby |
| :----------------------: | :-------: | :------: | :---: | :----------: | :-------: | :------: | :------: | :------: | :------: | 
| Hello World | 0.000008 | 0.000030 | 0.016000 | 0.000120 | 0.002000 | 0.003437 | 0.000019 | 0.000025 | 0.000010 |
| Factorial of 20 | 0.000008 | 0.000031 | 0.014000 | 0.000140 | 0.001325 | 0.003993 | 0.000022 | 0.003623 | 0.002444 |
| Summation of 1000000 | 0.002087 | 0.002143 | 0.014000 | 0.002532 | 0.002719 | 0.004033 | 0.004372 | 0.054200 | 0.034971 |
| 50th Recursive Fibonacci | 42.481205 | 44.993500 | 104.007000 | 39.050964 | 77.731000 | 71.288000 | 935.487598 | 3433.996770 | 983.176138 |
| 50th Iterative Fibonacci | 0.000010 | 0.000025 | 0.017000 | 0.000151 | 0.000131 | 0.000089 | 0.000031 | 0.000078 | 0.000034 |
| Linear Search; Maximum in 1000000 | 0.009356 | 0.009842 | 0.032000 | 0.028253 | 0.033965 | 0.035999 | 0.083719 | 0.998265 | 0.173740 |
| Print Triangle of 100 elements | 0.000454 | 0.001609 | 0.033000 | 0.131234 | 0.034649 | 0.026301 | 0.002680 | 0.014127 | 0.002308 |

### M1

|         Function         |     C     |   C++    |   C# |  Java     |    TypeScript     |    JavaScript    |    Lua    | Python | Ruby |
| :----------------------: | :-------: | :------: | :---: | :----------: | :-------: | :------: | :------: | :------: | :------: |
| Hello World | 0.000008 | 0.000009 | 0.016000 | 0.000058 | 0.000650 | 0.002200 | 0.000020 | 0.000012 | 0.000010 |
| Factorial of 20 | 0.000006 | 0.000004 | 0.014000 | 0.000140 | 0.000035 | 0.000340 | 0.000020 | 0.000040 | 0.000030 |
| Summation of 1000000 | 0.000793 | 0.000813 | 0.014000 | 0.000160 | 0.002080 | 0.002300 | 0.003722 | 0.029487 | 0.023006 |
| 50th Recursive Fibonacci | 36.409710 | 36.879400 | 104.007000 | 39.050964 | 74.878000 | 74.390000 | 1040.403432 | 2335.377700 | 761.963794 |
| 50th Iterative Fibonacci | 0.000006 | 0.000015 | 0.017000 | 0.000017 | 0.000042 | 0.000041 | 0.000050 | 0.000047 | 0.000024 |
| Linear Search; Maximum in 1000000 | 0.007715 | 0.008320 | 0.032000 | 0.007178 | 0.015793 | 0.015530 | 0.044224 | 0.451120 | 0.134323 |
| Print Triangle of 100 elements | 0.000370 | 0.001031 | 0.033000 | 0.024697 | 0.025935 | 0.009505 | 0.001086 | 0.003595 | 0.004576 |

## Computer Specifications

| Type | Computer Model | Processor | Memory | Graphics | Operating System |
| :--- | :------------: | :-------: | :----: | :--------: | :----------------: |
| Intel | MacBook Pro 13in 2019 | 2.8GHz Quad-Core Intel Core i7 | 16GB | Intel Iris Plus Graphics 655 | macOS Big Sur |
| M1 Pro | MacBook Pro 14in 2021 | Apple M1 Pro 10-CPU  | 32GB | Apple M1 Pro 16-GPU | macOS Monterey |
