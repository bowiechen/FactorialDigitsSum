# The Factorial Digits Sum Puzzle
Inspired by YouTube channel [Mind Your Decisions](https://www.youtube.com/watch?v=gAPNzzeNWZg).

## Problem Statement
Given `ABC = A! + B! + C!`, where `A`, `B`, `C` are integers between 1 and 9, find the solution tuples `(A, B, C)`. 

I provide the solution code to find solutions for arbitrary digits. That is, the problem statement which this solution code works is:

Given `AB...K = A! + B! + ... + K!`, where `A..K` are integers between (0|1) and 9, find the solution tuples `(A, B, ..., K)`. 

## Usage
```
usage: Factorial_Digits_Sum.py [-h] [-z] [-m MULTICORE] digits

```

`-z`, `-0`, `--allow_zero` allow zeros to be part of the calculation

`-m MULTICORE`, `--multicore MULTICORE` how many cores to use. if an invalid integer is given, '1' is used

