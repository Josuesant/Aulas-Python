
class SGBDs: 
    def __init__(self, SGBDs, SGBDs_desc):
        self.id_SGBDs = 0
        self.SGBDs = SGBDs
        self.SGBDs_desc = SGBDs_desc

    def __str__(self):
        return f'{self.id_SGBDs};{self.SGBDs};{self.SGBDs_desc}'