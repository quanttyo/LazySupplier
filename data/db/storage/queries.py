from sqlalchemy.orm import aliased
from sqlalchemy import desc

from data.db import get_storage_session
from data.storage import Node, Nomenclature


def roots_node(child_id: int = 1) -> list:
    """Returns a node of tree with the following structure: parent_name, child_name, child_id
        An default, returns root of the tree."""
    parent, child = aliased(Node), aliased(Node)
    query = get_storage_session().query(parent._name, child._name, child.id).join(parent,
                                                                                  child.root_id == parent.id).filter(
        parent.id == child_id).all()
    return query

def roots(parent: int = 1) -> list:
    p, c = aliased(Node), aliased(Node)
    query = get_storage_session().query(c._name, c.id).join(p, c.root_id == p.id).filter(p.id == parent).all()
    return query

def get_tree_name_by_id(name: int) -> str:
    try:
        return get_storage_session().query(Node._name).filter(Node.id == str(name)).all()[0]._asdict()['_name']
    except IndexError as e:
        return ''


def get_tree_id_by_name(arg: str) -> int:
    try:
        return get_storage_session().query(Node.id).filter(Node._name == arg).all()[0]._asdict()['id']
    except IndexError as e:
        return 0


def add_node(parent: int, name: str) -> tuple:
    a = Node()
    a.root_id = parent
    a._name = name
    get_storage_session().add(a)
    get_storage_session().flush()
    return a.id, a._name


def get_tree_child(arg: id) -> dict:
    try:
        query = get_storage_session().query(Node.id, Node._name).filter(Node.root_id == str(arg)).all()
        return dict((y, x) for x, y in query)
    except ValueError as e:
        return {}


def tree_no_children(parent: int) -> bool:
    if not get_storage_session().query(Node.id).filter(Node.root_id == str(parent)).all():
        return True
    else:
        return False


def nomenclature(identity: int = -1, visual: bool = True) -> list:
    n_brand, n_item = aliased(Node), aliased(Node)
    if visual:
        query = get_storage_session().query(Nomenclature.n_id, n_brand._name.label('n_brand'), Nomenclature.n_article,
                                        Nomenclature.n_color, Nomenclature.n_size, Nomenclature.n_barcode,
                                        Nomenclature.n_price, n_item._name.label('n_item'),
                                        Nomenclature.n_wb).join(n_brand, n_brand.id == Nomenclature.n_brand) \
        .join(n_item, n_item.id == Nomenclature.n_item)
    else:
        return get_storage_session().query(Nomenclature).order_by(desc(Nomenclature.n_id)).all()
    if identity == -1:
        query = query.order_by(desc(Nomenclature.n_id)).all()
    else:
        query = query.filter(Nomenclature.n_id == identity).all()

    return list(map(lambda item: item._asdict(), query))




def nomenclature_query(**kwargs: int) -> list:
    """ List of keyword arguments: item -> id of required item, parent -> id of parent (specify of 3 item level),
        level -> level of the item in the hierarchy, 2 or 3 (required parent argument"""
    n_brand, n_item = aliased(Node), aliased(Node)
    query = get_storage_session().query(Nomenclature.n_id, n_brand._name.label('n_brand'), Nomenclature.n_article,
                                        Nomenclature.n_color, Nomenclature.n_size, Nomenclature.n_barcode,
                                        Nomenclature.n_price, n_item._name.label('n_item'),
                                        Nomenclature.n_wb).join(n_brand, n_brand.id == Nomenclature.n_brand) \
        .join(n_item, n_item.id == Nomenclature.n_item)
    if kwargs['level'] == 3:
        query = query.filter(Nomenclature.n_brand == kwargs['parent'], Nomenclature.n_item == kwargs['item'])
        return list(map(lambda item: item._asdict(), query))
    elif kwargs['level'] == 2:
        query = query.filter(Nomenclature.n_brand == kwargs['item'])
        return list(map(lambda item: item._asdict(), query))
    else:
        return []

def nomenclature_exist_barcode(item: str) -> bool:
    query = get_storage_session().query(Nomenclature).filter(Nomenclature.n_barcode == item).all()
    if query:
        return True
    else:
        return False

