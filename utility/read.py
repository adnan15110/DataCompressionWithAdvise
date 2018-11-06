import os
CALGARY_DATASET_DIR = os.path.abspath(os.path.join(os.pardir,'dataset','calgary'))
print('Path to CALGARY dataset: {}'.format(CALGARY_DATASET_DIR))


# def get_next_character(f):
#     # note: assumes valid utf-8
#     c = f.read(1)
#     while c:
#         while True:
#             try:
#                 yield c.decode('ascii')
#             except UnicodeDecodeError:
#                 # we've encountered a multibyte character
#                 # read another byte and try again
#                 c += f.read(1)
#             else:
#                 # c was a valid char, and was yielded, continue
#                 c = f.read(1)
#                 break



path = os.path.abspath(os.path.join(CALGARY_DATASET_DIR,'paper1'))


# with open(path,"rb") as f:
#     for c in get_next_character(f):
#         print(chr(c))

# with open(path, 'rb') as f:
#     for chunk in iter(lambda: f.read(4096), b''):
#         print(chunk.decode("utf-8"))
#         break

file = open(path, mode='r')
import binascii
while 1:
    char = file.read(1)          # read by character
    if not char: break
    print("{} - {}".format(char, ord(char)))

file.close()