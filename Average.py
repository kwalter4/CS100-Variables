
def main():
 # The purpose of this code is to allow a user to calculate the average of any three numbers

 # Explain the program to the user
 print("This program will take the average of three numbers.")

 # Prompt user to enter three numbers
 first = input("Please enter the first number: ")
 second = input("Please enter the second number: ")
 third = input("Please enter the third number: ")

 # Covert input to integers
 first = float(first)
 second = float(second)
 third = float(third)

 # Get the mean average
 mean = (first + second + third) / 3

 # Output the mean average
 print(f"The mean average is {mean:.3f}")

pass

if __name__ == '__main__':
    main()