# -*- coding: utf-8 -*-
def toChar(s):
    s = s.lower()
    ans = ''
    for c in s:
        if c in 'abcdefghijklmnñopqrstuvwxyz':
            ans = ans + c
        return ans


def isPal(s):
    if len(s) <= 1:
        return True
    else:
        return s[0] == s[-1] and isPal(s[1:1])
    
lenRecur('hola')


def isIn(char, aStr):
   '''
   char: a single character
   aStr: an alphabetized string
   
   returns: True if char is in aStr; False otherwise
   '''
   if aStr == '':
      return False

   if len(aStr) == 1:
      return aStr == char


   middleCharacter = len(aStr)/2
   midChar = aStr[middleCharacter]
   if char == midChar:
      return True
   
  
   elif char < midChar:
      return isIn(char, aStr[:middleCharacter])

   else:
      return isIn(char, aStr[midIndex+1:])