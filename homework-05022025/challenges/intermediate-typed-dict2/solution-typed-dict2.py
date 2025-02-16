from typing import TypedDict, NotRequired


class Student(TypedDict):
    name: str
    age: int
    school: NotRequired[str]

a: Student = {"name": "Tom", "age": 15}
a1: Student = {"name": "Tom", "age": 15, "school": "Hogwarts"}
a2: Student = {"name": 1, "age": 15, "school": "Hogwarts"}  # expect-type-error
a3: Student = {(1,): "Tom", "age": 2, "school": "Hogwarts"}  # expect-type-error
a4: Student = {"name": "Tom", "age": "2", "school": "Hogwarts"}  # expect-type-error
a5: Student = {"z": "Tom", "age": 2}  # expect-type-error
assert Student(name="Tom", age=15) == dict(name="Tom", age=15)
assert Student(name="Tom", age=15, school="Hogwarts") == dict(
    name="Tom", age=15, school="Hogwarts"
)