'''
Created on Aug 26, 2019

@author: itap_testbench_02
'''
#def main():
"""    
t = ('yalig', 38, True, 'Anhui')
print(t)
print(t[0])
print(t[3])
""" 
    
#if __name__ == '__main__':
from __future__ import print_function

def main():
    set1 = {1, 2, 3, 3, 3, 2}
    print(set1)
    print('Length =', len(set1))
    set2 = set(range(1, 10))
    print(set2)
    set1.add(4)
    set1.add(5)
    print(set1)
    set2.update([11, 12])
    #set2.remove(0)
    print(set2)
    for elem in set2:
        print(elem ** 2, end=' ')    #python --version
    print()
# from __future__ import print_function
# 
# try:
#     from __future__ import unicode_literals
# except:
#     pass    
    
    
if __name__ == '__main__':
    main()