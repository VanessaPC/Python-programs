import string
def buildCoder(shift):
    """
    Returns a dict that can apply a Caesar cipher to a letter.
    The cipher is defined by the shift value. Ignores non-letter characters
    like punctuation, numbers, and spaces.

    shift: 0 <= int < 26
    returns: dict
    """
    dict = {}
    for chr in string.ascii_lowercase:
        val = ord(chr)
        dict = chr(val+shift)
        dict[chr] = next
        
    print dict
buildCoder(3)