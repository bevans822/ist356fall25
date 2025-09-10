
for i in range(5):
    password = input("Enter password: ")
    if password == 'secret':
        print("Access granted")
        break
    else:
        print("Invalid Password")
else:
    print("You are locked out")