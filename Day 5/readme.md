# Day 5 – Functions, Problem Solving and Python Challenges

## Overview

This folder contains my Day 5 Python practice programs focused mainly on **functions, loops, conditional logic, lists, randomisation, and problem-solving**.

The exercises gradually move from creating simple reusable functions to solving practical programming challenges such as finding prime numbers, simulating a dice battle, generating secure passwords, and navigating obstacles using the Reeborg environment.

## Programs

### 1. Basic Function – Sum, Product and Difference

Defines a custom function that accepts two numbers from the user and calculates their:

* Sum
* Product
* Difference

The program also uses conditional logic to calculate the difference as a positive value. This exercise introduces the basic structure of defining and calling a Python function.

**Concepts:** Functions, `def`, function calls, user input, arithmetic operations, conditional statements.

---

### 2. Prime Number List

Takes a list of numbers and identifies all the **prime numbers** present in it.

The program uses nested `for` loops to check whether each number is divisible by any number between `2` and itself. The identified prime numbers are stored in a separate list and returned from the function.

**Concepts:** Functions, nested loops, lists, modulo operator, conditional logic, `break`, `return`.

---

## Reeborg Robot Challenges

The folder also contains solutions to different challenges from the **Reeborg's World** Python programming environment. These exercises helped practice writing functions and loops while solving navigation problems logically.

### 3. Hurdle 1

A basic robot navigation challenge where the robot needs to repeatedly jump over hurdles until it reaches the goal.

The solution uses a `while` loop along with movement and turning commands.

**Concepts:** `while` loops, functions, repeated actions, conditional execution.

### 4. Hurdle 4

A more advanced hurdle challenge where the hurdle heights can vary.

Custom functions such as `turn_right()` and `jump()` are created to make the code reusable and easier to understand. The robot checks whether there is a wall in front and decides whether to jump or continue moving.

**Concepts:** Custom functions, `while` loops, nested loops, condition checking, code reuse.

### 5. Maze

Solves a maze using conditional logic and repeated movement.

The robot checks whether the right side or the front is clear and decides which direction to take. A custom `turn_right()` function is also used to simplify the navigation logic.

**Concepts:** `while` loops, `if-elif-else`, custom functions, logical decision-making, problem-solving.

Reeborg's World can be used to run and experiment with these challenges:

**Reeborg's World:** https://reeborg.ca/

---

### 6. Dice Battle

A two-player dice game where each player rolls a die five times. The program:

* Accepts the names of two players.
* Generates five random dice values for each player.
* Stores the rolls in separate lists.
* Calculates the total score for each player.
* Compares the scores and determines the winner.

This exercise combines functions, lists, loops, randomisation, and conditional statements into one program.

**Concepts:** Functions, lists, `random.randint()`, `for` loops, list operations, arithmetic operations, conditional statements.

---

### 7. Password Generator

Creates a random password based on the length specified by the user.

The program ensures that every generated password contains at least:

* One uppercase letter
* One lowercase letter
* One digit
* One special character

The remaining characters are generated randomly, after which all characters are shuffled before creating the final password.

The program also validates the minimum password length and displays an appropriate message if the requested length is less than 4.

**Concepts:** Functions, string module, randomisation, lists, list concatenation, `random.choice()`, `random.shuffle()`, string manipulation, input validation.

## Concepts Covered

* Defining and calling functions using `def`
* Function parameters and return values
* `for` and `while` loops
* Nested loops
* `if`, `elif`, and `else`
* Lists and list operations
* Randomisation using the `random` module
* Working with Python's `string` module
* `random.choice()` and `random.shuffle()`
* Modulo operator for divisibility checks
* `break` and `return`
* String manipulation and `join()`
* User input and type conversion
* Code reuse through custom functions
* Logical problem-solving


