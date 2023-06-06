
def main():
 # This program will find the price of five items a customer purchases
 # Including the subtotal, sales tax (7%), and total

 print("This program will calculate the total for 5 items including sales tax.")

 # Prompt the user to input the price of the five items
 one = input("Enter the price of the first item: ")
 two = input("Enter the price of the second item: ")
 three = input("Enter the price of the third item: ")
 four = input("Enter the price of the fourth item: ")
 five = input("Enter the price of the fifth item: ")

 # Convert inputs to integers
 one = float(one)
 two = float(two)
 three = float(three)
 four = float(four)
 five = float(five)

 # Calculate the subtotal
 subtotal = one + two + three + four + five

 # Output the subtotal
 print(f"Subtotal: ${subtotal:.2f}")

 # Calculate the sales tax
 sales_tax = subtotal * 0.07

 # Output the sales tax
 print(f"Sales Tax: ${sales_tax:.2f}")

 # Calculate the total
 total = subtotal + sales_tax

 # Output the total
 print(f"Total: ${total:.2f}")

 pass

if __name__ == '__main__':
    main()

