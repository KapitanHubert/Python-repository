import random
import string

password = ""

smallLetters = string.ascii_lowercase
bigLetters = string.ascii_uppercase
numbers = string.digits
specialCharacters = string.punctuation


reset = True
while reset == True:
    passwordLength = int(input("Podaj długość hasła: "))
    passwordNum = 0
    while passwordNum < passwordLength:
            choice = random.randrange(1,5)
            if choice == 1:
                password += random.choice(smallLetters)
            if choice == 2:
                password += random.choice(bigLetters)
            if choice == 3:
                password += random.choice(numbers)
            if choice == 4:
                password += random.choice(specialCharacters)
            passwordNum += 1
            
    reset = False
    while True:
        if smallLetters not in password:
            reset = True
        if bigLetters not in password:
            reset = True
        if numbers not in password:
            reset = True
        if specialCharacters not in password:
            reset = True
        break
    print("Generated password :", password)
    password = ""

    while True:
        new = True
        if new == True:
            newPassword = input("Would you like to generate new password ? (y/n): ")
            new = False
        if newPassword == "y":
            reset = True
            break
        if newPassword == "n":
            print("Goodbye !")
            reset = False
            break
        else: 
            print("I cannot regognnize this answer, please try again !")
            new = True   



