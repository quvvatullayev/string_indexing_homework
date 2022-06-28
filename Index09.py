def main(s):
    """
    a single character string is given. Convert it to int type, return -1 if not possible.
    Args:
        s(str): parameter
    Returns:
        int: answer
    """
    s = str(s)
    if s.isnumeric():
        return int(s)

    else:
        return -1

print(main("men1235df"))