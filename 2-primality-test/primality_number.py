
def main():
    x = get_numb()
    primaly = get_prim(x)
    print(f'Primaly? {primaly}')

def get_numb():
    valid = False
    while not valid:
        try:
            numb = int(input('A number, please: '))
        except ValueError:
            print('\033[4:31mError\033[m')
        else:
            valid = True
    return(numb)
#asdasdasd
#asdasd
def get_prim(x):
    i = 1
    m = 0

    while i < x + 1:
        if x % i == 0:
            print(f'{x} // {i}: ', x % i)
            m += 1
        i += 1
    print(m)
    
    if m == 2:
        valid = True
    else:
        valid = False

    return(valid)
main()
