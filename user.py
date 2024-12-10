class User:
    def __init__(self, user=None, password=None, rand=None, weathe=None, salt=None, nonce=None):
        self.user = user
        self.password = password
        self.rand = rand
        self.weathe = weathe
        self.salt = salt
        self.nonce = nonce
        
    def getUser(self):
        return self.user
    def getPassword(self):
        return self.password
    def getRand(self):
        return self.rand
    def getWeathe(self):
        return self.weathe
    def getSalt(self):
        return self.salt
    def getNonce(self):
        return self.nonce
    
    
    def setUser(self, user):
        self.user = user
    
    def setPassword(self, password):
        self.password = password
    
    def setRand(self, rand):
        self.rand = rand
    
    def setWeathe(self, weathe):
        self.weathe = weathe
    
    def setSalt(self, salt):
        self.salt = salt
    
    def setNonce(self, nonce):
        self.nonce = nonce
    
                                