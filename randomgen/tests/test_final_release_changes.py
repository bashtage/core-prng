import pytest

from randomgen import RandomGenerator

random_gen = RandomGenerator()


def test_random_sample_deprecated():
    with pytest.deprecated_call():
        random_gen.random_sample()
