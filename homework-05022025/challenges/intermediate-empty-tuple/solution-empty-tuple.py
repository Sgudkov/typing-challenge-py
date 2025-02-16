def foo(x: tuple[()]):
    pass


## End of your code ##
foo(())
foo((1,))  # expect-type-error
