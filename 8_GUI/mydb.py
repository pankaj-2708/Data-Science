import json

class Database:
    def add_data(self,name,email,password):
        with open('mydb.json','r') as f:

            database=json.load(f)

            if email in database:
                return 0
            
            with open('mydb.json','w') as f:
                database[email]=[name,password]
                json.dump(database,f,indent=4)
                print('Data added successfully')
                return 1
            
    def get_data(self,email):
        with open('mydb.json','r') as f:
            database=json.load(f)
            if email in database:
                return database[email]
            else:
                return None