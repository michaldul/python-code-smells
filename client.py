from store import *

if __name__ == '__main__':
    list = Store(allowed_types=(str, ))
    list.append('test object')
    print(list)