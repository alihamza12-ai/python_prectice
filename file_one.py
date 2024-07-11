#python operator
a : int = 8
b : int = 7
print(a+b)
a = 2
print(a+b)
#comparision operator
a : int = 8
b : int = 7
print(a == b)
#is
x : str = "abc" 
z: str = "abc" 
print(id(x),id(z))
print(x is z)
# use of in
names : list[str] = [chr(i) for i in range(65,91)]
print(names)
print("D" in names)
# user input

names: list[str] = ['ali', 'hamza', 'abdul', 'hadi', 'azan', 'ali', 'adil']
uinput = input("Enter your name: ")
print(uinput in names)
# * used
data("ali",2,2.0)
print(*data)
