SQUAREFEET_PER_ACRE = 43560


def main():
 # The purpose of this program is to convert the amount of given land in square feet to acres
 # There are 43560 square feet in one acre

 # Let the user know the intention of the program
 print("This program calculates the number of acres from square feet.")

 # Prompt the user to enter the square footage of the land
 square_ft = input("Enter the number of square feet: ")

 # Convert inputs to integers
 square_ft = float(square_ft)

 # Convert square feet to acres
 acres = square_ft / 43560

 # Output the acres
 print(f"{square_ft:.1f} square feet is equal to {acres:.4f} acres")

pass


if __name__ == '__main__':
    main()

