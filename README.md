# markov-text-gen
Python project featuring a custom Date class for calendar calculations and a Markov text generator that builds word transition dictionaries from file input to produce randomized text.

A two-part Python project combining a calendar date manipulation class with a Markov chain text generator that uses date-aware sentence structuring.

---

## Project Structure

| File | Responsibility |
|---|---|
| `dates.py` | `Date` class — calendar date representation and arithmetic |
| `create-dict.py` | Markov chain model — learns and generates text from any source file |

---

## Part 1 — Date Class (`dates.py`)

A class for storing and manipulating calendar dates, with support for comparison, arithmetic, leap year detection, and day-of-week lookup.

### Usage

```python
from dates import Date

# Create a date
d = Date(3, 17, 2026)
print(d)                        # 03/17/2026

# Leap year check
Date(2, 1, 2024).is_leap_year()    # True
Date(2, 1, 2025).is_leap_year()    # False

# Days in a given month
Date(2, 1, 2024).days_in_month()   # 29 (leap year February)
Date(2, 1, 2025).days_in_month()   # 28

# Compare two dates
d1 = Date(1, 1, 2020)
d2 = Date(6, 15, 2021)
d1.is_before(d2)     # True
d1.is_after(d2)      # False
d1 == d2             # False

# Count days between two dates
d1.days_between(d2)  # positive = d2 is after d1, negative = d2 is before d1

# Advance a date by one day (modifies in place)
d = Date(12, 31, 2025)
d.advance_one()
print(d)             # 01/01/2026

# Day of the week
Date(3, 17, 2026).day_name()    # 'Tuesday'
```

### Methods

| Method | Description |
|---|---|
| `__repr__()` | Returns date as `MM/DD/YYYY` string |
| `is_leap_year()` | Returns `True` if the year is a leap year |
| `days_in_month()` | Returns the number of days in the date's month |
| `copy()` | Returns a new `Date` object with the same values |
| `advance_one()` | Moves the date forward by one day (in place) |
| `__eq__(other)` | Returns `True` if both dates are the same |
| `is_before(other)` | Returns `True` if this date comes before `other` |
| `is_after(other)` | Returns `True` if this date comes after `other` |
| `days_between(other)` | Returns the signed number of days between two dates |
| `day_name()` | Returns the day of the week as a string |

### Leap Year Logic

Follows the Gregorian calendar rules:
- Divisible by **400** → leap year ✅
- Divisible by **100** (but not 400) → not a leap year ❌
- Divisible by **4** (but not 100) → leap year ✅
- Otherwise → not a leap year ❌

---

## Part 2 — Markov Chain Text Generator (`create-dict.py`)

Learns the word-transition patterns of any source text and generates new sentences that statistically mimic its style and vocabulary.

### How It Works

**Step 1 — Build the dictionary** (`create_dictionary`)

Reads the source text and builds a transition map where each word points to a list of words that followed it in the original:

```python
{
    '$':    ['It', 'The', 'Once', ...],   # $ = sentence start marker
    'It':   ['was', 'is', 'seemed', ...],
    'was':  ['a', 'the', 'never', ...],
    ...
}
```

`$` is a special key representing the beginning of a sentence — it resets whenever a word ending in `.`, `!`, or `?` is encountered.

**Step 2 — Generate text** (`generate_text`)

Starts at `$` and randomly walks the transition map, printing each chosen word until the requested word count is reached.

### Usage

```python
from create_dict import create_dictionary, generate_text

# Build the model from any plain text file
word_dict = create_dictionary('source.txt')

# Generate 100 words of new text
generate_text(word_dict, 100)
```

**Example output** (trained on a novel):
```
The old man walked slowly toward the river. He had not seen the village
in many years. A cold wind came from the north and the trees bent low...
```

---

## Requirements

- Python 3.x
- A plain `.txt` file for the text generator
- No external libraries required (`random` is from the standard library)

---

## Limitations

- `days_between()` works by looping `advance_one()` day by day — correct but slow for dates far apart; a direct arithmetic approach would be significantly faster
- `day_name()` is anchored to a hardcoded reference date (Monday, November 10, 2025)
- No input validation on `Date` — invalid dates like `Date(13, 45, 2025)` won't raise errors but will produce incorrect results
- In `create-dict.py`, punctuation is not stripped from words, so `'hello,'` and `'hello'` are treated as different dictionary keys
