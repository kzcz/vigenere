from vigenere import vigenere
from re import sub
from sys import argv

"""this brute-force attack only works if the encryption key is a word."""

def hack(cipherText, verbose = False):
    
    # gather valid words from dictionary file
    with open('dictionary.txt', "r") as x:
        words = x.readlines()
        newWords = set(map(lambda x: x.strip().lower(), words))

    # make words lowercase and strip of extra formatting
    best = ""
    best_accuracy = 0
    # use each dictionary word as the key
    for word in newWords:
        result = vigenere(cipherText, word, "decrypt")
        resultWords = result.split()

        # check how many valid words are in the resulting decryption
        counter = sum(map(lambda item: sub(r'[^a-z]+', "", item) in newWords, resultWords))
        accuracy = counter / len(resultWords)

        if verbose: print(f"{word}:{accuracy}")

        # show user potentially valid key
        if accuracy > best_accuracy:
            best = word
            best_accuracy = accuracy
        if accuracy > 0.5: # adjust desired accuracy here
            print("this is a potential result. Type stop to stop, and anything else to continue looking.")
            print(f"{word}: {result}")
            if input("> ").lower() == "stop": break

    return (best,best_accuracy)

# Example usage
if __name__ == "__main__":
    verbose = len(argv) > 1 and argv[1].lower() in ["-v","--verbose"]

    cipherText = "EDIT ME" # the longer the cipher the better
    result = hack(cipherText,verbose)
    print(result)
