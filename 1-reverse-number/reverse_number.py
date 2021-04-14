from abc import abstractmethod
from typing import get_args

# main_function
def main():
    numb = get_numb()
    rev_numb = rev(numb)
    print('numb:', numb)
    print(f'reverse number: {rev_numb}')
    
# get number
def get_numb():
    valid = False
    print('hello')
    while not valid:
        try:
            x = int(input('A number: '))
        except ValueError:
            print("Non intereger numeric value")
        else:
            valid = True    
    return(x)
# get_len
def rev(x):
    x = str(x)
    leg = len(x) - 1
    #testes
    # print('x: ', x)
    # print(f'len {leg}')
    while leg > -1:
        rev += x[leg]
        leg -= 1
    return int(rev)
main()
