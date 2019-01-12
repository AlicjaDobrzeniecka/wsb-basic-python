
# Write a program where string given by the user is encrypted using Caesar cipher and displayed to the user.


def encrypt():
    text = input('Enter plain text message: ')
    cipher = ''
    for each in text:
        c = (ord(each) + 3) % 126
        if c < 32:
            c += 31
        cipher += chr(c)
    print("Your encrypted message is:" + cipher)


encrypt()