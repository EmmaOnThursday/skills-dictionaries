"""Advanced skills-dictionaries.

  IMPORTANT: these problems are meant to be solved using dictionaries and sets.
"""


def top_characters(input_string):
    """Find most common character(s) in string.

    Given an input string, return a list of character(s) which
    appear(s) the most the input string.

    If there is a tie, the order of the characters in the returned
    list should be alphabetical.

    For example:

        >>> top_characters("The rain in spain stays mainly in the plain.")
        ['i', 'n']

    If there is not a tie, simply return a list with one item.

    For example:

        >>> top_characters("Shake it off, shake it off. Shake it off, Shake it off.")
        ['f']

    Do not count spaces, but count all other characters.

    """
    
    # instantiate empty dictionary
    char_counts = {}

    # for each characater, add char: count as k/v pair
    # if character is already in dict as a key, +1 to its value
    for x in input_string:
        if char_counts.get(x, 0) == 0:
            char_counts[x] = 1
        else:
            char_counts[x] += 1    
    
    # zero out count for spaces
    char_counts[" "] = 0

    # create list of counts; return max value
    just_counts = [x for x in char_counts.values()]
    highest_count = max(just_counts)

    # for each k/v pair in dict, return key if value equals highest_count
    most_common_letters = [x[0] for x in char_counts.iteritems() if x[1] == highest_count]

    return sorted(most_common_letters)

# print statement with example string; for debugging
# print top_characters("the quick brown fox jumps over jjjj")


def adv_alpha_sort_by_word_length(words):
    """Return list of word-lengths and words.

    Given a list of words, return a list of tuples, ordered by word-length.
    Each tuple should have two items--a number that is a word-length,
    and the list of words of that word length. In addition to ordering
    the list by word length, order each sub-list of words alphabetically.

    For example:

        >>> adv_alpha_sort_by_word_length(["ok", "an", "apple", "a", "day"])
        [(1, ['a']), (2, ['an', 'ok']), (3, ['day']), (5, ['apple'])]

    """
    # instantiate empty word dictionary; count each word
    word_dictionary = {}
    for x in words:
        if word_dictionary.get(word, 0) == 0:
            word_dictionary[word] = 1
        else:
            word_dictionary[word] += 1  

    new_dict = {}

    # take each item: (word, #)
    for pair in range(len(word_dictionary.iteritems())):
        # if new_dict has # already: append word
        # if not: make #, append word
        if new_dict.get(pair[1], 0) == 0:
            new_dict[pair[1]] = [pair[0]]
        else:
            new_dict[pair[1]].append(pair[0])

    print new_dict



    # return []

adv_alpha_sort_by_word_length(["ok", "an", "apple", "a", "day"])
##############################################################################
# You can ignore everything below this.


# if __name__ == "__main__":
#     print
#     import doctest
#     if doctest.testmod().failed == 0:
#         print "*** ALL TESTS PASSED ***"
#     print
