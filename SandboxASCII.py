#def greet(name,msg):
   #"""This function greets to
   #the person with the provided message"""
  # print("Hello",name + ', ' + msg)

#greet("Monica","Good morning!")
w = 1
while w != 0:
    try:
        user = int(input("Enter number (10-50):"))
    except ValueError:
        print("Please enter a valid number")
        continue
    else:
        break
def get_numbers(lower, upper):
    upper = 0
    lower = 0
    lower = user
    upper = user
    if user >= 51:
        print("Please enter a valid number")
    elif user is '':
        print("Please enter a valid number")
    elif user <= 10:
        print("Please enter a valid number")

    elif user <= 30:
        lower = user
        print("L")
        print(lower)
        return lower
    else:
        upper = user
        print("U")
        print(upper)
        return upper



p=get_numbers(user, user)
print("outside loop")
print(p)

