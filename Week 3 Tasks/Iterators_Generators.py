class Countdown:
    " iterator class that counts down from a given number to 1."

    def __init__(self, start_number):
        self.start_number = start_number

    def __iter__(self):
        return self

    def __next__(self):
        if self.start_number > 0:
            number = self.start_number
            self.start_number -= 1
            return number
        else:
            raise StopIteration

def fibonacci_generator(limit):
    """
    A generator function that yields Fibonacci numbers up to a specified limit.
        limit: The maximum value for the Fibonacci sequence.
    Yields/ returns:
        Fibonacci numbers from 0 to limit.
    """
    a, b = 0, 1
    while a < limit:
        yield a
        a, b = b, a + b

def random_number_generator(min_value, max_value):
    """
    A generator function that yields a sequence of random numbers between a specified range.
        min_value: The minimum value for the random number range.
        max_value: The maximum value for the random number range (inclusive).
    Yields:
        Random numbers between min_value and max_value.
    """
    import random
    while True:
        yield random.randint(min_value, max_value)

if __name__ == "__main__":
    # Demonstrate Countdown class
    for number in Countdown(5):
        print(number)

    # Demonstrate fibonacci_generator
    for number in fibonacci_generator(10):
        print(number)

    # Demonstrate random_number_generator (limited output due to infinite generator)
    for _ in range(5):  # Get 5 random numbers
        print(next(random_number_generator(1, 100)))
