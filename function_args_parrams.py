# # Greeting someone
# def greet():
#     print("Hello Coder, Max!!")

# greet()

# def greet():
#     print("Hello Coder, Fury!!")

# greet()

# # generalised coding
# def greet(name): # <---- parameter
#     print(f"Hello Coder, {name}")



# greet("Aamod")

def greetings(fname, lname):
    print(f"Hello Coder, {fname} {lname}")

greetings("Max", "Fury")

def subtract(a, b=1):
    difference = a - b
    return difference

result = subtract(b=3, a=4)

print(result)