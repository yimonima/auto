#!/usr/bin/env python3
#-*- coding:utf-8 -*-
import os

try:
    import psutil
except ModuleNotFoundError:
    print('check this module is not found and use pip install!')
    import psutil

mem=psutil.virtual_memory()

print('you memory total is:',(mem.total/1024/1024)+'M')
print('you memory used is:',(mem.used/1024/1024),'M')
print('you memory surplus is:',(mem.total-mem.used))
