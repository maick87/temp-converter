import os  # Importing the os module to interact with the operating system

while True:  # Starting an infinite loop to continuously prompt the user

    # Getting user input for a number
    user_input1 = input('type a number = ')
    user_input1_int = int(user_input1)  # Converting the input to an integer

    # Getting user input to choose the conversion type
    user_input2 = input('type 1 to convert Celsius to Fahrenheit and 2 to convert Fahrenheit to Celsius = ')

    # Checking the user's choice and performing the corresponding conversion
    if user_input2 == '1':  # If the user chose to convert Celsius to Fahrenheit
        fahrenheit = (user_input1_int * 9/5) + 32  # Conversion formula
        formatted_temperature1 = "{:.2f}".format(fahrenheit)  # Formatting the result to two decimal places
        print(f'The value in Fahrenheit is {formatted_temperature1} °F')  # Displaying the result

    elif user_input2 == '2':  # If the user chose to convert Fahrenheit to Celsius
        celsius = (user_input1_int - 32) * 5/9  # Conversion formula
        formatted_temperature2 = "{:.2f}".format(celsius)  # Formatting the result to two decimal places
        print(f'The value in Celsius is {formatted_temperature2} °C')  # Displaying the result

    else:  # If the user inputs neither 1 nor 2
        print('Error. Type only 1 or 2')

    # Asking the user whether to continue or exit
    user_input3 = input('type 3 to continue and 4 to exit = ')

    if user_input3 == '3':  # If the user chooses to continue
        os.system('cls')  # Clearing the screen (for Windows, for other OS change 'cls' to 'clear')
        continue  # Continuing to the next iteration of the loop

    elif user_input3 == '4':  # If the user chooses to exit
        os.system('cls')  # Clearing the screen (for Windows, for other OS change 'cls' to 'clear')
        print('thanks for using my code')  # Displaying a thank you message
        break  # Exiting the loop and ending the program



