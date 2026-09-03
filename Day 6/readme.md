# Day 6 – Functions, List Operations and Hangman Game

## Overview

This folder contains my Day 6 Python practice programs focused on **functions, list manipulation, loops, conditional statements, and logical problem-solving**.

The exercises involve creating reusable functions to perform common operations on lists without relying heavily on Python's built-in functions. These programs helped me understand how to manually implement operations such as calculating an average, finding minimum and maximum values, filtering elements, and reversing a list.

The folder also includes a **Hangman game**, which combines several Python concepts such as randomisation, loops, lists, strings, conditional logic, and user interaction into a complete terminal-based game.

---

## Programs

### 1. Calculate the Average of a List

This program calculates the average of all numbers present in a list.

A custom function named `calculate_avg()` iterates through each number in the list using a `for` loop and adds them to calculate the total sum. The average is then calculated by dividing the total by the number of elements in the list.

The final result is rounded to two decimal places and returned from the function.

**Concepts practiced:**

* Functions
* Function parameters
* `for` loops
* List traversal
* Arithmetic operations
* `len()`
* `round()`
* Return statements

---

### 2. Find Numbers Greater Than a Given Value

This program identifies all numbers in a list that are greater than a specified value.

The function accepts two arguments:

* A list of numbers
* A comparison value

It iterates through the list and checks each number using a conditional statement. Numbers greater than the specified value are stored in a new list and returned as the final result.

For example, when the comparison value is `25`, only numbers greater than `25` are included in the output.

**Concepts practiced:**

* Functions with multiple parameters
* List traversal
* Conditional statements
* Creating and modifying lists
* `append()`
* Return values

---

### 3. Find the Difference Between the Largest and Smallest Number

This program finds the largest and smallest values in a list and calculates the difference between them.

Instead of using Python's built-in `max()` and `min()` functions, the program manually identifies these values by:

1. Initializing both the largest and smallest values with the first element of the list.
2. Iterating through each number in the list.
3. Updating the largest value whenever a bigger number is found.
4. Updating the smallest value whenever a smaller number is found.
5. Subtracting the smallest value from the largest value.

This exercise demonstrates the logic behind manually finding minimum and maximum values.

**Concepts practiced:**

* Functions
* List traversal
* Conditional statements
* Variable updates
* Manual implementation of `min()` and `max()` logic
* Arithmetic operations

---

### 4. Find the Minimum Value in a List

This program finds the smallest number in a given list without using the built-in `min()` function.

The first number in the list is initially considered the minimum value. The program then iterates through the remaining values and updates the minimum whenever a smaller number is found.

The final minimum value is returned by the function.

**Concepts practiced:**

* Functions
* List traversal
* Conditional statements
* Comparison operators
* Variable updates
* Return statements

---

### 5. Reverse a List

This program reverses the elements of a list manually.

Instead of using Python's built-in `reverse()` method or slicing, the program uses the `range()` function to iterate through the list from the last index to the first index.

Each element is then added to a new list in reverse order.

For example:

```text
Original List: [10, 20, 30, 40, 50]
Reversed List: [50, 40, 30, 20, 10]
```

**Concepts practiced:**

* Functions
* List indexing
* Reverse traversal
* `range()`
* `len()`
* `append()`
* Creating a new list

---

## Hangman Game

### 6. Terminal-Based Hangman Game

The final program in this folder is a simple terminal-based implementation of the classic **Hangman game**.

The program starts by selecting a random word from a predefined list containing technology-related words, programming terms, and general words.

The player is given **six lives** and must guess the letters in the selected word.

### Game Flow

1. A random word is selected using `random.choice()`.
2. A list of underscores is created to represent the hidden word.
3. The player enters one letter at a time.
4. The program checks every position in the word to see whether the guessed letter is present.
5. If the guessed letter is found, it replaces the corresponding underscore.
6. If the guessed letter is not found, the player loses one life.
7. The game continues until:

   * The player successfully guesses all the letters, or
   * The player runs out of lives.

### Winning the Game

The player wins when all underscores have been replaced with the correct letters.

```text
Congratulations! You guessed the word.
```

### Losing the Game

The game ends when the player has no remaining lives. The correct word is then displayed.

```text
Game Over!
The word was: <random_word>
```

### Concepts Combined in the Hangman Game

The Hangman project brings together several Python concepts practiced in the previous exercises:

* Lists
* Strings
* `for` loops
* `while` loops
* Conditional statements
* User input
* String methods
* `random` module
* `random.choice()`
* List indexing
* Boolean flags
* Game state management

---

## Concepts Covered

Throughout the programs in this folder, the following concepts were practiced:

* Defining and calling functions
* Function parameters and return values
* `for` loops
* `while` loops
* List traversal
* List indexing
* Creating and updating lists
* `append()`
* Conditional statements
* Comparison operators
* Arithmetic operations
* `range()` and `len()`
* `round()`
* Randomisation using the `random` module
* String manipulation
* Boolean variables
* User interaction
* Problem-solving using Python

---
