'''
Created on Aug 26, 2019

@author: itap_testbench_02
'''
import os
import time


def main():
    content = 'dont go break my heart'
    while True:
         
        os.system('cls')  # os.system('clear')
        print(content)
         
        time.sleep(0.2)
        content = content[1:] + content[0]
        #break

if __name__ == '__main__':
    main()