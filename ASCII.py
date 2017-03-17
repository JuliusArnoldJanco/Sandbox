finished = False

result = 0

while not finished:

    try:

        user = int(input(">"))
        print("Valid result is:", user)
        break
        pass

    except:
        print("Please enter a valid integer.")

