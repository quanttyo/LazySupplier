from sqlalchemy import Column, Table, Integer, String, ForeignKey
from sqlalchemy.orm import mapper, synonym, relationship, backref, foreign
from sqlalchemy.orm.collections import attribute_mapped_collection
from sqlalchemy.ext.declarative import declarative_base
from data.db import storage_meta
from data.storage import Node


Base = declarative_base()

# tree = Table('tree', storage_meta,
#              Column('id', Integer, primary_key=True),
#              Column('root_id', Integer,
#                     ForeignKey('tree.id', ondelete='CASCADE'), index=True),
#              Column('name', String, nullable=False)
#              )
# mapper(Node, tree,
#        properties={
#            'ID':synonym('id'),
#            'children': relationship(Node, cascade="all",
#                                     backref=backref("parent",
#                                                     remote_side=tree.c.id),
#                                     collection_class=a_col('name'))
#        })



# class Node(Base):
#     __tablename__ = 'tree'
#     id = Column(Integer, primary_key=True)
#     root_id = Column(Integer, ForeignKey('tree.id', ondelete='CASCADE'), index=True),
#     name = Column(String, nullable=False)
#     ID = synonym('id')
#     children = relationship('Node', cascade='all', backref=backref('parent', remote_size=id),
#                             collection_class=attribute_mapped_collection('name'))