alphabets = "abcdefghijklmnopqrstuvwxyz"
key = "deceptive"


def getIndex(character):
    for index, char in enumerate(alphabets):
        if(char == character):
            return index


def encryptText(plainText):
    plainCount = 0
    keyCount = 0
    cipherText = [""]
    while(True):
        plainIndex = getIndex(plainText[plainCount])
        keyIndex = getIndex(key[keyCount])
        cipherIndex = plainIndex + keyIndex
        if(cipherIndex >= 26):
            cipherIndex = (plainIndex + keyIndex) % 26
        cipherText.append(alphabets[cipherIndex])
        if(keyCount == key.__len__()-1):
            keyCount = 0
        else:
            keyCount += 1

        if(plainCount == plainText.__len__()-1):
            return cipherText
        else:
            plainCount += 1


def decryptText(cipherText):
    cipherCount = 0
    keyCount = 0
    plainText = [""]
    while(True):
        cipherIndex = getIndex(cipherText[cipherCount])
        keyIndex = getIndex(key[keyCount])
        plainIndex = cipherIndex - keyIndex
        if(plainIndex < 0):
            plainIndex = plainIndex + 26
        plainText.append(alphabets[plainIndex])
        if(keyCount == key.__len__()-1):
            keyCount = 0
        else:
            keyCount += 1

        if(cipherCount == cipherText.__len__()-1):
            return plainText
        else:
            cipherCount += 1       


def main():
    # plainText = input("Enter plain text:- ")
    print(encryptText("wearediscoveredsaveyourself"))
    print(decryptText("ZICVTWQNGRZGVTWAVZHCQYGLMGJ".lower()))


if __name__ == "__main__":
    main()
