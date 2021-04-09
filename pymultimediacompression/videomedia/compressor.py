import os
import ffmpeg
import subprocess
import shutil
from pymultimediacompression.utilities.utils import bitrate_size_based, gb_to_bit, mb_to_bit, kb_to_bit, b_to_bit

MISSING_REQUIREMENTS = "FFmpeg required to be installed to use PyMultiMediaCompression \n Check https://github.com/AbdullrhmanAljasser/PyMultiMediaCompression"

'''
Check if required installs are satisfied

Raise an error if not
'''
def check_required():
    check = subprocess.call(['which', 'ffmpeg'])
    if check != 0:
        raise Exception(MISSING_REQUIREMENTS)
    check = subprocess.call(['which', 'ffprobe'])
    if check != 0:
        raise Exception(MISSING_REQUIREMENTS)

'''
Video Compression Based on given Size

Description:
    A function to allow users to compressa given video to their expected video size

Input Paramters:
    filepath  (Required): Path of the video file being compressed
    finalsize (Required): expected final size of video
    size_type (Optional): Specify final size type gb, mb, kb, or b (Default mb)
    output    (Optional): To keep original video specify output path to stop overwriting
    codec     (Optional): Specify the codec used to compress (Default x264)

    #TODO: More parameters to give more freedom to user
'''
def video_compress_size_based(
    filepath,
    finalsize,
    size_type='mb',
    output=None,
    codec='libx264'
):
    # Check if the required installs are satisfied
    check_required()

    # Check if filepath is a file
    if not os.path.isfile(filepath):
        raise Exception("File path is not a valid file")
    # Check if filepath is absolute or not
    if not os.path.isabs(filepath):
        filepath = os.getcwd() + filepath

    # Check if asked size is a correct number ==>
    try:
        float(finalsize)
    except Exception as e:
        raise (e)
    
    if finalsize <= 0:
        raise Exception("Unable to compress to 0 or below size")
    # END <==

    # Retrieve file extension to ensure it applicable ==>
    ext = os.path.splitext(filepath)[-1].lower()
    file_name_w_ext = filepath.split('\\')[-1]
    splitter = filepath.split('\\')
    path_to_file = ''
    for x in range(len(splitter)-1):
        path_to_file = path_to_file + '\\' +splitter[x]

    if not valid_video_ext(ext):
        raise Exception("Input file is not of valid video type")
    # END <==

    # Setup output (Overwrite/None)
    if output is None:
        if not os.path.isdir('compressed'):
            os.mkdir('compressed')
            os.chdir(os.getcwd()+'\\compressed')
        else: 
            os.chdir(os.getcwd()+'\\compressed')
    else:
        if os.path.isdir(output):
            if not os.path.isfile(output):
                if not os.path.isabs(output):
                    output = os.getcwd() + output
                    os.chdir(output)
                else:
                    os.chdir(output)
            else:
                raise Exception("Output path is a file not a directory")
        else:
            raise Exception("Output path is not a valid directory, maybe file doesn't exists?")

    file_info = ffmpeg.probe(filepath)
    file_info_size = file_info['format']['size']
    file_info_duration = file_info['format']['duration']
    file_info_bitrate = (float(file_info_size)) / float(file_info_duration)

    if not valid_size_type(size_type):
        raise Exception("Size type is not correct, must be gb, mb, kb, or b")

    finalsize = final_bit_size(finalsize, size_type=size_type)

    bitrate_for_compression = bitrate_size_based(finalsize, file_info_duration)

    try:
        ffmpeg.input(filepath)\
        .output(file_name_w_ext, **{'vcodec':codec, 'video_bitrate':bitrate_for_compression})\
        .overwrite_output()\
        .run()
    except Exception as e:
        raise (e)

    path_to_compressed = os.getcwd() + '\\' + file_name_w_ext

    if output is None:
        # Moving to overwrite file
        shutil.move(path_to_compressed, filepath)
    else:
        # Moving to the specified output
        True
        # shutil.move(path_to_compressed, output)

    return True

__all__ = [
    'video_compress_size_based',
    'check_required'
]