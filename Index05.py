from multiprocessing import managers


def main(s):
    """
    Given a variable s string of length five. Determine the number of digits involved in this variable.
    Args:
        s(str): parameter
    Returns:
        int: answer
    """
    answer = 0
    if s[0].isdigit():
        answer += 1
    else:
        0
    if s[1].isdigit():
        answer += 1

    else:
        0
    if s[2].isdigit():
        answer += 1

    else:
        0

    if s[3].isdigit():
        answer += 1

    else: 
        0

    if s[4].isdigit():
        answer += 1

    else:
        0

    return answer

print(main("ogabe"))