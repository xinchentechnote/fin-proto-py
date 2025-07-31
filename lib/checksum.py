from abc import ABC, abstractmethod
from typing import Generic, TypeVar
import zlib

from bytebuf import ByteBuf


InputType = TypeVar("InputType")
OutputType = TypeVar("OutputType")

class ChecksumService(ABC, Generic[InputType, OutputType]):
    @abstractmethod
    def algorithm(self) -> str:
        pass

    @abstractmethod
    def calc(self, data: InputType) -> OutputType:
        pass
    

    
class Crc16ChecksumService(ChecksumService):
    def algorithm(self):
        return "CRC16"

    def calc(self, data:ByteBuf):
        crc = 0xFFFF
        for b in data.to_bytes():
            crc ^= b
            for _ in range(8):
                if crc & 1:
                    crc = (crc >> 1) ^ 0xA001
                else:
                    crc >>= 1
        return crc & 0xFFFF

    
class Crc32ChecksumService(ChecksumService):
    def algorithm(self):
         return "CRC32"

    def calc(self, data:ByteBuf):
        val = zlib.crc32(data.to_bytes()) & 0xFFFFFFFF
        return val

class SsebinChecksumService(ChecksumService):
    def algorithm(self):
         return "SSE_BIN"

    def calc(self, data:ByteBuf):
        checksum = 0
        for b in data.to_bytes():
            checksum = (checksum + b) & 0xFF
        return checksum

class SzsebinChecksumService(ChecksumService):
    def algorithm(self):
        return "SZSE_BIN"

    def calc(self, data:ByteBuf):
        checksum = 0
        for b in data.to_bytes():
            checksum += b
        return checksum % 256
    
def create_checksum_service(algorithm: str) -> ChecksumService:
    """Factory method to create checksum services by name."""
    mapping = {
        "CRC16": Crc16ChecksumService(),
        "CRC32": Crc32ChecksumService(),
        "SSE_BIN": SsebinChecksumService(),
        "SZSE_BIN": SzsebinChecksumService()
    }
    return mapping[algorithm]