
import typing

T = typing.TypeVar("T")

class Foo:
    def return_self(self: T) -> T:
        ...


## End of your code ##
class SubclassOfFoo(Foo):
    pass


f: Foo = Foo().return_self()
sf: SubclassOfFoo = SubclassOfFoo().return_self()

sf: SubclassOfFoo = Foo().return_self()  # expect-type-error
