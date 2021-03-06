from collections import namedtuple

Enum = namedtuple('Enum', ('name', 'variants', 'attrs'))
Struct = namedtuple('Struct', ('name', 'fields', 'is_tuple', 'attrs'))
Flag = namedtuple('Flag', ('name', 'attrs'))
Field = namedtuple('Field', ('name', 'attrs'))


def variants_paths(se):
    if isinstance(se, Enum):
        return [(v, '%s::%s' % (se.name, v.name)) for v in se.variants]
    elif isinstance(se, Struct):
        return [(se, se.name)]
    else:
        raise TypeError('expected Struct or Enum')
