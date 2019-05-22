from randomgen.dsfmt import DSFMT
from randomgen.generator import Generator
from randomgen.mt19937 import MT19937
from randomgen.mtrand import RandomState
from randomgen.pcg32 import PCG32
from randomgen.pcg64 import PCG64
from randomgen.philox import Philox
from randomgen.threefry import ThreeFry
from randomgen.threefry32 import ThreeFry32
from randomgen.xoroshiro128 import Xoroshiro128
from randomgen.xorshift1024 import Xorshift1024

from randomgen.mt64 import MT64
from randomgen.xoshiro256 import Xoshiro256
from randomgen.xoshiro512 import Xoshiro512

BitGenerators = {'MT19937': MT19937,
                 'MT64': MT64,
                 'DSFMT': DSFMT,
                 'PCG32': PCG32,
                 'PCG64': PCG64,
                 'Philox': Philox,
                 'ThreeFry': ThreeFry,
                 'ThreeFry32': ThreeFry32,
                 'Xorshift1024': Xorshift1024,
                 'Xoroshiro128': Xoroshiro128,
                 'Xoshiro256': Xoshiro256,
                 'Xoshiro512': Xoshiro512,
                 }


def __generator_ctor(bit_generator_name='mt19937'):
    """
    Pickling helper function that returns a Generator object

    Parameters
    ----------
    bit_generator_name: str
        String containing the core BitGenerator

    Returns
    -------
    rg: Generator
        Generator using the named core BitGenerator
    """
    try:
        bit_generator_name = bit_generator_name.decode('ascii')
    except AttributeError:
        pass
    if bit_generator_name in BitGenerators:
        bit_generator = BitGenerators[bit_generator_name]
    else:
        raise ValueError(
            str(bit_generator_name) + ' is not a known BitGenerator module.')

    return Generator(bit_generator())


def __bit_generator_ctor(bit_generator_name='MT19937'):
    """
    Pickling helper function that returns a bit generator object

    Parameters
    ----------
    bit_generator_name: str
        String containing the name of the bit generator

    Returns
    -------
    bit_generator: BitGenerator
        Bit generator instance
    """
    try:
        bit_generator_name = bit_generator_name.decode('ascii')
    except AttributeError:
        pass
    if bit_generator_name in BitGenerators:
        bit_generator = BitGenerators[bit_generator_name]
    else:
        raise ValueError(
            str(bit_generator_name) + ' is not a known BitGenerator module.')

    return bit_generator()


def __randomstate_ctor(bit_generator_name='mt19937'):
    """
    Pickling helper function that returns a legacy RandomState-like object

    Parameters
    ----------
    bit_generator_name: str
        String containing the core BitGenerator

    Returns
    -------
    rs: RandomState
        Legacy RandomState using the named core BitGenerator
    """
    try:
        bit_generator_name = bit_generator_name.decode('ascii')
    except AttributeError:
        pass
    if bit_generator_name in BitGenerators:
        bit_generator = BitGenerators[bit_generator_name]
    else:
        raise ValueError(
            str(bit_generator_name) + ' is not a known BitGenerator module.')

    return RandomState(bit_generator())
