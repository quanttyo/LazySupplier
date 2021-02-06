from sqlalchemy import Table, Column, Integer, String, ForeignKey
from sqlalchemy.orm import mapper, synonym, relationship, backref
from sqlalchemy.ext.associationproxy import association_proxy
from sqlalchemy.orm.collections import attribute_mapped_collection
from data.db import storage_meta
from data.storage import Nomenclature, Node


nomenclature_table = Table('nomenclature', storage_meta,
                           Column('n_id', Integer, primary_key='True'),
                           Column('n_brand', Integer, ForeignKey('tree.id')),
                           Column('n_article', String),
                           Column('n_color', String),
                           Column('n_size', String),
                           Column('n_barcode', String),
                           Column('n_price', String),
                           Column('n_item', Integer, ForeignKey('tree.id')),
                           Column('n_wb', String)
                           )

mapper(Nomenclature, nomenclature_table, properties={
            'id':synonym('n_id'),
            #'brand': relation(Node, backref=backref("brand",cascade="all,delete", collection_class=attribute_mapped_collection('_name')),
                              #foreign_keys=[nomenclature_table.c.n_brand]),
            'brand': relationship(Node, foreign_keys=[nomenclature_table.c.n_brand], backref='brand'),
            'item': relationship(Node, foreign_keys=[nomenclature_table.c.n_item], backref='item'),
             'art':synonym('n_wb')

})

