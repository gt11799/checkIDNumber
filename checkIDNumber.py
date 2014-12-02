#! /usr/bin/env python
'''
Check the identify card number 
'''

weight_list = [2 ** i for i in range(18)]

def checkIDNumber(ID_number):
    ID_number = ID_number[::-1]
    
    sum_id = 0
    for number,weight in zip(ID_number,weight_list):
        sum_id = int(number) * weight
    number1 = (12 - (sum_id % 11)) % 11
    return number1
    
if __name__ == '__main__':
    ID_number = '698076193009111883'
    number1 = checkIDNumber(ID_number)
    print ID_number,number1
