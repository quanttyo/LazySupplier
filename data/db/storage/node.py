from sqlalchemy import Column, Table, Integer, String, ForeignKey, Sequence, Unicode
from sqlalchemy.orm import mapper, synonym, relationship, backref, remote, foreign
from sqlalchemy.orm.collections import attribute_mapped_collection
from sqlalchemy import func

from data.db import storage_meta
from data.storage import Node

tree = Table('tree', storage_meta,
             Column('id', Integer, primary_key=True),
             Column('root_id', Integer, ForeignKey('tree.id', ondelete='CASCADE'), index=True),
             Column('_name', String, nullable=False)
             )
mapper(Node, tree,
       properties={
           'children': relationship(Node, cascade="all",
                                    backref=backref("parent", remote_side=tree.c.id),
                                    collection_class=attribute_mapped_collection('_name'))
       })
