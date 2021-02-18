from sqlalchemy import Column, Integer, ForeignKey, String
from sqlalchemy.orm import synonym, relationship, backref, aliased
from sqlalchemy.orm.collections import attribute_mapped_collection

from data.db import Base


class Node(Base):
    __tablename__ = "tree"

    id = Column(Integer, primary_key=True)
    root_id = Column(Integer, ForeignKey(id, ondelete="CASCADE"))
    name = Column(String, nullable=False)
    ID = synonym("id")
    child = relationship(
        "Node",
        cascade="all, delete-orphan",
        backref=backref("parent", remote_side=id),
        collection_class=attribute_mapped_collection("name"),
    )

    def __init__(self, name, root_id=None):
        self.name = name
        self.root_id = root_id

    def __repr__(self):
        return f"Node({self.name},{self.id},{self.root_id}"

    @classmethod
    def get_pairs(cls, child_id: int = 1) -> list:
        """Returns a node of tree with the following structure: parent_name,
        child_name, child_id
        An default, returns root of the tree."""
        parent, child = aliased(Node), aliased(Node)
        query = (
            cls.query(parent.name, child.name, child.id)
            .join(parent, child.root_id == parent.id)
            .filter(parent.id == child_id)
            .all()
        )
        return query

    @classmethod
    def get_roots(cls: classmethod, parent: int = 1):
        p, c = aliased(Node), aliased(Node)
        query = (
            cls.query(c.name, c.id)
            .join(p, c.root_id == p.id)
            .filter(p.id == parent)
            .all()
        )
        return query

    @classmethod
    def get_tree_name_by_id(cls, name: int) -> str:
        try:
            return (
                cls.query(Node.name)
                .filter(Node.id == str(name))
                .all()[0]
                ._asdict()["_name"]
            )
        except IndexError:
            return ""

    @classmethod
    def get_tree_id_by_name(cls, arg: str) -> int:
        try:
            return cls.query(Node.id).filter(Node.name == arg) \
                                     .all()[0]._asdict()["id"]
        except IndexError:
            return 0

    @classmethod
    def add_node(cls, parent: int, name: str) -> tuple:
        a = Node()
        a.root_id = parent
        a._name = name
        cls.session.add(a)
        cls.session.flush()
        return a.id, a.name

    @classmethod
    def get_tree_child(cls, arg: id) -> dict:
        try:
            query = cls.query(Node.id, Node.name)\
                                      .filter(Node.root_id == str(arg)).all()
            return dict((y, x) for x, y in query)
        except ValueError:
            return {}

    @classmethod
    def tree_no_children(cls, parent: int) -> bool:
        if not cls.query(Node.id).filter(Node.root_id == str(parent)).all():
            return True
        else:
            return False
