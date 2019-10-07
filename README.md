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

Set up the environment and install dependencies.

```
# start in the countdown/ directory
python3 -m venv venv
. venv/bin/activate
pip install -r requirements.txt
```

Then, you can play the game with:

```
python3 play_game.py
```

## Implementation Details

Below, I will detail the key parts of the system I designed and
how they interact.

### Expression

### Rancom Expression Generator

### Parser

### Deck

### Countdown Game

## External Libraries

I used Lark to create my Expression parser. Lark is fantastic—I just
had to specify a grammar and a transformer, and it did all of the
parsing work for me.

You can find it's documentation here, and an example here. To create the
Expression, I drew heavily on a grammar that I put together for a
project called deriv.

## Testing

Tests were set up with the unittest python module. You can run them with:

```
python3 -m unittest
```
