#Finds volume given x is the length of an edge
def calc_volume(x):
    if isinstance(x,float) == False:
        if isinstance(x,int) == False:
            raise TypeError('This is not an integer or decimal')
    
    if x < 0:
        raise ValueError('Cannot get negative volume!')
    sum = x * x
    return(sum * x)
