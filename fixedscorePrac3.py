def main():

    MENU = "Score analyzer"
    print(MENU)
    score = int(input("Enter score: "))
    pal=Score_checker(score)
    if pal >= 100 and pal >= 0:
        print("Invalid score")
    elif pal >= 50:
        print("Passable")
    elif pal >=90:
        print("Excellent")
    else:
        print("Bad")
    ##print("miffles") -Debug
    ##print(pal)       -Debug

def Score_checker(score):

    if score >= 100 and score >= 0:

        return score

    elif score >= 50:

        return score

    elif score >= 90:

        return score

    else:
        score < 50
    print("\nBad\n")



main()