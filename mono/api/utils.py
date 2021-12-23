import random
import string


def generate_id(n, is_alphanum=True):
    """
    generate a random id of length n
    is_alphanum (True: random string of alphanumerals; False: random string of numbers)
    """
    _id = ''.join(["{}".format(random.randint(0, 9)) for num in range(0, n)])
    if is_alphanum:
        letters_and_digits = string.ascii_letters + string.digits
        _id = ''.join(random.choice(letters_and_digits) for i in range(0, n))
    return _id


def get_reference():
    #minimum 10 values
    return f'ref-{generate_id(10)}'
