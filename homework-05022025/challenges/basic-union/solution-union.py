def foo(x: int | str):
    pass


## End of your code ##
foo("foo")
foo(1)

foo([])  # expect-type-error
