def main():

    MENU = "Score analyzer"
    print(MENU)
    score = float(input("Enter score: "))
    Score_checker(score)



def Score_checker(score):

    if score >= 100 and score >= 0:
        print("Invalid score")
    elif score >= 50:
        print("\nPassable\n")
        return score
    elif score >= 90:
        print("\nExcellent\n")
        return score
    else:
        score < 50
    print("\nBad\n")



main()