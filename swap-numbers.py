# The function swaps two numbers without using third variable

def swap_numbers(a,b):
    print('initial numbers a='+str(a)+' b='+str(b))
    a=a+b
    b=a-b
    a=a-b
    print('swapped numbers a='+str(a)+' b='+str(b))

swap_numbers(3,5)