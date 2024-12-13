from argon2.low_level import hash_secret, Type
import os
import random



class Encrypt:
    def __init__(
        self,
        password,
        salt,
        nonce,
        rand,
    ):
        self.password = password
        self.salt = salt
        self.nonce = nonce
        self.rand = rand

    def getSalt():
        rand = os.urandom(16)
        rand2 = os.urandom(2)
        sum = int.from_bytes(rand2, byteorder="big")
        random = int.from_bytes(rand, byteorder="big")

        return random + sum

    def getNonce():
        rand = os.urandom(16)
        random = int.from_bytes(rand, byteorder="big")
        rand2 = os.urandom(2)
        sum = int.from_bytes(rand2, byteorder="big")
        return random + sum
    
    def randomString():
       pool ="abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890!@#$%^&*()_+"
       result = ""
       for i in range(0,20):
           rand = random.randint(1, len(pool))
           result += pool[rand-1]             
           pass
       return result

    def encrypt(Pass, salt, nonce, rand, StringHelper):
        
        wordString = Pass + str(salt) + str(nonce)

        # hashing the wordString
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

        hashed = hex(hValue & 0xFFFFFFFFFFFFFFFF)
        # end hashing the wordString
        
        

        # hasing the wordString using argon2 but adding the random number to the string
        StringHelper= hashed.encode('utf-8')
        hashHashed = hash_secret(hashed.encode('utf-8'), StringHelper, time_cost=3, memory_cost=65536, parallelism=4, hash_len=32, type=Type.ID)
        # end hashing the wordString using argon2 but adding the random number to the string

        #return hashed
        return  hex(int.from_bytes(hashHashed, byteorder="big") & 0xFFFFFFFFFFFFFFFFFF)
