import abc
import struct

from numpy import longlong

"""  
https://netty.io/4.0/api/io/netty/buffer/ByteBuf.html  
https://docs.oracle.com/javase/8/docs/api/java/nio/ByteBuffer.html  
https://docs.rs/bytes/1.1.0/bytes/  
"""


class Buf(metaclass=abc.ABCMeta):
    class ByteOrder:
        NATIVE = "@"
        STD_NATIVE = "="
        LITTLE_ENDIAN = "<"
        BIG_ENDIAN = ">"
        NETWORK = "!"

    PAD_BYTE = "x"
    CHAR = "c"
    SIGNED_CHAR = "b"
    UNSIGNED_CHAR = "B"
    BOOLEAN = "?"
    SHORT = "h"
    UNSIGNED_SHORT = "H"
    INT = "i"
    UNSIGNED_INT = "I"
    LONG = "l"
    UNSIGNED_LONG = "L"
    LONG_LONG = "q"
    UNSIGNED_LONG_LONG = "Q"
    SSIZE_T = "n"
    SIZE_T = "N"
    EXPONENT = "e"
    FLOAT = "f"
    DOUBLE = "d"
    CHAR_ARR = "s"
    CHAR_ARR1 = "p"
    VOID = "P"

    @abc.abstractmethod
    def readable_bytes_len(self) -> int:
        pass

    @abc.abstractmethod
    def to_bytes(self) -> bytearray:
        pass

    @abc.abstractmethod
    def write_i8(self, value: int):
        pass

    @abc.abstractmethod
    def write_u8(self, value: int):
        pass

    @abc.abstractmethod
    def write_bool(self, value: bool):
        pass

    @abc.abstractmethod
    def write_i16(self, value: int):
        pass

    @abc.abstractmethod
    def write_i16_le(self, value: int):
        pass

    @abc.abstractmethod
    def write_u16(self, value: int):
        pass

    @abc.abstractmethod
    def write_u16_le(self, value: int):
        pass

    @abc.abstractmethod
    def write_i32(self, value: int):
        pass

    @abc.abstractmethod
    def write_i32_le(self, value: int):
        pass

    @abc.abstractmethod
    def write_u32(self, value: int):
        pass

    @abc.abstractmethod
    def write_u32_le(self, value: int):
        pass

    @abc.abstractmethod
    def write_i64(self, value: longlong):
        pass

    @abc.abstractmethod
    def write_i64_le(self, value: longlong):
        pass

    @abc.abstractmethod
    def write_u64(self, value: longlong):
        pass

    @abc.abstractmethod
    def write_u64_le(self, value: longlong):
        pass

    @abc.abstractmethod
    def write_f32(self, value: float):
        pass

    @abc.abstractmethod
    def write_f32_le(self, value: float):
        pass

    @abc.abstractmethod
    def write_f64(self, value: float):
        pass

    @abc.abstractmethod
    def write_f64_le(self, value: float):
        pass

    @abc.abstractmethod
    def write_bytes(self, value: bytes):
        pass

    @abc.abstractmethod
    def read_i8(self):
        pass

    @abc.abstractmethod
    def read_u8(self):
        pass

    @abc.abstractmethod
    def read_bool(self):
        pass

    @abc.abstractmethod
    def read_i16(self):
        pass

    @abc.abstractmethod
    def read_i16_le(self):
        pass

    @abc.abstractmethod
    def read_u16(self):
        pass

    @abc.abstractmethod
    def read_u16_le(self):
        pass

    @abc.abstractmethod
    def read_i32(self):
        pass

    @abc.abstractmethod
    def read_i32_le(self):
        pass

    @abc.abstractmethod
    def read_u32(self):
        pass

    @abc.abstractmethod
    def read_u32_le(self):
        pass

    @abc.abstractmethod
    def read_i64(self):
        pass

    @abc.abstractmethod
    def read_i64_le(self):
        pass

    @abc.abstractmethod
    def read_u64(self):
        pass

    @abc.abstractmethod
    def read_u64_le(self):
        pass

    @abc.abstractmethod
    def read_f32(self):
        pass

    @abc.abstractmethod
    def read_f32_le(self):
        pass

    @abc.abstractmethod
    def read_f64(self):
        pass

    @abc.abstractmethod
    def read_f64_le(self):
        pass

    @abc.abstractmethod
    def read_bytes(self, length: int) -> bytes:
        pass


class ByteBuf(Buf):
    def __init__(self, buf: bytearray = None) -> None:
        if buf is None:
            self.buf = bytearray()
            self.write_index = 0
            self.read_index = 0
        else:
            self.buf = buf
            self.write_index = len(buf)
            self.read_index = 0

    def check_readable_bytes_len(self, length: int):
        if self.readable_bytes_len() < length:
            raise Exception(
                "readable bytes length must greater than or equal %d" % length
            )

    def readable_bytes_len(self) -> int:
        return self.write_index - self.read_index

    def to_bytes(self) -> bytearray:
        return self.buf

    def write_i8(self, value: int):
        self.buf += struct.pack(Buf.SIGNED_CHAR, value)
        self.write_index += 1

    def write_u8(self, value: int):
        self.buf += struct.pack(Buf.UNSIGNED_CHAR, value)
        self.write_index += 1

    def write_bool(self, value: bool):
        self.buf += struct.pack(Buf.BOOLEAN, value)
        self.write_index += 1

    def write_i16(self, value: int):
        self.buf += struct.pack(Buf.ByteOrder.BIG_ENDIAN + Buf.SHORT, value)
        self.write_index += 2

    def write_i16_le(self, value: int):
        self.buf += struct.pack(Buf.ByteOrder.LITTLE_ENDIAN + Buf.SHORT, value)
        self.write_index += 2

    def write_u16(self, value: int):
        self.buf += struct.pack(Buf.ByteOrder.BIG_ENDIAN + Buf.UNSIGNED_SHORT, value)
        self.write_index += 2

    def write_u16_le(self, value: int):
        self.buf += struct.pack(Buf.ByteOrder.LITTLE_ENDIAN + Buf.UNSIGNED_SHORT, value)
        self.write_index += 2

    def write_i32(self, value: int):
        self.buf += struct.pack(Buf.ByteOrder.BIG_ENDIAN + Buf.INT, value)
        self.write_index += 4

    def write_i32_le(self, value: int):
        self.buf += struct.pack(Buf.ByteOrder.LITTLE_ENDIAN + Buf.INT, value)
        self.write_index += 4

    def write_u32(self, value: int):
        self.buf += struct.pack(Buf.ByteOrder.BIG_ENDIAN + Buf.UNSIGNED_INT, value)
        self.write_index += 4

    def write_u32_le(self, value: int):
        self.buf += struct.pack(Buf.ByteOrder.LITTLE_ENDIAN + Buf.UNSIGNED_INT, value)
        self.write_index += 4

    def write_i64(self, value: longlong):
        self.buf += struct.pack(Buf.ByteOrder.BIG_ENDIAN + Buf.LONG_LONG, value)
        self.write_index += 8

    def write_i64_le(self, value: longlong):
        self.buf += struct.pack(Buf.ByteOrder.LITTLE_ENDIAN + Buf.LONG_LONG, value)
        self.write_index += 8

    def write_u64(self, value: longlong):
        self.buf += struct.pack(
            Buf.ByteOrder.BIG_ENDIAN + Buf.UNSIGNED_LONG_LONG, value
        )
        self.write_index += 8

    def write_u64_le(self, value: longlong):
        self.buf += struct.pack(
            Buf.ByteOrder.LITTLE_ENDIAN + Buf.UNSIGNED_LONG_LONG, value
        )
        self.write_index += 8

    def write_f32(self, value: float):
        self.buf += struct.pack(Buf.ByteOrder.BIG_ENDIAN + Buf.FLOAT, value)
        self.write_index += 4

    def write_f32_le(self, value: float):
        self.buf += struct.pack(Buf.ByteOrder.LITTLE_ENDIAN + Buf.FLOAT, value)
        self.write_index += 4

    def write_f64(self, value: float):
        self.buf += struct.pack(Buf.ByteOrder.BIG_ENDIAN + Buf.DOUBLE, value)
        self.write_index += 8

    def write_f64_le(self, value: float):
        self.buf += struct.pack(Buf.ByteOrder.LITTLE_ENDIAN + Buf.DOUBLE, value)
        self.write_index += 8

    def write_bytes(self, value: bytes):
        if len(value) > 0:
            self.buf += value
            self.write_index += len(value)

    def read_i8(self) -> int:
        self.check_readable_bytes_len(1)
        ret = struct.unpack(
            Buf.SIGNED_CHAR, self.buf[self.read_index : self.read_index + 1]
        )
        self.read_index += 1
        return ret[0]

    def read_u8(self):
        self.check_readable_bytes_len(1)
        ret = struct.unpack(
            Buf.UNSIGNED_CHAR, self.buf[self.read_index : self.read_index + 1]
        )
        self.read_index += 1
        return ret[0]

    def read_bool(self):
        self.check_readable_bytes_len(1)
        ret = struct.unpack(
            Buf.BOOLEAN, self.buf[self.read_index : self.read_index + 1]
        )
        self.read_index += 1
        return ret[0]

    def read_i16(self):
        self.check_readable_bytes_len(2)
        ret = struct.unpack(
            Buf.ByteOrder.BIG_ENDIAN + Buf.SHORT,
            self.buf[self.read_index : self.read_index + 2],
        )
        self.read_index += 2
        return ret[0]

    def read_i16_le(self):
        self.check_readable_bytes_len(2)
        ret = struct.unpack(
            Buf.ByteOrder.LITTLE_ENDIAN + Buf.SHORT,
            self.buf[self.read_index : self.read_index + 2],
        )
        self.read_index += 2
        return ret[0]

    def read_u16(self):
        self.check_readable_bytes_len(2)
        ret = struct.unpack(
            Buf.ByteOrder.BIG_ENDIAN + Buf.UNSIGNED_SHORT,
            self.buf[self.read_index : self.read_index + 2],
        )
        self.read_index += 2
        return ret[0]

    def read_u16_le(self):
        self.check_readable_bytes_len(2)
        ret = struct.unpack(
            Buf.ByteOrder.LITTLE_ENDIAN + Buf.UNSIGNED_SHORT,
            self.buf[self.read_index : self.read_index + 2],
        )
        self.read_index += 2
        return ret[0]

    def read_i32(self):
        ret = struct.unpack(
            Buf.ByteOrder.BIG_ENDIAN + Buf.INT,
            self.buf[self.read_index : self.read_index + 4],
        )
        self.read_index += 4
        return ret[0]

    def read_i32_le(self):
        self.check_readable_bytes_len(4)
        ret = struct.unpack(
            Buf.ByteOrder.LITTLE_ENDIAN + Buf.INT,
            self.buf[self.read_index : self.read_index + 4],
        )
        self.read_index += 4
        return ret[0]

    def read_u32(self):
        self.check_readable_bytes_len(4)
        ret = struct.unpack(
            Buf.ByteOrder.BIG_ENDIAN + Buf.UNSIGNED_INT,
            self.buf[self.read_index : self.read_index + 4],
        )
        self.read_index += 4
        return ret[0]

    def read_u32_le(self):
        self.check_readable_bytes_len(4)
        ret = struct.unpack(
            Buf.ByteOrder.LITTLE_ENDIAN + Buf.UNSIGNED_INT,
            self.buf[self.read_index : self.read_index + 4],
        )
        self.read_index += 4
        return ret[0]

    def read_i64(self):
        self.check_readable_bytes_len(8)
        ret = struct.unpack(
            Buf.ByteOrder.BIG_ENDIAN + Buf.LONG_LONG,
            self.buf[self.read_index : self.read_index + 8],
        )
        self.read_index += 8
        return ret[0]

    def read_i64_le(self):
        self.check_readable_bytes_len(8)
        ret = struct.unpack(
            Buf.ByteOrder.LITTLE_ENDIAN + Buf.LONG_LONG,
            self.buf[self.read_index : self.read_index + 8],
        )
        self.read_index += 8
        return ret[0]

    def read_u64(self):
        self.check_readable_bytes_len(8)
        ret = struct.unpack(
            Buf.ByteOrder.BIG_ENDIAN + Buf.UNSIGNED_LONG_LONG,
            self.buf[self.read_index : self.read_index + 8],
        )
        self.read_index += 8
        return ret[0]

    def read_u64_le(self):
        self.check_readable_bytes_len(8)
        ret = struct.unpack(
            Buf.ByteOrder.LITTLE_ENDIAN + Buf.UNSIGNED_LONG_LONG,
            self.buf[self.read_index : self.read_index + 8],
        )
        self.read_index += 8
        return ret[0]

    def read_f32(self):
        self.check_readable_bytes_len(4)
        ret = struct.unpack(
            Buf.ByteOrder.BIG_ENDIAN + Buf.FLOAT,
            self.buf[self.read_index : self.read_index + 4],
        )
        self.read_index += 4
        return ret[0]

    def read_f32_le(self):
        self.check_readable_bytes_len(4)
        ret = struct.unpack(
            Buf.ByteOrder.LITTLE_ENDIAN + Buf.FLOAT,
            self.buf[self.read_index : self.read_index + 4],
        )
        self.read_index += 4
        return ret[0]

    def read_f64(self):
        self.check_readable_bytes_len(8)
        ret = struct.unpack(
            Buf.ByteOrder.BIG_ENDIAN + Buf.DOUBLE,
            self.buf[self.read_index : self.read_index + 8],
        )
        self.read_index += 8
        return ret[0]

    def read_f64_le(self):
        self.check_readable_bytes_len(8)
        ret = struct.unpack(
            Buf.ByteOrder.LITTLE_ENDIAN + Buf.DOUBLE,
            self.buf[self.read_index : self.read_index + 8],
        )
        self.read_index += 8
        return ret[0]

    def read_bytes(self, length: int) -> bytearray:
        self.check_readable_bytes_len(length)
        ret = self.buf[self.read_index : self.read_index + length]
        self.read_index += length
        return ret
