import random

def main():
    lower = 0

    upper = 0



    MAX_INCREASE = 0.1  # 10%

    MAX_DECREASE = 0.05  # 5%

    MIN_PRICE = 0.01

    MAX_PRICE = 1000.0

    INITIAL_PRICE = get_numbers(lower, upper)
    counter = 0

    price = INITIAL_PRICE
    print(price)
    print("initial price is: ${:,.2f}".format(price))
    # print("${:,.2f}".format(price))



    while price >= MIN_PRICE and price <= MAX_PRICE:
        counter = counter + 1
        price_change = 0

        # generate a random integer of 1 or 2

        # if it's 1, the price increases, otherwise it decreases

        if random.randint(1, 2) == 1:

            # generate a random floating-point number

            # between 0 and MAX_INCREASE

            price_change = random.uniform(0, MAX_INCREASE)

        else:

            # generate a random floating-point number

            # between negative MAX_INCREASE and 0

            price_change = random.uniform(-MAX_DECREASE, 0)

        price *= (1 + price_change)

        print("The price on {:,.0f} is ${:,.2f}".format(counter, price))
        continue
def get_numbers(lower, upper):
    w = 1
    while w !=0:
        try:
            user = int(input("Enter number (10-50):"))

        except ValueError:
            print("Please enter a valid number")
            continue
        else:
            if user >= 51:
                print("Please enter a valid number")
                continue
            elif user is '':
                print("Please enter a valid number")
                continue
            elif user <= 10:
                print("Please enter a valid number")
                continue

            elif user <= 30:
                lower = user
                return lower
            else:
                upper = user
                return upper
            break


main()