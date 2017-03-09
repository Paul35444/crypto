LETTERS = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
message = input("Enter your text: ")
key = input("Enter text key to encrypt: ")

def encrypt(message, key):
    translated = []
    keyIndex = 0
    key = key.upper()

    for symbol in message:
        num = LETTERS.find(symbol.upper())
        if num != -1:
            if symbol.upper() in LETTERS:
                num += LETTERS.find(key[keyIndex])

            num %= len(LETTERS)
            if symbol.isupper():
                translated.append(LETTERS[num])
            elif symbol.islower():
                translated.append(LETTERS[num].lower())
            keyIndex += 1
            if keyIndex == len(key):
                keyIndex = 0
        else:
            translated.append(symbol)
    return ''.join(translated)

print (encrypt(message, key))
