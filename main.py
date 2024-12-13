

from apiRand import apiRandResponse
from classPatito import Patito
from toHash import Encrypt


def main():
    rand = apiRandResponse()
    salt = Encrypt.getSalt()
    nonce = Encrypt.getNonce()
    StringToHash = "pichaMamaUsted"
    
    #print(f'Randon: {rand} Salt: {salt} Nonce: {nonce}')
    
    result = Encrypt.encrypt(StringToHash, salt, nonce, rand)
    
    print (f'With this rand: {rand} with this salt: {salt} with this nonce: {nonce} the result is: {result}')
    
   #print(Patito.whoAmI())
   
    pass


if __name__ == "__main__":
    main()
