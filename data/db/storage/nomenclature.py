from sqlalchemy import Table, Column, Integer, String, ForeignKey
from sqlalchemy.orm import mapper, synonym, relationship, backref
from sqlalchemy.ext.associationproxy import association_proxy
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm.collections import attribute_mapped_collection
from data.db import storage_meta
from data.storage import Nomenclature, Node

# nomenclature_table = Table('nomenclature', storage_meta,
#                            Column('n_id', Integer, primary_key='True'),
#                            Column('n_brand', Integer, ForeignKey('tree.id')),
#                            Column('n_article', String),
#                            Column('n_color', String),
#                            Column('n_size', String),
#                            Column('n_barcode', String),
#                            Column('n_price', String),
#                            Column('n_item', Integer, ForeignKey('tree.id')),
#                            Column('n_wb', String)
#                            )
#
# mapper(Nomenclature, nomenclature_table, properties={
#     'ID': synonym('n_id'),
#     'brand': relationship(Node, foreign_keys=[nomenclature_table.c.n_brand],
#                           backref='brand'),
#     'item': relationship(Node, foreign_keys=[nomenclature_table.c.n_item],
#                          backref='item'),
#     'art': synonym('n_wb')
#
# })

Base = declarative_base()

# class Nomenclature(Base):
#     __tablename__ = 'nomenclature'
#
#     n_id = Column(Integer, primary_key='True')
#     n_brand = Column(Integer, ForeignKey('tree.id'))
#     n_article = Column(String)
#     n_color = Column(String)
#     n_size = Column(String)
#     n_barcode = Column(String)
#     n_price = Column(String)
#     n_item = Column(Integer, ForeignKey('tree.id'))
#     n_wb = Column(String)
#     ID = synonym('n_id')
#     brand = relationship(Node, foreign_keys=[n_brand])
#     item = relationship(Node, foreign_keys=[n_item])
#     art = synonym('n_wb')
#
#     def __init__(self, n_id, n_brand, n_article, n_color, n_size, n_barcode,
#                  n_price, n_item, n_wb):
#         self.n_id = n_id
#         self.n_brand = n_brand
#         self.n_article = n_article
#         self.n_color = n_color
#         self.n_size = n_size
#         self.n_barcode = n_barcode
#         self.n_price = n_price
#         self.n_item = n_item
#         self.n_wb = n_wb
#
#     def __repr__(self):
#         return f'Nomenclature {str(self.__dict__)}'
