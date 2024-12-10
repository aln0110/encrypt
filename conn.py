import mysql.connector
from user import User


class dataBase:
    def __init__(self):
         self.host = 'localhost'
         self.user = 'root'
         self.password = ''
         self.database = 'bdencrypt'
         self.con = mysql.connector.connect(host=self.host, user=self.user, password=self.password, database=self.database)
         
     
    
    def insert(self, user_obj):
        cursor = self.con.cursor()
        cursor.execute("INSERT INTO users (user, password, rand, weathe, salt, nonce) VALUES (%s, %s, %s, %s, %s, %s)", (user_obj.getUser(),user_obj.getPassword(), user_obj.getRand(), user_obj.getWeathe(), user_obj.getSalt(), user_obj.getNonce()))
        self.con.commit()
        cursor.close()
        return True
    
    def validate(self, username, password):
        user = User()
        cursor = self.con.cursor()
        cursor.execute("SELECT * FROM users WHERE user = %s", (username,))
        result = cursor.fetchall()
        passToHash  = " "
        
        if len(result) == 0:
            return False
        else:
            user(result[0][1], result[0][2], result[0][3], result[0][4], result[0][5], result[0][6])
            pass
        
        #all the shit show is here to set the  hashed pass word  
        #so i will need a way to make it work from the other ecrypclass 
        
        passToHash = user.getSalt() + password + user.getNonce()  
        
        if user.getPassword() == passToHash:
            return True
        else:
            return False
        
        
        
        
        
            
        
           
                
          
    
