import mya_encoder
import mya_decoder

import sys
# import re


print("To use incoder: Enter 0\nTo use decoder: Enter 1")
flag = int(sys.stdin.readline())

print("Please write the text...")
text = sys.stdin.readline()

print("[Result]")
if flag:
    print(mya_decoder.myaDecoder(text))
else:
    print(mya_encoder.myaEncoder(text))




#영문/한글 구분(?)
# reg = re.compile(r'[a-zA-Z]')

# if reg.match(text):
#     print(mya_encoder.myaEncoder(text))
# else:
#     print(mya_decoder.myaDecoder(text))

