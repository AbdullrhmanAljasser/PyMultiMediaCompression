import os
import ffmpeg
import shutil
from .utils import bitrate_size_based, gb_to_bit, mb_to_bit, kb_to_bit, b_to_bit

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
    if not os.path.isfile(filepath):
        raise Exception("File path is not a valid file")
    if not os.path.isabs(filepath):
        filepath = os.getcwd() + filepath
    try:
        float(finalsize)
    except Exception as e:
        raise (e)
    
    if finalsize <= 0:
        raise Exception("Unable to compress to 0 or below size")

    ext = os.path.splitext(filepath)[-1].lower()
    file_name_w_ext = filepath.split('\\')[-1]
    splitter = filepath.split('\\')
    path_to_file = ''
    for x in range(len(splitter)-1):
        path_to_file = path_to_file + '\\' +splitter[x]

    valid_ext = ['.webm', '.mpg', '.mp2', '.mpeg', '.mpe', '.mpv', '.ogg', '.mp4', '.m4p', '.m4v', '.avi', '.wmv', '.flv', '.swf', '.mov', '.qt']
    valid_flag = False

    for valid in valid_ext:
        if valid == ext:
            valid_flag = True

    if not valid_flag:
        raise Exception("Input file is not of valid video type")

    if output is None:
        if not os.path.isdir('compressed'):
            os.mkdir('compressed')
            os.chdir(os.getcwd()+'\\compressed')
        else: 
            os.chdir(os.getcwd()+'\\compressed')
    else:
        #TODO CHECK OUTPUT AND DIRECTORY
        1==1

    file_info = ffmpeg.probe(filepath)
    file_info_size = file_info['format']['size']
    file_info_duration = file_info['format']['duration']
    file_info_bitrate = (float(file_info_size)) / float(file_info_duration)

    size_type_flag = False
    for Stype in ['gb','mb','kb','b']:
        if Stype == size_type:
            size_type_flag = True

    if not size_type_flag:
        raise Exception("Size type is not correct, must be gb, mb, kb, or b")

    if size_type == 'gb':
        finalsize = gb_to_bit(finalsize)
    if size_type == 'mb':
        finalsize = mb_to_bit(finalsize)
    if size_type == 'kb':
        finalsize = kb_to_bit(finalsize)
    if size_type == 'b':
        finalsize = b_to_bit(finalsize)

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
        #TODO change the output
        1 == 1

    print(os.getcwd(), file_info_duration, bitrate_for_compression)

__all__ = [
    'video_compress_size_based'
]