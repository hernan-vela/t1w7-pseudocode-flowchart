def sum():
    addition = 3 + 4
    return addition

outcome = sum()

print(outcome)

def colors():
    a = 5
    print("Red")
    print("Green")
    print("yellow")
    return a
    print("Blue")
    print("Purple")
    

colors_outcome = colors()
print(colors_outcome)

def colors():
    a = 5
    print("Red")
    print("Green")
    print("yellow")
    print("Blue")
    print("Purple")
    if a > 5:
        return a
    elif a < 5:
        return a-5
    else:
        return 1
    
multiple_returns = colors()
print(multiple_returns)