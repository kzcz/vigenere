ALPHABET = "abcdefghijklmnopqrstuvwxyz"

def main():

    #encryption
    messageOne = "EDIT ME" # edit message here
    keyOne = "EDIT ME" # edit key here

    print("encryption")
    print(vigenere(messageOne, keyOne, "encrypt"))
    print("\n")

    #decryption
    messageTwo = "EDIT ME" # edit message here
    keyTwo = "EDIT ME" # edit key here

    print("decryption")
    print(vigenere(messageTwo, keyTwo, "decrypt"))
    print("\n")

def vigenere(message, key, direction):
    if direction == "encrypt":
        direction = 1
    elif direction == "decrypt":
        direction = -1
    else:
        print("invalid direction")
        return ""

    mlen = len(message)

    # make message and key uppercase for consistency
    message = message.upper()
    key = key.upper()
    
    #adjust key for message length
    key *= int(mlen / len(key) + 1)

    result = [" "]*mlen
    for i in range(mlen):
        # ignore non-letter characters
        if message[i].isalpha():
            # row and column refers to the vigenere square
            row = (ord(message[i])&63) - 1
            column = (ord(key[i])&63) - 1
            column *= -1
            result[i] = chr(ord('a') + (row + column)%26)
        else:
            key = key[:i] + " " + key[i:]
            result[i] = message[i]
    return "".join(result)
    
if __name__ == "__main__":
    main()
