from time import sleep
from tqdm import tqdm


def ft_tqdm(numbers):
    """
    Decorate an iterable object, returning an iterator which acts exactly
    like the original iterable, but prints a dynamically updating
    progressbar every time a value is requested.
    """
    total = len(numbers)
    for i, elem in enumerate(numbers):
        percent = round(i / total * 100)
        bar = "█" * percent
        bar += " " * (100 - percent)
        print(f"\r{percent}%|{bar}|", end="")
        yield elem


for elem in ft_tqdm(range(333)):
    sleep(0.005)
print()

for elem in tqdm(range(333)):
    sleep(0.005)
print()