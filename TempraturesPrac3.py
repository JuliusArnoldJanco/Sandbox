"""
CP1404/CP5632 - Practical
Pseudocode for temperature conversion
"""

__author__ = 'Julius Arnold-Janco'



"""Code remains unaltered here:"""

MENU = "C - Convert Celsius to Fahrenheit\nF - Convert Fahrenheit to Celsius\nQ (for quit)"
print(MENU)
choice = input(">>> ").upper()

"""FUNCTIONS ARE DEFINED HERE:
    created using right click >> refractor >> extract >> method"""

def Celcius_function(value):
    global celsius, fahrenheit

    celsius = int(input("Celsius: "))
    fahrenheit = celsius * 9.0 / 5 + 32
    value = fahrenheit
    return value



def fahrenheit_function(value):
    global fahrenheit, celsius
    #if choice == "F":
    fahrenheit = int(input("Fahrenheit: "))
    celsius = 5 / 9 * (fahrenheit - 32)

    value = celsius

    return value



while choice != "Q":


    """Functions are called here:"""

    value = 0
    if choice == "C":
        Cel=Celcius_function(value)
        print("\nResult: {:.2f} F\n".format(Cel))
    elif choice == "F":
        Farh=fahrenheit_function(value)
        print("\nResult: {:.2f} C (The proper measurement.....)\n".format(Farh))
    else:
        print("Invalid option")

    choice = input(">>> ").upper()
print("Cheers Mate, was fun :).")

"""All versions have been committed and saved to GitHub: /JuliusArnoldJanco/Sandbox
    thank you for your time."""


