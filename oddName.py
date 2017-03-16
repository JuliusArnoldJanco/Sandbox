""""Julius Arnold-Janco"""

userinput = input(">>")
try:
    if ' ' in userinput:
        print('Please Enter Name:')

    elif '  ' in userinput:
        print("Only one space please")

    elif userinput is '':
        print("Something has to be put in porkchop")

    else:
        count = 2
        for each in list(userinput):
            if count % 2 != 0:
                print(each)
                count+=1
            else:
                count+=1
except SyntaxError:
    userinput = None
    print("must enter something")




