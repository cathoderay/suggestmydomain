import string, random

import whois


def random_name(n=5):
    return ''.join([random.choice(string.lowercase + "0123456789") 
                    for x in xrange(n)]) + ".com"


def is_registered(name):
    try: 
        whois.query(name).creation_date
    except AttributeError:
        return False
    return True


def find_domain(name=None):
    name = name or random_name()
    return name, is_registered(name)


def find_available():
    registered = True 
    while registered:
        name, registered = find_domain()
    return name


if __name__ == '__main__':
    import sys
    if len(sys.argv) > 1:
        print find_domain(sys.argv[1])
    else:
        print find_domain()
