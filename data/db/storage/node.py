from sqlalchemy import Column, Table, Integer, String, ForeignKey
from sqlalchemy.orm import mapper, synonym, relationship, backref, foreign
from sqlalchemy.orm.collections import attribute_mapped_collection as a_col

from data.db import storage_meta
from data.storage import Node

tree = Table('tree', storage_meta,
             Column('id', Integer, primary_key=True),
             Column('root_id', Integer,
                    ForeignKey('tree.id', ondelete='CASCADE'), index=True),
             Column('name', String, nullable=False)
             )
mapper(Node, tree,
       properties={
           'ID':synonym('id'),
           'children': relationship(Node, cascade="all",
                                    backref=backref("parent",
                                                    remote_side=tree.c.id),
                                    collection_class=a_col('name'))
       })
