# Programming Language Speeds

## Data

Data in seconds

|         Function         |     C     |   C++    |     Java     |    TypeScript     |    JavaScript    |    Python    |
| :----------------------: | :-------: | :------: | :----------: | :-------: | :------: | :------: |
| Hello World | 0.000008 | 0.000030 | 0.000120 | 0.002000 | 0.003437 | 2.479e-05 |
| Factorial of 20 | 0.000008 | 0.000031 | 0.000140 | 0.001325 | 0.003993 | 0.003623 |
| Summation of 1000000 | 0.002087 | 0.002143 | 0.002532 | 0.002719 | 0.004033 | 0.0542 |
| 50th Recursive Fibonacci | 42.983709 | 39.743700 | 46.673188 | 77.731000 | 71.288000 | 9382499.2236* |
| 50th Iterative Fibonacci | 0.000010 | 0.000025 | 0.000151 | 0.000131 | 0.000089 | 7.8e-05 |
| Linear Search; Maximum in 1000000 | 0.009356 | 0.009842 | 0.028253 | 0.033965 | 0.035999 | 0.998265 |
| Print Triangle of 10 elements | 0.000014 | 0.000054 | 0.013388 | 0.002661 | 0.005474 | 0.0002551 |

<sub>*Estimation: Note, 50th Recursive Fibonacci for Python was calculated based on how long it takes to run through 1000000 numbers, as it would theoretically run 2<sup>50</sup> times. The calculation was ((2<sup>50</sup> / 1000000 / 10) / 12) to calculate the estimated duration. This number is an estimate as it, in itself, was not completing on my machine or repl, so I calculated the estimated duration instead. </sub>