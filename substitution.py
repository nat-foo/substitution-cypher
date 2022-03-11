def encrypt():
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    unusedChars = alphabet
    usedChars = ""

    print("Encrypting text...")
    key = input("Enter key: ").upper()
    plainText = input("Enter plain text: ").upper()

    # Validation
    if (len(key) != 26):
        key = key[:26]
        for keyChar in key:
            if (keyChar in usedChars):
                print(f"Key contains duplicate character '{keyChar}'. Please enter a key with no duplicate characters.")
                return False
            for unusedChar in unusedChars:
                if (keyChar == unusedChar):
                    print(f"Removing '{keyChar}'.")
                    # Remove key character from unused characters.
                    unusedChars = unusedChars.replace(keyChar, '')
                    # Add it to used letters.
                    usedChars += keyChar
        # Add remaining unused characters onto end of key.
        key += unusedChars
    
    print(f"Key: {key}")

    # Encryption
    cipherText = ""
    for plainChar in plainText:
        # Get position of plain character in the alphabet.
        pos = alphabet.index(plainChar)
        print(f"Searching for {plainChar} in {alphabet}... {pos}")
        # Find corresponding character in the key at that position.
        plainChar = key[pos]
        cipherText += plainChar

    print("Cipher text: "+cipherText)
    return True

def decrypt():
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    unusedChars = alphabet
    usedChars = ""

    print("Decrypting text...")
    key = input("Enter key: ").upper()
    cipherText = input("Enter cipher text: ").upper()

    # Validation
    if (len(key) != 26):
        key = key[:26]
        for keyChar in key:
            if (keyChar in usedChars):
                print(f"Key contains duplicate character '{keyChar}'. Please enter a key with no duplicate characters.")
                return False
            for unusedChar in unusedChars:
                if (keyChar == unusedChar):
                    print(f"Removing '{keyChar}'.")
                    # Remove key character from unused characters.
                    unusedChars = unusedChars.replace(keyChar, '')
                    # Add it to used letters.
                    usedChars += keyChar
        # Add remaining unused characters onto end of key.
        key += unusedChars
    
    print(f"Key: {key}")

    # Decryption
    plainText = ""
    for cipherChar in cipherText:
        # Get position of cipher character in the key.
        pos = key.index(cipherChar)
        print(f"Searching for {cipherChar} in {key}... {pos}")
        # Find corresponding character in the alphabet at that position.
        plainChar = alphabet[pos]
        plainText += plainChar

    print(f"Plain text: {plainText}")
    return True

def main():
    success = encrypt()
    if (not success):
        return
    success = decrypt()
    if (not success):
        return

if __name__ == "__main__":
    main()