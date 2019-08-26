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

def main():
    scores = {'yaling': 95, 'xuming': 78, 'aoqi': 82}
    print(scores['yaling'])
    print(scores['xuming'])
    for elem in scores:
        print('%s\t--->\t%d' % (elem, scores[elem]))
        
    print(scores.get('aoqi', 99))
    print(scores.popitem()) 
    print(scores.popitem())
    print(scores.pop('aoqi', 100))
    
    
    
    
if __name__ == '__main__':
    main()