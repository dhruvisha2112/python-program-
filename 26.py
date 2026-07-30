x=10
def show():
    x=5
    print("local x:",x)
def display():
    global x
    x=x+5
    print("modified global x:",x)
show()
display()
print("global x after function call:",x)