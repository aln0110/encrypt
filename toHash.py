from argon2 import PasswordHasher
import os
class Encrypt:
    def __init__(self, password, salt, nonce, rand,  ):
        self.password = password
        self.salt =salt
        self.nonce = nonce
        self.rand = rand
    
    
    def getSalt():
       rand= os.urandom(16)
       rand2 = os.urandom(2)
       sum = int.from_bytes(rand2, byteorder='big')
       random = int.from_bytes(rand, byteorder='big')
       
       return random  + sum
     
    def getNonce():
       rand = os.urandom(16)
       random = int.from_bytes(rand, byteorder='big') 
       rand2 = os.urandom(2)
       sum = int.from_bytes(rand2, byteorder='big')
       return  random  + sum
    
    def encrypt(Pass,salt, nonce, rand ):
        ph = PasswordHasher()
        wordString = Pass + str(salt) + str(nonce)

        
        #hashing the wordString
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
                
                
        hashed =  hex(hValue & 0xFFFFFFFFFFFFFFFF)      
        #end hashing the wordString
        
        #hasing the wordString using argon2 but adding the random number to the string
        hashHashed = ph.hash(hashed)  
       #end hashing the wordString using argon2 but adding the random number to the string  

         
        return hashHashed