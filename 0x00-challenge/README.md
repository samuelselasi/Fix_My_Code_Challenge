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

### Fix
* Ccheck for `FizzBiuzz` should be first in `if else` statement else the `Fizz` will be printed for numbers that are divisible by both `3` and `5` because `Fizz` was checked first

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

### Fix
* The code `size = parseInt(process.argv[2], 16)` is used to convert a hexadecimal (base `16`) string representation of a number into its decimal (base `10`) equivalent and assign it to the variable size.
* Remove `16` to avoid conversion from base 16 to base 10 for line `17` to be `size = parseInt(process.argv[2])`

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

### Fix
* Modifying the insert statement to `result.insert(i, i_arg)` to insert the element at index `i` instead of `i - 1` on line 23

[3. User password](./3-user.py)

Please find here my implementation of a User class in Python: [source code](https://github.com/holbertonschool/0x00-Fix_My_Code_Challenge/blob/master/3-user.py)

Something is going wrong….
```
$ ./3-user.py 
Test User
is_valid_password should return True if it's the right password
$
```
My tests should not print any error…

### Fix
* Typo in `password` function where `__password` is written as `_password` on line `43`
* Comparison in `is_valid_password` function where hashed password is being compared with uppercase hexadecimal (`return hashlib.md5(pwd.encode()).hexdigest().upper() == self.__password`) instead of lowercase hexadecimal (`return hashlib.md5(pwd.encode()).hexdigest().lowe() == self.__password`) as it was set in the `password` function on line 57
