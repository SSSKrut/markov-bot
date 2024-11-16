import chardet
from pathlib import Path

def detect_and_convert_encoding(filename):
    raw_content = Path(filename).read_bytes()
    
    detected = chardet.detect(raw_content)
    print(f"Detected encoding: {detected}")
    
    # Common Russian encodings
    encodings = ['cp1251', 'koi8-r', 'iso-8859-5', 'utf-8']
    
    for encoding in encodings:
        try:
            decoded = raw_content.decode(encoding)
            print(f"\nSuccessfully decoded with {encoding}:")
            print(decoded[:500])
            return decoded
        except UnicodeDecodeError:
            continue
    
    return None

filename = "lib3.txt"
decoded_text = detect_and_convert_encoding(filename)