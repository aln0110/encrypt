import requests


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
        urlR = "https://api.random.org/json-rpc/4/invoke"

        headers = {"Content-Type": "application/json"}

        payload = {
            "jsonrpc": "2.0",
            "method": "generateIntegers",
            "params": {
                "apiKey": "7406367f-407d-44a6-91b1-a9daf911be6b",
                "n": 1,
                "min": -115251252,
                "max": 925245125,
                "replacement": True,
            },
            "id": 42,
        }
        rand = requests.post(urlR, json=payload, headers=headers)
        rand = rand.json()["result"]["random"]["data"][0]
        stringResult = prueba("pichaMamaUsted", 1, 47, rand)

        print("********************************************")
        print(f"Hash result: {stringResult}")
        print(f"String size: {len(stringResult)}")
        print("********************************************")


if __name__ == "__main__":
    main()
