"""A program to find the prime factors of a given number.
    Also a test of a simple UI and test coverage."""

"""Program Outline
It may work better as a class.

Import list of X primes.
Ask user for integer. Verify input.
Calculate prime factors. Return list of primes ordered smallest to largest.

"""
# from pathlib import Path


def get_list_of_primes(data_source: str) -> list:
    """Read in a list of primes from a .txt file and return them as a list.
    """
    with open(data_source, 'r') as file:
        data = [int(line.rstrip('\n')) for line in file.readlines()]
    return data


def get_integer_from_user() -> int:
    pass


def find_prime_factors(i: int) -> list:
    """Returns the prime factors of the input integer as a list.
    The list of prime factors is orders from smallest to largest."""
    pass


if __name__ == '__main__':
    list_of_primes = get_list_of_primes('primes.txt')
    print(list_of_primes)
