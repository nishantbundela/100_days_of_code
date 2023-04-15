import art

def caeser_cipher():
    print(art.logo)
    string = input("Enter the string:")
    shift = int(input("Enter the shift:"))
    def encoder(string, shift):
        cipher = ''
        for char in string:
            if char == ' ':
                cipher = cipher + char
            else:
                cipher = cipher + chr(ord(char) + (shift % 26))
        return cipher
    def decoder(string, shift):
        cipher = ''
        for char in string:
            if char == ' ':
                cipher = cipher + char
            else:
                cipher = cipher + chr(ord(char) - (shift % 26))
        return cipher
    task = input("Enter 'e' for encoding and 'd' for decoding: ")
    if task == 'e':
        cipher = encoder(string, shift)
    elif task == 'd':
        cipher = decoder(string, shift)
    print("The cipher is:", cipher)
    return cipher


caeser_cipher()
