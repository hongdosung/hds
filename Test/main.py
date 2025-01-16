import sys
import os

module_demo_path = os.path.join(os.getcwd(), 'hds\Test\module_demo')
print(f'os.getcwd(): {os.getcwd()}\n')
sys.path.append(module_demo_path)

# export PYTHONPATH=c:\\00.개발소스\\hds\\Test/module_demo

print('sys.path from main.py')
print('\n'.join(sys.path))
print()

print('__name__ of main.py')
print(__name__)
print()

# from module_demo import library
# from module_demo import util

from module_demo import library # sys.path.append 추가로 그냥 import libray도 가능
#import library 
from module_demo import util # sys.path.append 추가로 그냥 import util도 가능
