
from typing import Dict, Generic, Type, TypeVar

T = TypeVar("T")
M = TypeVar("M")

class SingleMeta(type):
    _instances:Dict[type,object] = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super().__call__(*args, **kwargs)
        return cls._instances[cls]
    
class MessageFactory(Generic[T, M],metaclass=SingleMeta):
    def __init__(self):
        self._creators : Dict[T,Type[M]] = {}
    
    def register(self, msg_type:T, cls:Type[M]):
        self._creators[msg_type] = cls
    
    def remove(self, msg_type:T):
        if msg_type in self._creators:
            del self._creators[msg_type]
    
    def create(self, msg_type:T) -> M:
        cls = self._creators.get(msg_type)
        if not cls:
            raise ValueError(f"Message type {msg_type} not registered.")
        return cls()