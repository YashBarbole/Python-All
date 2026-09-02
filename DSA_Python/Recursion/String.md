# Python Strings for DSA

This guide explains Python strings, the methods most useful in DSA questions, and common transformations.

## 1. Strings Basics

A string is an ordered sequence of characters inside quotes.

```python
text = "Python"
empty = ""
```

Strings are **immutable**: a character cannot be changed in place. Create a new string instead.

```python
word = "cat"
# word[0] = "b"  # Error: strings are immutable
word = "bat"
```

## 2. Indexing and Slicing

Indexing starts at `0`; negative indices count from the end.

```python
text = "python"

print(text[0])   # p, first character
print(text[-1])  # n, last character
print(text[1:4]) # yth; index 4 is excluded
print(text[:3])  # pyt; start defaults to 0
print(text[3:])  # hon; stop defaults to the end
print(text[::2]) # pto; take every second character
print(text[::-1]) # nohtyp; reverse the string
```

Syntax: `text[start:stop:step]`. The start is included and the stop is excluded.

## 3. Length, Membership, and Loops

```python
text = "banana"

print(len(text))         # 6
print("ana" in text)    # True: substring exists
print("z" not in text)  # True

for char in text:
    print(char)          # One character at a time

for index, char in enumerate(text):
    print(index, char)   # Index and character together
```

## 4. Compare Strings

`==` compares contents and is case-sensitive. For case-insensitive checks, normalize both strings with `casefold()`.

```python
print("Cat" == "cat")  # False
print("Cat".casefold() == "cat".casefold())  # True
```

## 5. Important String Methods

String methods do not modify the original string. They return a new value.

### Case Methods

```python
text = "PyThOn dSa"

print(text.lower())      # python dsa
print(text.upper())      # PYTHON DSA
print(text.capitalize()) # Python dsa
print(text.title())      # Python Dsa
print(text.swapcase())   # pYtHoN DsA
print(text.casefold())   # python dsa; best for comparisons
```

### Remove Characters at Both Ends

`strip()` removes only beginning and ending characters, never characters in the middle.

```python
text = "  hello  "
print(text.strip())   # hello
print(text.lstrip())  # hello__ (left spaces removed)
print(text.rstrip())  # __hello (right spaces removed)

path = "///home/user///"
print(path.strip("/"))  # home/user
```

### Search and Count

```python
text = "banana"

print(text.count("a"))       # 3
print(text.find("na"))       # 2; -1 if missing
print(text.rfind("na"))      # 4; last matching index
print(text.index("na"))      # 2; raises ValueError if missing
print(text.startswith("ban")) # True
print(text.endswith("ana"))   # True
```

Prefer `find()` when a substring may be absent. Use `index()` when absence should be treated as an error.

### Replace

```python
text = "I like Java"
print(text.replace("Java", "Python"))  # I like Python
print("aaaa".replace("a", "b", 2))    # bbaa; only two replacements
```

### Split and Join

`split()` changes a string into a list. `join()` combines strings from an iterable.

```python
sentence = "learn python for dsa"
words = sentence.split()
print(words)  # ['learn', 'python', 'for', 'dsa']

colors = "red,green,blue".split(",")
print(colors)           # ['red', 'green', 'blue']
print("-".join(colors)) # red-green-blue
```

For repeated construction, append to a list and join once. It is normally more efficient than repeatedly using `+` in a loop.

```python
result = []
for char in "hello":
    result.append(char.upper())

print("".join(result))  # HELLO
```

### Character Checks

```python
print("abc".isalpha())    # True: letters only
print("123".isdigit())    # True: digits only
print("abc123".isalnum()) # True: letters and/or digits only
print(" \t".isspace())    # True: whitespace only
print("hello".islower())  # True
print("HELLO".isupper())  # True
```

For strictly ASCII digits in a DSA problem, use `"0" <= char <= "9"`.

## 6. `ord()` and `chr()`

`ord()` converts one character to its Unicode number. `chr()` does the reverse.

```python
print(ord("A"))  # 65
print(ord("a"))  # 97
print(chr(65))    # A
```

This makes a fast frequency array for lowercase English letters.

```python
text = "banana"
frequency = [0] * 26

for char in text:
    frequency[ord(char) - ord("a")] += 1

print(frequency[0])  # 3: count of 'a'
```

## 7. Core DSA Transformations

### Reverse a String

```python
text = "hello"
print(text[::-1])              # olleh
print("".join(reversed(text))) # olleh
```

### Palindrome Check: Two Pointers

A palindrome reads identically from left to right and right to left.

```python
def is_palindrome(text):
    left = 0
    right = len(text) - 1

    while left < right:
        if text[left] != text[right]:
            return False
        left += 1
        right -= 1

    return True


print(is_palindrome("madam"))  # True
```

To ignore spaces, punctuation, and case:

```python
def is_clean_palindrome(text):
    cleaned = "".join(char.casefold() for char in text if char.isalnum())
    return cleaned == cleaned[::-1]


print(is_clean_palindrome("A man, a plan, a canal: Panama"))  # True
```

### Frequency Map

Use a dictionary when character types are not limited to `a` through `z`.

```python
text = "banana"
frequency = {}

for char in text:
    frequency[char] = frequency.get(char, 0) + 1

print(frequency)  # {'b': 1, 'a': 3, 'n': 2}
```

`Counter` is a concise alternative.

```python
from collections import Counter

frequency = Counter("banana")
print(frequency["a"])  # 3
```

### Anagram Check

Anagrams have the same characters with the same frequencies.

```python
def are_anagrams(first, second):
    return sorted(first) == sorted(second)


print(are_anagrams("listen", "silent"))  # True
```

For an anagram check that ignores punctuation, spaces, and case:

```python
def normalize(text):
    return "".join(char.casefold() for char in text if char.isalnum())


def are_clean_anagrams(first, second):
    return sorted(normalize(first)) == sorted(normalize(second))
```

### Remove Duplicate Characters, Keeping Order

```python
def remove_duplicates(text):
    seen = set()
    result = []

    for char in text:
        if char not in seen:
            seen.add(char)
            result.append(char)

    return "".join(result)


print(remove_duplicates("programming"))  # progamin
```

### Remove Whitespace

```python
text = "data structures and algorithms"
print(text.replace(" ", ""))  # Removes ordinary spaces
print("".join(text.split()))   # Removes all whitespace, including tabs/newlines
```

### Toggle Case Manually

```python
def toggle_case(text):
    result = []

    for char in text:
        if "a" <= char <= "z":
            result.append(char.upper())
        elif "A" <= char <= "Z":
            result.append(char.lower())
        else:
            result.append(char)

    return "".join(result)
```

### Rotate a String

A left rotation by `k` shifts the first `k` characters to the end.

```python
def left_rotate(text, k):
    if not text:
        return text

    k %= len(text)  # Handles k larger than the length.
    return text[k:] + text[:k]


print(left_rotate("abcdef", 2))  # cdefab
```

```python
def right_rotate(text, k):
    if not text:
        return text

    k %= len(text)
    return text[-k:] + text[:-k] if k else text
```

### Check Whether a String Is a Rotation

```python
def is_rotation(first, second):
    # A rotation must appear inside two consecutive copies of first.
    return len(first) == len(second) and second in (first + first)


print(is_rotation("abcd", "cdab"))  # True
```

### Reverse Words

```python
sentence = "I love solving DSA"
print(" ".join(sentence.split()[::-1]))  # DSA solving love I
```

`split()` without an argument handles multiple spaces, tabs, and newlines.

### Convert Between String and Number

```python
number = int("12345")
decimal = float("3.14")
text = str(12345)
```

Manual digit conversion helps explain digit-processing problems:

```python
def string_to_integer(text):
    number = 0

    for char in text:
        number = number * 10 + ord(char) - ord("0")

    return number
```

## 8. Two-Pointer Example: Reverse Vowels

Convert to a list when individual characters must be swapped, because lists are mutable.

```python
def reverse_vowels(text):
    characters = list(text)
    vowels = set("aeiouAEIOU")
    left = 0
    right = len(characters) - 1

    while left < right:
        while left < right and characters[left] not in vowels:
            left += 1
        while left < right and characters[right] not in vowels:
            right -= 1

        characters[left], characters[right] = characters[right], characters[left]
        left += 1
        right -= 1

    return "".join(characters)


print(reverse_vowels("hello"))  # holle
```

## 9. Sliding Window: Longest Unique Substring

Use a sliding window for substring questions with a changing condition.

```python
def longest_unique_substring_length(text):
    last_seen = {}
    left = 0
    longest = 0

    for right, char in enumerate(text):
        # Move left beyond the character's previous location.
        if char in last_seen and last_seen[char] >= left:
            left = last_seen[char] + 1

        last_seen[char] = right
        longest = max(longest, right - left + 1)

    return longest


print(longest_unique_substring_length("abcabcbb"))  # 3
```

## 10. Useful Built-ins

```python
text = "dbca"

print(sorted(text))           # ['a', 'b', 'c', 'd']
print("".join(sorted(text))) # abcd
print(min(text))              # a
print(max(text))              # d
print(list(text))             # ['d', 'b', 'c', 'a']
```

## 11. Complexity Cheat Sheet

Let $n$ be the string length and $m$ the searched substring length.

| Operation | Complexity | Note |
| --- | --- | --- |
| `len(text)` | $O(1)$ | Length is stored. |
| `text[index]` | $O(1)$ | Direct access. |
| `text[start:stop]` | $O(n)$ | Makes a new string. |
| `text[::-1]` | $O(n)$ | Makes a reversed string. |
| `char in text` | $O(n)$ | Searches the text. |
| `text.count(char)` | $O(n)$ | Scans the text. |
| `sorted(text)` | $O(n \log n)$ | Common anagram solution. |
| `"".join(parts)` | $O(n)$ | Efficient final construction. |

## 12. DSA Checklist

1. Compare both ends: use **two pointers**.
2. Count characters: use a **dictionary**, `Counter`, or a 26-element array.
3. Find a substring under conditions: consider a **sliding window**.
4. Change individual characters: use `list(text)`, then `"".join(...)`.
5. Ignore case or punctuation: **normalize** the input first.
6. Build output in a loop: append to a list and join once.