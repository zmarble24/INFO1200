# !/bin/usr/env python3
import math

def main():
    print("Welcome to Zach's \
    Circle Circumference Calculator")
    PI = math.pi
    TWO = 2

    userInput = input("Radius (x to exit): ")
    while userInput.lower() != 'x':
        radius = float(userInput)
        circumference = (TWO * PI * radius)
        print(f'Circumference = {round(circumference, 2)}')
        print()
        userInput = input("Radius (x to exit): ")
        
    print()
    print('Goodbye!')

if __name__ == "__main__" :  main()
12