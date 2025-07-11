import os, sys

from bytebuf import ByteBuf

sys.path.append(os.getcwd())
from unittest import TestCase
import pytest


class TestByteBuf(TestCase):
    def setUp(self) -> None:
        self.buf = ByteBuf()

    def test_byte_buf(self) -> int:
        self.buf.write_i8(127)
        self.buf.write_i8(127)
        self.buf.write_i8(1)
        self.buf.write_f32(1)
        buf1 = ByteBuf(self.buf.to_bytes())
        self.assertEqual(7, buf1.readable_bytes_len())

    def test_readable_bytes_len(self) -> int:
        self.buf.write_i8(127)
        self.buf.write_i8(127)
        self.buf.write_i8(1)
        self.buf.write_f32(1)
        self.assertEqual(7, self.buf.readable_bytes_len())

    def test_to_bytes(self) -> bytes:
        self.buf.write_i8(127)
        self.buf.write_i8(127)
        self.buf.write_i8(1)
        self.assertEqual(b"\x7f\x7f\x01", self.buf.to_bytes())

    def test_write_i8(self):
        self.buf.write_i8(-128)
        self.buf.write_i8(0)
        self.buf.write_i8(127)
        self.assertEqual(-128, self.buf.read_i8())
        self.assertEqual(0, self.buf.read_i8())
        self.assertEqual(127, self.buf.read_i8())

    def test_write_i8_failed1(self):
        with pytest.raises(Exception):
            self.buf.write_i8(128)

    def test_write_i8_failed2(self):
        with pytest.raises(Exception):
            self.buf.write_i8(-129)

    def test_write_i8_failed3(self):
        with pytest.raises(Exception):
            self.buf.read_i8()

    def test_write_u8(self):
        self.buf.write_u8(0)
        self.buf.write_u8(127)
        self.buf.write_u8(255)
        self.assertEqual(0, self.buf.read_u8())
        self.assertEqual(127, self.buf.read_u8())
        self.assertEqual(255, self.buf.read_u8())

    def test_write_u8_failed1(self):
        with pytest.raises(Exception):
            self.buf.write_u8(-1)

    def test_write_u8_failed2(self):
        with pytest.raises(Exception):
            self.buf.write_u8(256)

    def test_write_bool(self):
        self.buf.write_bool(True)
        self.buf.write_bool(False)
        self.buf.write_bool(1)
        self.buf.write_bool(0)
        self.buf.write_bool(22222)
        self.assertTrue(self.buf.read_bool())
        self.assertFalse(self.buf.read_bool())
        self.assertTrue(self.buf.read_bool())
        self.assertFalse(self.buf.read_bool())
        self.assertTrue(self.buf.read_bool())

    def test_write_i16(self):
        self.buf.write_i16(-32768)
        self.buf.write_i16(0)
        self.buf.write_i16(127)
        self.buf.write_i16(32767)
        self.assertEqual(-32768, self.buf.read_i16())
        self.assertEqual(0, self.buf.read_i16())
        self.assertEqual(127, self.buf.read_i16())
        self.assertEqual(32767, self.buf.read_i16())

    def test_write_i16_failed1(self):
        with pytest.raises(Exception):
            self.buf.write_i16(-32769)

    def test_write_i16_failed2(self):
        with pytest.raises(Exception):
            self.buf.write_i16(32768)

    def test_write_i16_le(self):
        self.buf.write_i16_le(-32768)
        self.buf.write_i16_le(0)
        self.buf.write_i16_le(127)
        self.buf.write_i16_le(32767)
        self.buf.write_i16_le(32767)
        self.assertEqual(-32768, self.buf.read_i16_le())
        self.assertEqual(0, self.buf.read_i16_le())
        self.assertEqual(127, self.buf.read_i16_le())
        self.assertEqual(32767, self.buf.read_i16_le())
        self.assertNotEqual(32767, self.buf.read_i16())

    def test_write_u16(self):
        self.buf.write_u16(0)
        self.buf.write_u16(127)
        self.buf.write_u16(65535)
        self.assertEqual(0, self.buf.read_u16())
        self.assertEqual(127, self.buf.read_u16())
        self.assertEqual(65535, self.buf.read_u16())

    def test_write_u16_failed1(self):
        with pytest.raises(Exception):
            self.buf.write_u16(-1)

    def test_write_u16_failed2(self):
        with pytest.raises(Exception):
            self.buf.write_u16(65536)

    def test_write_u16_le(self):
        self.buf.write_u16_le(0)
        self.buf.write_u16_le(127)
        self.buf.write_u16_le(65535)
        self.buf.write_u16_le(65534)
        self.assertEqual(0, self.buf.read_u16_le())
        self.assertEqual(127, self.buf.read_u16_le())
        self.assertEqual(65535, self.buf.read_u16_le())
        self.assertNotEqual(65534, self.buf.read_u16())

    def test_write_i32(self):
        self.buf.write_i32(-(2**31))
        self.buf.write_i32(0)
        self.buf.write_i32(127)
        self.buf.write_i32(127)
        self.buf.write_i32(2**31 - 1)
        self.assertEqual(-(2**31), self.buf.read_i32())
        self.assertEqual(0, self.buf.read_i32())
        self.assertEqual(127, self.buf.read_i32())
        self.assertNotEqual(127, self.buf.read_i32_le())
        self.assertEqual(2**31 - 1, self.buf.read_i32())

    def test_write_i32_le(self):
        self.buf.write_i32_le(-(2**31))
        self.buf.write_i32_le(0)
        self.buf.write_i32_le(127)
        self.buf.write_i32_le(127)
        self.buf.write_i32_le(2**31 - 1)
        self.assertEqual(-(2**31), self.buf.read_i32_le())
        self.assertEqual(0, self.buf.read_i32_le())
        self.assertEqual(127, self.buf.read_i32_le())
        self.assertNotEqual(127, self.buf.read_i32())
        self.assertEqual(2**31 - 1, self.buf.read_i32_le())

    def test_write_u32(self):
        self.buf.write_u32(0)
        self.buf.write_u32(127)
        self.buf.write_u32(127)
        self.buf.write_u32(2**32 - 1)
        self.assertEqual(0, self.buf.read_u32())
        self.assertEqual(127, self.buf.read_u32())
        self.assertNotEqual(127, self.buf.read_u32_le())
        self.assertEqual(2**32 - 1, self.buf.read_u32())

    def test_write_u32_failed1(self):
        with pytest.raises(Exception):
            self.buf.write_u32(-1)

    def test_write_u32_failed2(self):
        with pytest.raises(Exception):
            self.buf.write_u32(2**32)

    def test_write_u32_le(self):
        self.buf.write_u32_le(0)
        self.buf.write_u32_le(127)
        self.buf.write_u32_le(127)
        self.buf.write_u32_le(2**32 - 1)
        self.assertEqual(0, self.buf.read_u32_le())
        self.assertEqual(127, self.buf.read_u32_le())
        self.assertNotEqual(127, self.buf.read_u32())
        self.assertEqual(2**32 - 1, self.buf.read_u32_le())

    def test_write_i64(self):
        self.buf.write_i64(-(2**63))
        self.buf.write_i64(0)
        self.buf.write_i64(127)
        self.buf.write_i64(127)
        self.buf.write_i64(2**63 - 1)
        self.assertEqual(-(2**63), self.buf.read_i64())
        self.assertEqual(0, self.buf.read_i64())
        self.assertEqual(127, self.buf.read_i64())
        self.assertNotEqual(127, self.buf.read_i64_le())
        self.assertEqual(2**63 - 1, self.buf.read_i64())

    def test_write_i64_le(self):
        self.buf.write_i64_le(-(2**63))
        self.buf.write_i64_le(0)
        self.buf.write_i64_le(127)
        self.buf.write_i64_le(127)
        self.buf.write_i64_le(2**63 - 1)
        self.assertEqual(-(2**63), self.buf.read_i64_le())
        self.assertEqual(0, self.buf.read_i64_le())
        self.assertEqual(127, self.buf.read_i64_le())
        self.assertNotEqual(127, self.buf.read_i64())
        self.assertEqual(2**63 - 1, self.buf.read_i64_le())

    def test_write_u64(self):
        self.buf.write_i64_le(-(2**63))
        self.buf.write_i64_le(0)
        self.buf.write_i64_le(127)
        self.buf.write_i64_le(127)
        self.buf.write_i64_le(2**63 - 1)
        self.assertEqual(-(2**63), self.buf.read_i64_le())
        self.assertEqual(0, self.buf.read_i64_le())
        self.assertEqual(127, self.buf.read_i64_le())
        self.assertNotEqual(127, self.buf.read_i64())
        self.assertEqual(2**63 - 1, self.buf.read_i64_le())

    def test_write_u64_le(self):
        self.buf.write_u64_le(0)
        self.buf.write_u64_le(127)
        self.buf.write_u64_le(127)
        self.buf.write_u64_le(2**64 - 1)
        self.assertEqual(0, self.buf.read_u64_le())
        self.assertEqual(127, self.buf.read_u64_le())
        self.assertNotEqual(127, self.buf.read_u64())
        self.assertEqual(2**64 - 1, self.buf.read_u64_le())

    def test_write_f32(self):
        self.buf.write_f32(0)
        self.buf.write_f32(127)
        self.buf.write_f32(127)
        self.buf.write_f32(12.0)
        self.assertEqual(0, self.buf.read_f32())
        self.assertEqual(127, self.buf.read_f32())
        self.assertNotEqual(127, self.buf.read_f32_le())
        self.assertEqual(12.0, self.buf.read_f32())

    def test_write_f32_le(self):
        self.buf.write_f32_le(0)
        self.buf.write_f32_le(127)
        self.buf.write_f32_le(127)
        self.buf.write_f32_le(12.0)
        self.assertEqual(0, self.buf.read_f32_le())
        self.assertEqual(127, self.buf.read_f32_le())
        self.assertNotEqual(127, self.buf.read_f32())
        self.assertEqual(12.0, self.buf.read_f32_le())

    def test_write_f64(self):
        self.buf.write_f64(0)
        self.buf.write_f64(127)
        self.buf.write_f64(127)
        self.buf.write_f64(12.0)
        self.assertEqual(0, self.buf.read_f64())
        self.assertEqual(127, self.buf.read_f64())
        self.assertNotEqual(127, self.buf.read_f64_le())
        self.assertEqual(12.0, self.buf.read_f64())

    def test_write_f64_le(self):
        self.buf.write_f64_le(0)
        self.buf.write_f64_le(127)
        self.buf.write_f64_le(127)
        self.buf.write_f64_le(12.0)
        self.assertEqual(0, self.buf.read_f64_le())
        self.assertEqual(127, self.buf.read_f64_le())
        self.assertNotEqual(127, self.buf.read_f64())
        self.assertEqual(12.0, self.buf.read_f64_le())

    def test_write_bytes(self):
        self.buf.write_bytes(b"hello")
        self.assertEqual(b"hel", self.buf.read_bytes(3))
        self.assertEqual(b"lo", self.buf.read_bytes(2))
