class Account:
    #Object oriented programming baby
    def __init__(self, username, password, points):
        self.username = username
        self.password = password
        self.points = points
    
    @property
    def email(self):
        return '{}.{}@email.com'.format(self.username, self.password)
    
    @property
    def accountinfo(self):
        return '{} {}'.format(self.username, self.password)
    
    def __repr__(self):
        return "Employee('{}', '{}', {})".format(self.username,self.password,self.points)