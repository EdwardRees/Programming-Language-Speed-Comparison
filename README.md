# Programming Language Speeds

## Data

Data in seconds

|         Function         |     C     |   C++    |     Java     |    TypeScript     |    JavaScript    |    Python    |
| :----------------------: | :-------: | :------: | :----------: | :-------: | :------: | :------: |
| Factorial of 20 | 8e-06 | 3.1e-05 | 0.0001395 | 0.001325 | 0.003993 | 0.003623 |
| Summation of 1000000 | 0.002087 | 0.002143 | 0.002532 | 0.002719 | 0.004033 | 0.0542 |
| 50th Recursive Fibonacci | 42.983709 | 39.7437 | 46.673188157 | 77.731 | 71.288 | 9382499.2236* |
| 50th Iterative Fibonacci | 1e-05 | 2.5e-05 | 0.000150594 | 0.0001314 | 8.9e-05 | 7.8e-05 |
| Linear Search; Maximum in 1000000 | 0.009356 | 0.009842 | 0.028253198 | 0.033965 | 0.035999 | 0.998265 |

<sub>*Estimation: Note, 50th Recursive Fibonacci for Python was calculated based on how long it takes to run through 1000000 numbers, as it would theoretically run 2<sup>49</sup> times. The calculation was ((2<sup>49</sup> / 1000000 / 10) / 12) to calculate the estimated duration. This number is an estimate as it, in itself, was not completing on my machine or repl, so I calculated the estimated duration instead. </sub>