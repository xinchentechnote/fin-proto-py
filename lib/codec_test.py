import unittest
from bytebuf import ByteBuf
from codec import *


class TestBufferUtils(unittest.TestCase):
    def setUp(self):
        self.buffer = ByteBuf()  # Assuming ByteBuf is your buffer implementation

    def test_write_len_u8(self):
        write_len(self.buffer, 42, 'u8')
        self.assertEqual(read_len(self.buffer, 'u8'), 42)

    def test_write_len_u16_le(self):
        write_len(self.buffer, 1024, 'u16')
        self.assertEqual(read_len(self.buffer, 'u16'), 1024)

    def test_write_len_u32_le(self):
        write_len(self.buffer, 65536, 'u32')
        self.assertEqual(read_len(self.buffer, 'u32'), 65536)

    def test_write_len_u64_le(self):
        write_len(self.buffer, 1234567890, 'u64')
        self.assertEqual(read_len(self.buffer, 'u64'), 1234567890)

    def test_write_len_i8(self):
        write_len(self.buffer, -42, 'i8')
        self.assertEqual(read_len(self.buffer, 'i8'), -42)

    def test_write_len_i16_le(self):
        write_len(self.buffer, -1024, 'i16')
        self.assertEqual(read_len(self.buffer, 'i16'), -1024)

    def test_write_len_invalid_type(self):
        with self.assertRaises(ValueError):
            write_len(self.buffer, 42, 'invalid')

    def test_write_string_empty(self):
        write_string(self.buffer, "", 'u32')
        self.assertEqual(read_string(self.buffer, 'u32'), "")

    def test_write_string_utf8(self):
        test_str = "Hello, 世界!"
        write_string(self.buffer, test_str, 'u16')
        self.assertEqual(read_string(self.buffer, 'u16'), test_str)

    def test_write_string_custom_encoding(self):
        test_str = "こんにちは"
        write_string(self.buffer, test_str, 'u32', 'shift_jis')
        self.assertEqual(read_string(self.buffer, 'u32', 'shift_jis'), test_str)

    def test_read_string_invalid_length(self):
        # Write a length that's too large for the buffer
        write_len(self.buffer, 1000, 'u16')
        with self.assertRaises(Exception):  # Or whatever error your buffer raises
            read_string(self.buffer, 'u16')

    def test_roundtrip_multiple_strings(self):
        strings = ["First", "", "Third string with spaces", "Final"]
        len_type = 'u32'
        
        for s in strings:
            write_string(self.buffer, s, len_type)
        
        for expected in strings:
            actual = read_string(self.buffer, len_type)
            self.assertEqual(actual, expected)

    def test_write_exact_length(self):
        """Test writing a string that exactly matches the fixed length."""
        write_fixed_string(self.buffer, "A", 1)  # Exactly 1 byte in UTF-8
        self.assertEqual(self.buffer.read_bytes(1), b'A')

    def test_write_short_string_padded(self):
        """Test writing a string shorter than the fixed length (should be padded)."""
        write_fixed_string(self.buffer, "Hi", 5)  # "Hi" is 2 bytes, padded to 5
        self.assertEqual(self.buffer.read_bytes(5), b'Hi   ')

    def test_write_long_string_truncated(self):
        """Test writing a string longer than the fixed length (should be truncated)."""
        write_fixed_string(self.buffer, "Hello, 世界!", 5)  # Truncated to 5 bytes
        self.assertEqual(self.buffer.read_bytes(5), b'Hello'[:5])  # First 5 bytes

    def test_write_empty_string(self):
        """Test writing an empty string (should be padded)."""
        write_fixed_string(self.buffer, "", 3)
        self.assertEqual(self.buffer.read_bytes(3), b'   ')

    def test_custom_padding(self):
        """Test writing with custom padding (space instead of null byte)."""
        write_fixed_string(self.buffer, "AB", 5, padding='0')
        self.assertEqual(self.buffer.read_bytes(5), b'AB000')


if __name__ == '__main__':
    unittest.main()