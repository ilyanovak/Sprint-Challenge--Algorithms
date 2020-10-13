'''
Your function should take in a single parameter (a string `word`)
Your function should return a count of how many occurences of ***"th"*** occur within `word`. Case matters.
Your function must utilize recursion. It cannot contain any loops.
'''


def count_th(word):
    # For testing
    print(word)

    # If word is less than two characters long
    # Then return count = 0
    if len(word) < 2:
        return 0

    # If first two characters are 't' followed by 'h'
    # Then return count = 1 plus count_th with word string's succeeding characters after first two character
    if word[0] == 't' and word[1] == 'h':
        return 1 + count_th(word[2:])

    # Otherwise first two characters are NOT 't' followed by 'h'
    # Then return count = 0 plus count_th with word string's succeeding characters after first character
    else:
        return 0 + count_th(word[1:])
