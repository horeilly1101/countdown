# countdown

> Console-based implementation of the Countdown numbers game.

Countdown is a popular game show in the UK. This is my take on it.

## Rules

You will be given 6 numbers and a goal number.

Your task: Use the 6 numbers to get as close to the
goal number as possible.

You may add, subtract, multiply, and divide the given numbers, 
but the result MUST be an integer. You don't have to use all
of the numbers, but you can't use any numbers that haven't
been given. The order of the numbers in your answer does not 
matter.

Give your solution as an algebraic expression (e.g. 5 * 6 + 9).
You may use parentheses. 

### Example 1

    Your cards are [3, 7, 6, 6, 11, 2].
    Your goal is 68.
    Your answer: 6 * 11 + 2
    
### Example 2

    Your cards are [4, 10, 2, 5, 13, 5].
    Your goal is 125.
    Your answer: 5 * 5 * (10/2)

## How to Run

You will need at least *Python 3.6.5* installed on your machine. 
Set up the environment and install dependencies.

```
# start in the repository directory
python3 -m venv venv
. venv/bin/activate
pip install -r requirements.txt
```

Then, you can play the game with:

```
python3 play_game.py
```

## Implementation Details

### Expression

An `Expression` models a mathematical expression, like 5 + 2. There are
several different types of expressions. Most of the implementing
classes represent operations (e.g. addition, multiplication), and these
classes are built up recursively out of other Expressions. There is also
a `Number` implementing class that represents the base case in most of the 
`Expression` methods. A number is pretty much a wrapper around an int.

### Random Expression Generator

The `RandomExpressionGenerator` takes a list of numbers and (randomly)
constructs an `Expression` from them. This is how the goal is computed
in each round of the game.

### Parser

The `Parser` is used to parse input strings (e.g. `"5+(12/4)"`) into
corresponding instances of our Expression classes. For example, it
might parse the string above into 
`Add(Number(5), Divide(Number(12), Number(3)))`.

### Deck

The `Deck` keeps track of the cards left in the game, and is responsible
for picking cards from the deck, uniformly at random. In the context of
this game, a card is simply an integer between 1 and 13.

### Countdown Game

The `CountdownGame` keeps track of the game's state between rounds
and interacts with the player. It also aggregates all of the other
classes together and is in charge of the game's functionality.

## External Libraries

I used Lark to create my Expression parser. Lark is fantastic—I just
had to specify a grammar and a transformer, and it did all of the
parsing work for me. I chose Lark because of its simplicity and
documentation.

You can find it's documentation [here](https://github.com/lark-parser/lark), 
and an example 
[here](https://github.com/lark-parser/lark/blob/master/docs/json_tutorial.md). 
To create the Expression, I drew heavily on a grammar that I put together 
for a project called [deriv](https://github.com/horeilly1101/deriv).

## Testing

Tests were set up with the unittest python module. You can run them with:

```
# start in the repository directory
python3 -m unittest
```
