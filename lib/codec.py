from abc import ABC, abstractmethod

from bytebuf import ByteBuf


class BinaryCodec(ABC):
    @abstractmethod
    def encode(self, buffer: ByteBuf) -> None:
        pass

    @abstractmethod
    def decode(self, buffer: ByteBuf):
        pass
