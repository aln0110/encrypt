import json
class Encrypt:
    def __init__(self, apiWeather, apiLocation, password, salt, nonce, rand, weather, location, weatherKey):
        self.apiWeather = apiWeather
        self.weatherKey = weatherKey
        self.apiLocation = apiLocation
        self.password = password
        self.salt =salt
        self.nonce = nonce
        self.rand = rand
        self.weather = weather
        self.location = location
    
    
   
    
    def encrypt(Pass,salt, nonce, rand ):
        #the random number is generated  by Random.org API and if not possible by the random module
        dataToHash =  json.dumps({"Pass": Pass, "salt": salt, "nonce": nonce, "rand": rand})
         
        wordString = Pass + str(salt) + str(nonce)
        #hashing the wordString
        hValue = 2166136261
        
        for i in range(len(wordString)):
            hValue =  (hValue << 7) + hValue + ord(wordString[i])
            if (hValue % 2 == 0):
                hValue = hValue  + 2
            else:
                hValue = hValue + 1
            
            if (hValue % 3 == 0):
                hValue =  hValue  ^  ord(wordString[i])
                
                
        hashed =  hex(hValue & 0xFFFFFFFFFFFFFFFF)
        
        
        
        
        
        
        
        #end hashing the wordString
        
        
        #hasing the wordString using argon2 but adding the random number to the string
        hashHashed = " "
        
       #end hashing the wordString using argon2 but adding the random number to the string  
        
        
        
        passToHash = dataToHash 
        return passToHash
                                    
        