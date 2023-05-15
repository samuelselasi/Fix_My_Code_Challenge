# 0x00. Fix my code
### `Debugging`
### Background Context
`Fix my code` is a new type of project, where we’ll jump into an existing code base and fix it!

Sometimes you will know the language, sometimes not.

Please download the repository [0x00-Fix_My_Code_Challenge](https://github.com/holbertonschool/0x00-Fix_My_Code_Challenge) and use it as initial files for all solutions.

You should not recode everything, just fix it!

## Requirements
### General

* Allowed editors: `vi`, `vim`, `emacs`
* All your files will be compiled on Ubuntu 20.04 LTS
* All your files should end with a new line
* A `README.md` file, at the root of the folder of the project is mandatory

## Tasks

[0. FizzBuzz](./0-fizzbuzz.py)

Please take a look at my implementation of FizzBuzz in Python: [source code](https://github.com/holbertonschool/0x00-Fix_My_Code_Challenge/blob/master/0-fizzbuzz.py)

Something is going wrong….
```
$ ./0-fizzbuzz.py 50
1 2 Fizz 4 Buzz Fizz 7 8 Fizz Buzz 11 Fizz 13 14 Fizz 16 17 Fizz 19 Buzz Fizz 22 23 Fizz Buzz 26 Fizz 28 29 Fizz 31 32 Fizz 34 Buzz Fizz 37 38 Fizz Buzz 41 Fizz 43 44 Fizz 46 47 Fizz 49 Buzz
$
```
`15` should print `FizzBuzz` not `Fizz`

[1. Print square](./1-print_square.js)

Please take a look at my implementation of printing a square in Javascript: [source code](https://github.com/holbertonschool/0x00-Fix_My_Code_Challenge/blob/master/1-print_square.js)

Something is going wrong….
```
$ ./1-print_square.js 4
####
####
####
####
$ ./1-print_square.js 10
################
################
################
################
################
################
################
################
################
################
################
################
################
################
################
################
$
```
`./1-print_square.js 10` should print a square of size 10…

[2. Sort](./2-sort.rb)

Please find here my implementation of sorting arguments in Ruby: [source code](https://github.com/holbertonschool/0x00-Fix_My_Code_Challenge/blob/master/2-sort.rb)

Something is going wrong….
```
$ ruby 2-sort.rb 12 41 2 C 9 -9 31 fun -1 32
31
32
12
41
2
9
-9
-1
$
```
