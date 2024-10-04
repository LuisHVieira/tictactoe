class Player:
    
    p1 = None
    p2 = None

    @classmethod
    def set_players(cls, p1, p2):
        cls.p1 = p1
        cls.p2 = p2

    @classmethod
    def get_players(cls):
        return cls.p1, cls.p2