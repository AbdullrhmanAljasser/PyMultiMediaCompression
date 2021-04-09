import unittest
from pymultimediacompression import videomedia, check_required, video_compress_size_based

path_191_1080p_54_mp4 = 'C:\\Users\\Abdullrhman\\Videos\\Test\\191_1080p_54.mp4'
path_191_720p_20_mp4 = 'C:\\Users\\Abdullrhman\\Videos\\Test\\191_720p_20.mp4'
path_360_1080p_202_mp4 = 'C:\\Users\\Abdullrhman\\Videos\\Test\\360_1080p_202.mp4'
path_360_720p_101_mp4 = 'C:\\Users\\Abdullrhman\\Videos\\Test\\360_720p_101.mp4'

ow_path_191_1080p_54_mp4 = 'C:\\Users\\Abdullrhman\\Videos\\Test\\overwrite_test\\191_1080p_54.mp4'
ow_path_191_720p_20_mp4 = 'C:\\Users\\Abdullrhman\\Videos\\Test\\overwrite_test\\191_720p_20.mp4'
ow_path_360_1080p_202_mp4 = 'C:\\Users\\Abdullrhman\\Videos\\Test\\overwrite_test\\360_1080p_202.mp4'
ow_path_360_720p_101_mp4 = 'C:\\Users\\Abdullrhman\\Videos\\Test\\overwrite_test\\360_720p_101.mp4'

output_path = 'C:\\Users\\Abdullrhman\\Videos\\Test\\output_test'

class test_requirement(unittest.TestCase):
    def test_check_no_err(self):
        check_required()

class test_compression(unittest.TestCase):

    def test_compression_overwrite(self):
        True
        # self.assertTrue(video_compress_size_based(ow_path_360_720p_101_mp4,65))

    def test_compression_nonOW(self):
        True
        self.assertTrue(video_compress_size_based(path_360_1080p_202_mp4, 101, output=output_path))

if __name__ == '__main__':
    unittest.main()