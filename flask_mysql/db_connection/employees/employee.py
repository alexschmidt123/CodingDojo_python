from mysqlconnection import connectToMySQL

class Employee:

    def __init__(self,data):
        self.id = data['id']