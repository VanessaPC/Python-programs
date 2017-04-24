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
    for char in string.ascii_lowercase:
        try: 
            val = ord(char)
            next = chr(val+shift)
            dict[char] = next
        except:
            val = ' '
            val = string.punctuation
            val = string.digits
            val = '{'
        
    print dict
    
buildCoder(3)