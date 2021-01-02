# Programming Language Speeds

## Data

Data in seconds

|         Function         |     C     |   C++    |     Java     |    TypeScript     |    JavaScript    |    Lua    | Python | Ruby |
| :----------------------: | :-------: | :------: | :----------: | :-------: | :------: | :------: | :------: | :------: | 
| Hello World | 0.000008 | 0.000030 | 0.000120 | 0.002000 | 0.003437 | 0.000019 | 0.000025 | 0.000010 | 
| Factorial of 20 | 0.000008 | 0.000031 | 0.000140 | 0.001325 | 0.003993 | 0.000022 | 0.003623 | 0.002444 | 
| Summation of 1000000 | 0.002087 | 0.002143 | 0.002532 | 0.002719 | 0.004033 | 0.004372 | 0.054200 | 0.034971 | 
| 50th Recursive Fibonacci | 42.983709 | 39.743700 | 46.673188 | 77.731000 | 71.288000 | 140737488.355328<sup>[1]</sup> | 9382499.223600<sup>[2]</sup> | 102354536.985693<sup>[3]</sup> | 
| 50th Iterative Fibonacci | 0.000010 | 0.000025 | 0.000151 | 0.000131 | 0.000089 | 0.000031 | 0.000078 | 0.000034 | 
| Linear Search; Maximum in 1000000 | 0.009356 | 0.009842 | 0.028253 | 0.033965 | 0.035999 | 0.083719 | 0.998265 | 0.173740 | 
| Print Triangle of 100 elements | 0.000454 | 0.001609 | 0.131234 | 0.034649 | 0.026301 | 0.002680 | 0.014127 | 0.002308 | 

<sup>[1]</sup> Estimation: Note, 50th Recursive Fibonacci for Lua was calculated based on how long it takes to run through 1000000 numbers, as it would theoretically run 2<sup>50</sup> times. The calculation was <code>(2<sup>50</sup> / 1000000 / 8)</code> to calculate the estimated duration. This number is an estimate as it, in itself, was not completing on my machine or repl, so I calculated the estimated duration instead. </sub>
<sup>[2]</sup> Estimation: Note, 50th Recursive Fibonacci for Python was calculated based on how long it takes to run through 1000000 numbers, as it would theoretically run 2<sup>50</sup> times. The calculation was <code>((2<sup>50</sup> / 1000000 / 10) / 12)</code> to calculate the estimated duration. This number is an estimate as it, in itself, was not completing on my machine or repl, so I calculated the estimated duration instead. </sub>
<sup>[3]</sup> Estimation: Note, 50th Recursive Fibonacci for Ruby was calculated based on how long it takes to run through 1000000 numbers, as it would theoretically run 2<sup>50</sup> times. The calculation was <code>(2<sup>50</sup> / 1000000 / 11)</code> to calculate the estimated duration. This number is an estimate as it, in itself, was not completing on my machine or repl, so I calculated the estimated duration instead. </sub>