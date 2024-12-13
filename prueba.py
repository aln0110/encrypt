from apiRand import apiRandResponse


def prueba(String, salt, nonce, rand):
    wordString = String + str(salt) + str(nonce)
    hValue = 2166136261 + int(rand)
    for i in range(len(wordString)):
        hValue = (hValue << 7) + hValue + ord(wordString[i])

        if hValue % 2 == 0:
            hValue = hValue + 100

        else:
            hValue = hValue + 5

        if hValue % 3 == 0:
            hValue = hValue ^ ord(wordString[i])
            hValue = hValue + 5

        if hValue % 5 == 0:
            hValue = hValue * ord(wordString[i])

    return hex(hValue & 0xFFFFFFFFFFFFFFFFFF)  #  2 extra F


def main():

    for i in range(3):
        rand = apiRandResponse()
        stringResult = prueba("pichaMamaUsted", 1, 47, rand)

        print("********************************************")
        print(f"Hash result: {stringResult}")
        print(f"String size: {len(stringResult)}")
        print("********************************************")


if __name__ == "__main__":
    main()
