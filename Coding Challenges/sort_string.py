"""This function takes a series of words as an argument and returns them in a sorted order"""
def sortString(input):
    # This implementation splits the input and sorts it with the modifier to ignore the case and then joins them back together with a space inbetween.
    return ' '.join(sorted(input.split(), key=str.casefold))


print(sortString("This is not sorted"))   