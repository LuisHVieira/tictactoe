class Player:

    # status = 0
    
    def __init__(self, id, name):
        self.id = id
        self.name = name


# TESTE
p = Player(1, "name")
print(p.name, p.id)