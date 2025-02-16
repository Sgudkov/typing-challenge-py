from typing import TypeVar, List

T = TypeVar("T", int, str)


def add(a: T, b: T) -> T:
    ...


## End of your code ##
from typing import assert_type

assert_type(add(1, 2), int)
assert_type(add("1", "2"), str)

add(["1"], ["2"])  # expect-type-error
add("1", 2)  # expect-type-error
