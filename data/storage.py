from .eqbase import Eqbase
from sqlalchemy.orm import reconstructor


class Nomenclature(Eqbase):
    @property
    def attr(self):
        at = self.__dict__
        try:
            del at['_sa_instance_state']
        except KeyError:
            return at
        return at

class Node(Eqbase):
    pass
