'''
Dict with attr access to keys.

Usage:

    pip install adict
    from adict import adict

    d = adict(a=1)
    assert d.a == d['a'] == 1

See all features, including ajson() in adict.py:test().

adict version 0.1.5
Copyright (C) 2013 by Denis Ryzhkov <denisr@denisr.com>
MIT License, see http://opensource.org/licenses/MIT
'''

#### adict

class adict(dict):

    def __getattr__(self, name):
        try:
            return self[name]
        except KeyError:
            raise AttributeError("type object '{subclass_name}' has no attribute '{attr_name}'".format(subclass_name=type(self).__name__, attr_name=name))

    def __setattr__(self, name, value):
        self[name] = value

    def copy(self):
        return adict(dict.copy(self))

#### ajson

def ajson(item):
    return (
        adict((name, ajson(value)) for name, value in item.iteritems()) if isinstance(item, dict) else
        [ajson(value) for value in item] if isinstance(item, list) else
        item
    )

#### test

def test():

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
    assert d.copy().a == d.a == 1 # Really.

    assert 'invalid' not in d # Check membership.

    try:
        d.invalid # Exception.
        raise Exception('AttributeError expected')
    except AttributeError as e: # Exception is of correct type.
        assert str(e) == "type object 'adict' has no attribute 'invalid'" # And correct message.

    class SubClass(adict):
        pass
    try:
        SubClass().invalid # Exception in SubClass.
    except AttributeError as e: # Exception is of correct type.
        assert str(e) == "type object 'SubClass' has no attribute 'invalid'" # And correct message.

    j = ajson({"e": ["f", {"g": "h"}]}) # JSON with all dicts converted to adicts.
    assert j.e[1].g == 'h' # Get by attr in JSON.

    print('OK')

if __name__ == '__main__':
    test()
