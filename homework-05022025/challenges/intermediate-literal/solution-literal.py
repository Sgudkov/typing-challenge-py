from typing import Literal

Direction = Literal["left", "right"]


def foo(direction: Direction):
    ...


## End of your code ##
foo("left")
foo("right")

a = "".join(["l", "e", "f", "t"])
foo(a)  # expect-type-error
