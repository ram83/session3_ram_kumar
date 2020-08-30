from fractions import Fraction

def encoded_from_base10(number, base, digit_map):
    '''
    This function returns a string encoding in the "base" for the the "number" using the "digit_map"
    Conditions that this function must satisfy:
    - 2 <= base <= 36 else raise ValueError
    - invalid base ValueError must have relevant information
    - digit_map must have sufficient length to represent the base
    - must return proper encoding for all base ranges between 2 to 36 (including)
    - must return proper encoding for all negative "numbers" (hint: this is equal to encoding for +ve number, but with - sign added)
    - the digit_map must not have any repeated character, else ValueError
    - the repeating character ValueError message must be relevant
    - you cannot use any in-built functions in the MATH module
    '''
    if base <=2 or base >= 36:
        raise ValueError(f'{base} base is not in the range of 2 and 36')
    if len(digit_map)!=base:
        raise ValueError(f'digit_map does not have sufficient length to represent base ')
    if len(digit_map)!= len(set(digit_map)):
        raise ValueError("digit_map having repeating characters")

    digits = []
    if number == 0:
        digits = [0]
    if number < 0:
        number *= -1
        encoding = '-'
    else:
        encoding = ''
    while  number > 0:
        m = number % base
        number = number // base
        digits.insert(0,m)
    encoding += ''.join([digit_map[x] for x in digits])
    return encoding

def float_equality_testing(a, b):
    '''
        This function emulates the ISCLOSE method from the MATH module, but you can't use this function
        We are going to assume:
        - rel_tol = 1e-12
        - abs_tol = 1e-05
    '''
    rel_tol = 1e-12
    abs_tol = 1e-05
    rv = abs(a - b) <= max(rel_tol * max(abs(a), abs(b)), abs_tol)
    return rv


def manual_truncation_function(f_num):
    '''
    This function emulates python's MATH.TRUNC method. It ignores everything after the decimal point. 
    It must check whether f_num is of correct type before proceed. You can use inbuilt constructors like int, float, etc
    '''

    f_num=str(f_num)
    f_num=float(f_num.split('.')[0])
    return f_num

def manual_rounding_function(f_num):
    '''
    This function emulates python's inbuild ROUND function. You are not allowed to use ROUND function, but
    expected to write your one manually.
    '''
    frac1 = Fraction(f_num)
    if frac1 >= 0:
        frac2 = frac1.numerator // frac1.denominator
    else:
        frac2 = (frac1.numerator // frac1.denominator) + 1
    return frac2

def rounding_away_from_zero(f_num):
    '''
    This function implements rounding away from zero as covered in the class
    Desperately need to use INT constructor? Well you can't. 
    Hint: use FRACTIONS and extract numerator. 

    '''
    f_nu = Fraction(f_num)
    return f_nu