#!usr/bin/python
print("Kon Bnega Krodpati Mai Apka Swagat Hai\n")

question1 = "WHAT IS CAPITAL OF INDIA?"
options1 = "a. PUNJAB\nb. MUMBAI\nc. DELHI\nd. MANALI\n"
print(question1)
print(options1)

while True:
    response = input("Enter Your Answer\n")
    if response == "c":
        break
    else:
        print("Galat Jwaab.")

        while True:
            response = input("Enter Your Answer\n")

            if response == "c":
                stop = True
                break
            else:
                print("Incorrect!!! You ran out of your attempts")
                stop = True
                break
        if stop:
            break
