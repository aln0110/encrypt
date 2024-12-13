

from apiRand import apiRandResponse
from classPatito import Patito
from toHash import Encrypt


def main():
    #rand = apiRandResponse()
    #salt = Encrypt.getSalt()
    #nonce = Encrypt.getNonce()
    #StrngHelper = Encrypt.randomString()
    StringToHash = "pichaMamaUsted"
    

    rand= 311025526
    salt= 122670693681576847774163115726612019392
    nonce= 199487788391418891040571943207132884477
    StringHelper= "Qc0Hn4UEWUr0AB@rDLdB"
    
    result = Encrypt.encrypt(StringToHash, salt, nonce, rand, StringHelper)
    
    
    print (f'With this rand: {rand} with this salt: {salt} with this nonce: {nonce} with this String helper: {StringHelper} the result is: {result}  and the size is: {len(result)}')
    
   #print(Patito.whoAmI())
   
    pass


if __name__ == "__main__":
    main()
