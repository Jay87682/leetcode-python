#!/usr/bin/python3

"""
strings are immutable sequences of Unicode code points.
"""
## thriple quoted: multiple line present
# mul_line = """ this is the test line:
#  Hello, world """
# print(mul_line)

## There is no mutable string type.
## But str.join() or io.StringIO can create string obj
# test_1 = 'test_1'
# print(id(test_1))
# print(id(test_1.join('test_2')))
# chinese=u'中文'
# print(str('元').encode('big5').decode('unicode_escape'))
# print(chinese)
# print(chinese.encode(encoding='big5', errors='strict'))
# print(str(chinese).encode(encoding='big5', errors='strict'))

"""
  print chinese
  ref: https://github.com/rgbkrk/atom-script/issues/738
"""
# import sys
# import io
# print(sys.stdout.encoding)
# print(sys.stdin.encoding)
# print(sys.stderr.encoding)
#
# sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
# # sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')
# ## or we can use the "PYTHONIOENCODING=utf-8 in system environments"
# print(sys.stdout.encoding)
# print(sys.stdin.encoding)
# print(sys.stderr.encoding)
# print ('中文')


"""
bytes is the immutable sequence of integer (akin to a tuple)
 b[0] => integer
 b[0:1] => bytes object
For string: both are string
"""
# w = b'test'  # same as following line
# w = b'\x74\x65\x73\x74'
# print(type(w)) ## bytes
# print(w)
# print(type(w[0])) ##integer
# print(w[0])
# print(type(w[:1])) ## bytes
# print(w[:1])
#
# print(w.hex())
## Any binary value over 127 must be entered into bytes literals
# print((127).to_bytes(1, byteorder='big'))  ## => \x7f
# x = b'\x61'   ## 97 => a start of ASCII
# print(x)
# print(b'\x7a')  ## 122 => z
# x = b'\x7e'   ## 126 => ~
# print(x)
# x = b'\x7f'   ## 127 => \x7f
# print(x)

### r (means raw) will disble the escape sequence processing
# k = r'\x74\x65\x73\x74' #This is string \x74\x65...
# print(k)
# print(k[2])

""" Underscore _ """