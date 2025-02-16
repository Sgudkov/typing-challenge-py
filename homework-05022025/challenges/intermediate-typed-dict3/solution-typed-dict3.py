from typing import TypedDict, Required


class Person(TypedDict, total=False):
    name: Required[str]
    age: int
    gender: str
    address: str
    email: str


## End of your code ##
a: Person = {
    "name": "Capy",
    "age": 1,
    "gender": "Male",
    "address": "earth",
    "email": "capy@bara.com",
}
a1: Person = {"name": "Capy"}
# fmt: off
a2: Person = {"age": 1, "gender": "Male", "address": "", "email": ""}  # expect-type-error
