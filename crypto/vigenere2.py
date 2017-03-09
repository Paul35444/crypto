plain = input("Enter your message: ")
key = input("Enter your key word to encrypt the message: ")

a = ord('a')
z = ord('z')
def encrypt(plain, key):
    cypher = ""
    keyindex = 0
    for letter in plain:
        if letter.upper():
            caps = True
        else:
            caps = False
        ascii = ord(letter)
        if ascii >= a and ascii <= z:
            enc = ascii + ord(key[keyindex])
            keyindex = keyindex + 1
            if keyindex >= len(key):
                keyindex = 0
                while enc > z:
                    enc = enc - 26
                cypher = cypher + chr(enc)
            else:
                cypher = cypher + letter
    return cypher

print (encrypt(plain, key))
