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

__all__ = [
    'bitrate_size_based',
    'bitrate_ratio_based',
    'gb_to_bit',
    'mb_to_bit',
    'kb_to_bit',
    'b_to_bit'
]