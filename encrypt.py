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
    
    
    def getApiWeather(self):
        return self.apiWeather
    
    def getApiLocation(self):
        return self.apiLocation
    
    def getPassword(self):
        return self.password
    
    def getSalt(self):
        return self.salt
    
    def getNonce(self):
        return self.nonce
    
    def getRand(self):
        return self.rand
    
    def getWeather(self):
        return self.weather
    
    def getLocation(self):
        return self.location
    
    def setApiWeather(self, apiWeather):
        self.apiWeather = apiWeather
    
    def setApiLocation(self, apiLocation):
        self.apiLocation = apiLocation
    
    def setPassword(self, password):
        self.password = password

    def setSalt(self, salt):
        self.salt = salt
    
    def setNonce(self, nonce):
        self.nonce = nonce
        
    def setRand(self, rand):  
        self.rand = rand
    
    def setWeather(self, weather):
        self.weather = weather
        
    def setLocation(self, location):
        self.location = location
        
    
    def encrypt(Pass, salt, nonce, weather, rand, ip):
        #the random number is generated  by Random.org API and if not possible by the random module
        passToHash = salt + Pass + nonce + weather + rand + ip
        return passToHash
                                    
        