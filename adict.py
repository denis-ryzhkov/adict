'''
Dict with attr access to keys.

Usage: See the test in the end of file.

adict version 0.1.2
Copyright (C) 2013 by Denis Ryzhkov <denisr@denisr.com>
MIT License, see http://opensource.org/licenses/MIT
'''

#### adict

class adict(dict):

    def __getattr__(self, name):
        try:
            return self[name]
        except KeyError as e:
            raise AttributeError(*e.args)

    def __setattr__(self, name, value):
        self[name] = value

    def copy(self):
        return adict(dict.copy(self))

#### ajson

def ajson(item):
    if isinstance(item, dict):
        item = adict(
            (name, ajson(value))
            for name, value in item.iteritems()
        )
    elif isinstance(item, list):
        item = [
            ajson(value)
            for value in item
        ]
    return item

#### test

def _test():

    d = adict(a=1) # Create from names and values.
    assert d == adict(dict(a=1)) # Create from dict.

    assert d.a == d['a'] == 1 # Get by attr and by key.

    d.b = 2 # Put by attr.
    assert d.b == d['b'] == 2

    d['c'] = 3 # Put by key.
    assert d.c == d['c'] == 3

    d.update(copy=3) # Put reserved name by update().
    d['copy'] = 3 # Put reserved name by key.
    assert d['copy'] == 3 # Get reserved name by key.

    assert isinstance(d.copy(), adict) # copy() is adict too.
    assert d.copy().a == d.a == 1 # With get by attr working too.

    assert 'invalid' not in d # Check membership.

    try:
        d.invalid # Exception.
        raise Exception('AttributeError expected')
    except AttributeError: # Exception of correct type.
        pass

    assert ajson({"e": ["f", {"g": "h"}]}).e[1].g == 'h' # Get by attr in JSON.

    print('ok')

if __name__ == '__main__':
    _test()
