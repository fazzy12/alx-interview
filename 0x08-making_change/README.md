# 0x08. Making Change
This project is part of the ALX Africa Software Engineering Curriculum. It focuses on implementing an algorithm in Python to determine the fewest number of coins needed to meet a given amount total.

## Requirements

- Allowed editors: `vi`, `vim`, `emacs`
- All your files will be   `interpreted/compiled` on `Ubuntu 14.04 LTS using python3 (version 3.4.3)`
- All your files should end with a new line
- The first line of all your files should be exactly `#!/usr/bin/python3`
- A `README.md` file, at the root of the folder of the project, is mandatory
- Your code should use the `PEP 8` style `(version 1.7.x)`
- All your files must be executable

### Tasks
#### 0. Change comes from within
Given a pile of coins of different values, the task is to determine the fewest number of coins needed to meet a given amount total.

- Prototype: `def makeChange(coins, total)`
- Return: fewest number of `coins` needed to meet the `total`
- `If` the `total` is `0` or `less`, `return 0`
- `If` the `total` cannot be met by any number of `coins` you have, `return -1`
- `coins` is a list of the values of the `coins` in your possession
- The value of a `coin` will always be an integer greater than `0`
- You can assume you have an infinite number of each denomination of `coin` in the list

### Example usage:

```
makeChange([1, 2, 25], 37)  # Output: 7

makeChange([1256, 54, 48, 16, 102], 1453)  # Output: -1
```

Please refer to the [0-making_change.py]() file for the implementation.

### Repository

- GitHub repository: [alx-interview](https://github.com/fazzy12/alx-interview/tree/main)
- Directory: [0x08-making_change](https://github.com/fazzy12/alx-interview/tree/main/0x08-making_change)
- [File: 0-making_change.py](https://github.com/fazzy12/alx-interview/blob/main/0x08-making_change/0-making_change.py)

This project is part of the ALX Africa Software Engineering Curriculum