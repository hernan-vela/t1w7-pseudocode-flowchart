def greet():
    print("I love coding!!")

#Once the indentention is aligned with "def" we're out of the function

#Once we typed the name of the function, it will execute all the statements inside the function
greet()

scope_out = "outside"

def test_scope():
    print(scope_out)

test_scope()

def test_scope1():
    scope_in = "Inside"

# print(scope_in)