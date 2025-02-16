def foo(**kwargs: int | str):
    ...


foo(a=1, b="2")
foo(a=[1])  # expect-type-error
