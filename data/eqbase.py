from sqlalchemy.ext.declarative import declarative_base

class Eqbase:
    ID = None

    def __repr__(self):
        return str(self.__dict__)

    def __eq__(self, other):
        return type(self) == type(other) and self.ID == other.ID

    def __ne__(self, other):
        return type(self) != type(other) and self.ID != other.ID

    def __hash__(self):
        return id(type(self)) + self.ID