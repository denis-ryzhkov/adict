from distutils.core import setup

setup(
    name='adict',
    version='0.1.4',
    description='Dict with attr access to keys.',
    long_description='''
Usage::

    pip install adict
    from adict import adict

    d = adict(a=1)
    assert d.a == d['a'] == 1

See all features, including ``ajson()`` in ``adict.py:test()``.

https://github.com/denis-ryzhkov/adict/blob/master/adict.py#L46
''',
    url='https://github.com/denis-ryzhkov/adict',
    author='Denis Ryzhkov',
    author_email='denisr@denisr.com',
    license='MIT',
    classifiers=[
        'Development Status :: 4 - Beta',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 2.7',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ],
    py_modules=['adict'],
)
