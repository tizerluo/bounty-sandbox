# IssueBountyEscrow public evidence sandbox

Small merged pull requests for the GenLayer IssueBountyEscrow complete/partial acceptance smoke tests. No credentials or real funds. See tizerluo/genlayer-issue-bounty.

## Integer addition

Use `addition.add` to return the sum of two integers:

```python
from addition import add
assert add(2, 3) == 5
assert add(-2, 3) == 1
```

## `bounty_math.add(a, b)`

`add(a, b)` returns the sum of two integers and raises `TypeError` for any other input type.

```python
from bounty_math import add
assert add(2, 3) == 5
assert add(-4, 1) == -3
```

## `bounty_math.subtract(a, b)`

`subtract(a, b)` returns the difference `a - b` of two integers and raises `TypeError` for any other input type (including `bool`).

```python
from bounty_math import subtract
assert subtract(5, 3) == 2
assert subtract(-4, 1) == -5
```

Run the tests with `python -m pytest tests/`.
