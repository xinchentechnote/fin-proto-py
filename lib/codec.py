from abc import ABC, abstractmethod

from bytebuf import ByteBuf


class BinaryCodec(ABC):
    @abstractmethod
    def encode(self, buffer: ByteBuf) -> None:
        pass

    @abstractmethod
    def decode(self, buffer: ByteBuf):
        pass

def put_len(buffer: ByteBuf, length: int, len_type: str) -> None:
    
    if len_type == 'u8':
        buffer.write_u8(length)
    elif len_type == 'u16':
        buffer.write_u16(length)
    elif len_type == 'u32':
        buffer.write_u32(length)
    elif len_type == 'u64':
        buffer.write_u64(length)
    elif len_type == 'i8':
        buffer.write_i8(length)
    elif len_type == 'i16':
        buffer.write_i16(length)
    elif len_type == 'i32':
        buffer.write_i32(length)
    elif len_type == 'i64':
        buffer.write_i64(length)
    else:
        raise ValueError(f"Unsupported length type: {len_type}")


def put_len_le(buffer: ByteBuf, length: int, len_type: str) -> None:
    
    if len_type == 'u8':
        buffer.write_u8(length)
    elif len_type == 'u16':
        buffer.write_u16_le(length)
    elif len_type == 'u32':
        buffer.write_u32_le(length)
    elif len_type == 'u64':
        buffer.write_u64_le(length)
    elif len_type == 'i8':
        buffer.write_i8(length)
    elif len_type == 'i16':
        buffer.write_i16_le(length)
    elif len_type == 'i32':
        buffer.write_i32_le(length)
    elif len_type == 'i64':
        buffer.write_i64_le(length)
    else:
        raise ValueError(f"Unsupported length type: {len_type}")

def put_string(buffer: ByteBuf, string: str, len_type: str, encoding = 'utf-8') -> None:
    if string == None or string == '':
        put_len(buffer, 0, len_type)
        return
    encoded_string = string.encode(encoding)
    put_len(buffer, len(encoded_string), len_type)
    buffer.write_bytes(encoded_string)
    
def put_string_le(buffer: ByteBuf, string: str, len_type: str, encoding = 'utf-8') -> None:
    if string == None or string == '':
        put_len_le(buffer, 0, len_type)
        return
    encoded_string = string.encode(encoding)
    put_len_le(buffer, len(encoded_string), len_type)
    buffer.write_bytes(encoded_string)
    
def get_len(buffer: ByteBuf, len_type: str) -> int:
    
    if len_type == 'u8':
        return buffer.read_u8()
    elif len_type == 'u16':
        return buffer.read_u16()
    elif len_type == 'u32':
        return buffer.read_u32()
    elif len_type == 'u64':
        return buffer.read_u64()
    elif len_type == 'i8':
        return buffer.read_i8()
    elif len_type == 'i16':
        return buffer.read_i16()
    elif len_type == 'i32':
        return buffer.read_i32()
    elif len_type == 'i64':
        return buffer.read_i64()
    else:
        raise ValueError(f"Unsupported length type: {len_type}")  
    
    
def get_len_le(buffer: ByteBuf, len_type: str) -> int:
    
    if len_type == 'u8':
        return buffer.read_u8()
    elif len_type == 'u16':
        return buffer.read_u16_le()
    elif len_type == 'u32':
        return buffer.read_u32_le()
    elif len_type == 'u64':
        return buffer.read_u64_le()
    elif len_type == 'i8':
        return buffer.read_i8()
    elif len_type == 'i16':
        return buffer.read_i16_le()
    elif len_type == 'i32':
        return buffer.read_i32_le()
    elif len_type == 'i64':
        return buffer.read_i64_le()
    else:
        raise ValueError(f"Unsupported length type: {len_type}")

def get_string(buffer: ByteBuf, len_type: str, encoding = 'utf-8') -> str:
    
    len = get_len(buffer, len_type)
    return buffer.read_bytes(len).decode(encoding)
    
def get_string_le(buffer: ByteBuf, len_type: str, encoding = 'utf-8') -> str:
    
    len = get_len_le(buffer, len_type)
    return buffer.read_bytes(len).decode(encoding)
    
    
def write_fixed_string(buffer: ByteBuf, string: str, fixed_length: int, encoding: str = 'utf-8', padding: bytes = b'\x00') -> None:
    """Write a fixed-length string to the buffer.
    
    Args:
        buffer: The buffer to write to
        string: The string to write
        fixed_length: The fixed byte length required
        encoding: The string encoding (default: 'utf-8')
        padding: The byte used for padding (default: null byte)
    
    Raises:
        ValueError: If the string cannot fit in the fixed length when encoded
    """
    encoded = string.encode(encoding)
    if len(encoded) > fixed_length:
        encoded = encoded[:fixed_length]
        buffer.write_bytes(encoded)
        return
    
    # Pad with null bytes if needed
    padded = encoded.ljust(fixed_length, padding)
    buffer.write_bytes(padded)