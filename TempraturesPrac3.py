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
    if choice == "C":
        celsius = int(input("Celsius: "))
        fahrenheit = celsius * 9.0 / 5 + 32
        value = fahrenheit
        return value
        print("\nResult: {:.2f} F\n".format(fahrenheit))


def fahrenheit_function(value):
    global fahrenheit, celsius
    if choice == "F":
        # TODO: Write this section so the program converts F to C and displays the result
        # TODONE
        fahrenheit = int(input("Fahrenheit: "))
        celsius = 5 / 9 * (fahrenheit - 32)
        value = celsius
        return value
    else:
        pass


while choice != "Q":


    """Functions are called here:"""
    value = 0
    Celcius_function(value)
    Cel=Celcius_function(value)
    print("\nResult: {:.2f} F\n".format(Cel))
    fahrenheit_function(value)
    Farh=fahrenheit_function(value)
    print("\nResult: {:.2f} C (The proper measurement.....)\n".format(Farh))

    choice = input(">>> ").upper()
print("Cheers Mate, was fun :).")

"""All versions have been committed and saved to GitHub: /JuliusArnoldJanco/Sandbox
    thank you for your time."""


