from cgi import print_environ


def main(s):
    """
    A string of length five is given. Return the index of the "*" character, return False if not present.
    Args:
        s(str): parameter
    Returns:
        int: answer
    """
    s = str(s)
    if int(s.index("*")) >= 0:
        return s.index("*")

    else:
        return False


print(main("Ogabe*"))