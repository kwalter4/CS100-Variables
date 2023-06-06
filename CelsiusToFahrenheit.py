

def main():
 # The purpose of this program is to convert Celsius temperatures to fahreheit temperatures
 print("This program will convert degrees celsius to fahrenheit.")

 # We will use the formula F = 9/5 * Celsius + 32

 # First, prompt the user to input degrees celsius
 Celsius = input("Please enter the degrees in celsius: ")

 # Convert input to integers
 Celsius = float(Celsius)

 # Convert celsius to fahrenheit
 Fahrenheit = 9/5 * Celsius + 32
 print(f"{Celsius:.1f} degrees celsius is {Fahrenheit:.2f} degrees fahrenheit")

pass

if __name__ == '__main__':
    main()

