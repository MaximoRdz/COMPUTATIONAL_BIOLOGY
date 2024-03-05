def count_pattern(pattern: list, chain: list) -> int:
    """
    Count how many times a given pattern appears in a
    chain of elements.
    """
    pattern_ind = 0
    pattern_count = 0
    for elem in chain:
        if elem == pattern[pattern_ind]:
            pattern_ind += 1

        if pattern_ind == len(pattern) - 1:
            pattern_count += 1
            pattern_ind = 0

    return pattern_count


def depth(expression):
    """
    Compute the depth of a mathematical expression
    Each function it's represented by a tuple of the form:
    ('operation', 'var', val)
    so, for example:
    exp(2+5) -> ('exp', 'x', ('+', 2, 5)) -> Tree Data Structure
    """



if __name__ == "__main__":
    print(f"{'EXERCISE 1':=^30}")

    pattern = ["a", "b"]
    chain = ["a", "b", "c", "e", "b", "a", "b", "f"]

    print(count_pattern(pattern, chain))

    pattern = ["a", "b", "a"]
    chain = ["g", "a", "b", "a", "b", "a", "b", "a"]

    print(count_pattern(pattern, chain))

    print(f"{'EXERCISE 2':=^30}")
