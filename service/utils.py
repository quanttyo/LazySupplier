from __future__ import annotations
from typing import Generic, TypeVar, Callable

T = TypeVar('T')
Value = TypeVar('Value')


class ClassProperty(Generic[T]):

    def __init__(self, f_get: Callable[[T], Value]) -> None:
        self.f_get = f_get

    def __get__(self, obj, instance=None) -> Value:
        if instance is None:
            instance = type(obj)
        return self.f_get.__get__(obj, instance)()


def classproperty(func):
    if not isinstance(func, (classmethod, staticmethod)):
        func = classmethod(func)

    return ClassProperty(func)
