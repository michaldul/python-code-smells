import logging
import datetime

class Store:
    allowed_types = ()

    def __init__(self, allowed_types):
        Store.allowed_types = allowed_types
        self.store_lst = []

    def append(self, obj, time=datetime.datetime.now()):
        if type(obj) not in self.allowed_types:
            raise TypeError

        try:
            self.store_lst.append((obj, time))
        except:
            logging.debug('Can\'t append')

    def __repr__(self):
        return 'Store of {} objects'.format(len(self.store_lst))