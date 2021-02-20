from sqlalchemy import Column, Integer, ForeignKey, String, desc
from sqlalchemy.orm import synonym, relationship, aliased, RelationshipProperty
from typing import Any, Union

from db import Base
from db.models.node import Node
from service.utils import asdict


class Nomenclature(Base):
    __tablename__ = "nomenclature"

    n_id = Column(Integer, primary_key="True")
    n_brand = Column(Integer, ForeignKey("tree.id"))
    n_article = Column(String)
    n_color = Column(String)
    n_size = Column(String)
    n_barcode = Column(String)
    n_price = Column(String)
    n_item = Column(Integer, ForeignKey("tree.id"))
    n_wb = Column(String)
    ID = synonym("n_id")
    art = synonym("n_wb")

    brand: RelationshipProperty = relationship("Node", foreign_keys=[n_brand])
    item: RelationshipProperty = relationship("Node", foreign_keys=[n_item])

    def __init__(self, n_id: int, n_brand: int, n_article: str,
                 n_color: str, n_size: str, n_barcode: str,
                 n_price: str, n_item: int, n_wb: str) -> None:
        self.n_id = n_id
        self.n_brand = n_brand
        self.n_article = n_article
        self.n_color = n_color
        self.n_size = n_size
        self.n_barcode = n_barcode
        self.n_price = n_price
        self.n_item = n_item
        self.n_wb = n_wb

    def __repr__(self) -> str:
        return f"Nomenclature {str(self.__dict__)}"

    @classmethod
    def get(cls, identity: int = -1, visual: bool = True) -> \
            list[dict[str, Union[str, int]]]:
        n_brand, n_item = aliased(Node), aliased(Node)
        if visual:
            query = (
                cls.query(
                    Nomenclature.n_id,
                    n_brand.name.label("n_brand"),
                    Nomenclature.n_article,
                    Nomenclature.n_color,
                    Nomenclature.n_size,
                    Nomenclature.n_barcode,
                    Nomenclature.n_price,
                    n_item.name.label("n_item"),
                    Nomenclature.n_wb
                )
                .join(n_brand, n_brand.id == Nomenclature.n_brand)
                .join(n_item, n_item.id == Nomenclature.n_item)
            )
        else:
            return cls.query().order_by(desc(Nomenclature.n_id)).all()
        if identity == -1:
            query = query.order_by(desc(Nomenclature.n_id)).all()
        else:
            query = query.filter(Nomenclature.n_id == identity).all()

        return list(map(lambda item: asdict(item), query))

    @classmethod
    def get_specific(cls, **kwargs: dict[str, Any]) -> \
            list[dict[str, Union[str, int]]]:
        """List of keyword arguments: item -> id of required item, parent ->
        id of parent (specify of 3 item level),
        level -> level of the item in the hierarchy,
        2 or 3 (required parent argument"""
        n_brand, n_item = aliased(Node), aliased(Node)
        query = (
            cls.query(
                Nomenclature.n_id,
                n_brand.name.label("n_brand"),
                Nomenclature.n_article,
                Nomenclature.n_color,
                Nomenclature.n_size,
                Nomenclature.n_barcode,
                Nomenclature.n_price,
                n_item.name.label("n_item"),
                Nomenclature.n_wb,
            )
            .join(n_brand, n_brand.id == Nomenclature.n_brand)
            .join(n_item, n_item.id == Nomenclature.n_item)
        )
        if kwargs['level'] == 2:
            query = query.filter(Nomenclature.n_brand == kwargs['item']).all()
            return list(map(lambda item: asdict(item), query))

        elif kwargs['level'] == 3:
            query = query.filter(Nomenclature.n_brand == kwargs['parent'],
                                 Nomenclature.n_item == kwargs['item'],
                                 )
            return list(map(lambda item: asdict(item), query))
        else:
            return []

    @classmethod
    def barcode_exist(cls, item: str) -> bool:
        query = cls.query().filter(Nomenclature.n_barcode == item).all()
        if query:
            return True
        else:
            return False
