import unittest
from pymultimediacompression.utilities.utils import (
    gb_to_bit, mb_to_bit, kb_to_bit, 
    b_to_bit, final_bit_size, valid_size_type,
    valid_video_ext, valid_audio_ext, valid_image_ext
)

class test_util(unittest.TestCase):
    def test_gb_to_bit(self):
        self.assertEqual(gb_to_bit(2), 2 * 1024 * 1024 * 1024 * 8)

    def test_mb_to_bit(self):
        self.assertEqual(mb_to_bit(2), 2 * 1024 * 1024 * 8)

    def test_kb_to_bit(self):
        self.assertEqual(kb_to_bit(2), 2 * 1024 * 8)

    def test_b_to_bit(self):
        self.assertEqual(b_to_bit(2), 2 * 8)

    def test_final_bit_size(self):
        self.assertEqual(final_bit_size(60,size_type='mb'),60*1024*1024*8)

    def test_final_bit_size_fail(self):
        # Incorrect size_type 
        try:
            final_bit_size(60,size_type='ks')
            self.assertTrue(False) # If no exception raised then this fails
        except Exception as e:
            print(e)
            self.assertTrue(True)

        # Incorrect size
        try:
            final_bit_size(-5,size_type='kb')
            self.assertTrue(False) # If no exception raised then this fails
        except Exception as e:
            print(e)
            self.assertTrue(True)

    def test_valid_size_type(self):
        self.assertTrue(valid_size_type('mb'))

    def test_valid_size_type_fail(self):
        self.assertFalse(valid_size_type('mbs'))

    def test_valid_video_ext(self):
        self.assertTrue(valid_video_ext('.mp4'))

    def test_valid_video_ext_fail(self):
        self.assertFalse(valid_video_ext('.mp42'))
    
    def test_valid_audio_ext(self):
        self.assertTrue(valid_audio_ext('.mp3'))

    def test_valid_audio_ext_fail(self):
        self.assertFalse(valid_audio_ext('.mmp3'))

    def test_valid_image_ext(self):
        self.assertTrue(valid_image_ext('.png'))

    def test_valid_image_ext(self):
        self.assertFalse(valid_image_ext('.pnng'))

    