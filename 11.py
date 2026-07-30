with open("test.txt","w") as f:
    f.write("hello student!")
with open("test.txt","r") as f:
    content= f.read()
    print("file content:",content)