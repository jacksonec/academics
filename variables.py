print('High-Precision Strings Simulator v7.6')

input_string = input("Give me a string (type CANCEL to quit): ")
while input_string != "CANCEL":
    print(f'Formatted string: {input_string}')
    print(r'Raw string (used wrong): {input_string}')
    print(r'Raw string (used right): ' + input_string)
    print('Normal String (basically the same as raw): ' + input_string)
    print('')
    print(f'Windows path (formatted string): c:\\users\\jacks')
    print(r'Windows path (raw string): c:\users\jacks')
    print('Windows path (normal string): c:\\users\\jacks')

    print('')


    input_string = input('Now give me a number (again, type cancel to quit): ')
    print(f"You entered {input_string}")
    try:
        print("Adding 5 to your number")
        input_string = input_string + 5
    except Exception as e:
        print(f'Error {e}! No good.')
        input ("This won't work because the program is trying to add a string and integer together")

    print('')

    print("Here is what we get if we combine the input and 5 if they are both strings: " + input_string + "5")
    # We need to make a copy of the input string, but convert it into an integer
    input_integer = int(input_string)
    # Now we add 5
    input_integer += 5
    print(f"Now we can print it using a formatted string: {input_integer}")
    print(f"We could also do all of that in one statement: {int(input_string) + 5}")

    input_string = input("Give me a string (type CANCEL to quit): ")