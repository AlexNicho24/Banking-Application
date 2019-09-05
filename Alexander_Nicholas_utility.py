import random, string

def createAccountNo():
    '''
    param: None
    Return: Random account number 
    '''
    number = ''.join(random.choices(string.ascii_letters.upper() + string.digits, k=4))
    return number

