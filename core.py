import string, random

import whois


def random_name(n=5):
    return ''.join([random.choice(string.lowercase + "0123456789") for x in xrange(n)]) + ".com"


def is_registered(name):
    try: 
        whois.query(name).creation_date
    except AttributeError:
        return False
    return True


def find_my_domain():
    name = random_name()
    return name, is_registered(name)


if __name__ == '__main__':
    print find_my_domain()
