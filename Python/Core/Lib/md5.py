# uncompyle6 version 2.9.10
# Python bytecode 2.7 (62211)
# Decompiled from: Python 2.7.10 (default, Feb  6 2017, 23:53:20) 
# [GCC 4.2.1 Compatible Apple LLVM 8.0.0 (clang-800.0.34)]
# Embedded file name: md5.py
import warnings
warnings.warn('the md5 module is deprecated; use hashlib instead', DeprecationWarning, 2)
from hashlib import md5
new = md5
blocksize = 1
digest_size = 16