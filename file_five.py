names : list[str] = ["ali hamza","azan ali","abdul hadi","M.adil"]
for name in names:
    print(name)
#list tuple
data_base : list[tuple[str,str]] = [("ali hamza","1234"),
                                    ("abdul hadi","5678"),
                                    ("azan ali","90")]
for row in data_base:
    print(row)

#     #apply if statement
    data_base : list[tuple[str,str]] = [("ali hamza","1234"),
                                       ("abdul hadi","5678"),
                                        ("azan ali","90")]
    input_user = input("Enter your user")
    input_password = input("Enter your password")
for row in data_base:
    user,password = row
    if input_user ==user and input_password == password:
     print(user,password)
    # list comprehensive style
    print([i**2 for i in range(0,11)])
    for n in range(1,11):
       print(f"{2} x {n} = {2*n}")