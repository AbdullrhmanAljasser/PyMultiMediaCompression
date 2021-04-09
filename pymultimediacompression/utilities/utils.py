import math

def bitrate_size_based(roof_size, duration):
    try:
        roof_size = int(roof_size)
        duration = float(duration)
    except Exception as e:
        raise e

    if roof_size <= 0:
        raise Exception("Entered expected size is below 0")
    
    if duration <= 0:
        raise Exception("Entered duration is below 0")

    return math.floor(roof_size/duration)

def bitrate_ratio_based(ratio, duration, size):
    try:
        ratio = float(ratio)
        size = int(size)
        duration = float(duration)
    except Exception as e:
        raise e

    if ratio <= 0:
        raise Exception("Entered expected ratio is below 0")

    if ratio >= 1:
        raise Exception("Entered ratio is increasing (e.g over 1)")
    
    if duration <= 0:
        raise Exception("Entered duration is below 0")

    if size <= 0:
        raise Exception("Entered original size is below 0")

    return math.floor(math.floor(size*ratio)/duration)

def gb_to_bit(gigabyte):
    try:
        gigabyte = float(gigabyte)
    except Exception as e:
        raise e

    if gigabyte <= 0:
        raise Exception("Entered gigabyte is below 0")

    return gigabyte * 1024 * 1024 * 1024 * 8

def mb_to_bit(megabyte):
    try:
        megabyte = float(megabyte)
    except Exception as e:
        raise e

    if megabyte <= 0:
        raise Exception("Entered megabyte is below 0")

    return megabyte * 1024 * 1024 * 8

def kb_to_bit(kilobyte):
    try:
        kilobyte = float(kilobyte)
    except Exception as e:
        raise e

    if kilobyte <= 0:
        raise Exception("Entered kilobyte is below 0")

    return kilobyte * 1024 * 8

def b_to_bit(byte):
    try:
        byte = float(byte)
    except Exception as e:
        raise e

    if byte <= 0:
        raise Exception("Entered byte is below 0")

    return byte * 8

def final_bit_size(
    finalsize,
    size_type='mb'
):
    try:
        int(finalsize)
    except:
        Exception("Input Paramter finalsize must be an int of valid size_type=(default 'mb')")
    if size_type == 'gb':
        return gb_to_bit(finalsize)
    if size_type == 'mb':
        return mb_to_bit(finalsize)
    if size_type == 'kb':
        return kb_to_bit(finalsize)
    if size_type == 'b':
        return b_to_bit(finalsize)
    raise Exception("Entered size_type is incorrect format, gb, mb, kb or b (byte)")

def valid_size_type(size_type):
    size_type_flag = False
    for Stype in ['gb','mb','kb','b']:
        if Stype == size_type:
            size_type_flag = True

    if not size_type_flag:
        return False
    else:
        return True

def valid_video_ext(
    ext
):
    valid_ext = ['.webm', '.mpg', '.mp2', '.mpeg', '.mpe', '.mpv', '.ogg', '.mp4', '.m4p', '.m4v', '.avi', '.wmv', '.flv', '.swf', '.mov', '.qt']

    for valid in valid_ext:
        if valid == ext:
            return True
    return False

def valid_audio_ext(
    ext
):
    valid_ext = ['.mpg', '.mpeg', '.avi', '.wmv', '.mov', '.rm', '.ram', '.swf', '.flv', '.ogg', '.webm', '.mp4', '.mp3']

    for valid in valid_ext:
        if valid == ext:
            return True
    return False

def valid_image_ext(
    ext
):
    valid_ext = ['.apng', '.avif', '.gif', '.jpg', '.jpeg', '.jfif', '.pjpeg', '.pjp', '.png', '.svg', '.webp']

    for valid in valid_ext:
        if valid == ext:
            return True
    return False

__all__ = [
    'bitrate_size_based',
    'bitrate_ratio_based',
    'gb_to_bit',
    'mb_to_bit',
    'kb_to_bit',
    'b_to_bit',
    'final_bit_size',
    'valid_size_type',
    'valid_audio_ext',
    'valid_image_ext'
]