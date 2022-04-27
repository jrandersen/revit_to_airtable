# general overall algorithms and utility functions
import re
import collections
from fractions import Fraction

### concatenate and flatten a list of lists
# https://stackoverflow.com/questions/952914/how-to-make-a-flat-list-out-of-a-list-of-lists?page=2&tab=votes#tab-top
def listSmash (l):
    flatList = []
    flatList.extend ([l]) if (type (l) is not list) else [flatList.extend (listSmash (e)) for e in l]
    return flatList

def remove_duplicates(lst):
    return collections.OrderedDict(zip(lst, lst)).values()

def is_string_in_list(str, ls):
    #clean string
    str = string_preprocess(str)
    
    #look for string in list
    filter_object = filter(lambda a: str in a, ls)

    # Convert the filter object to list
    return list(filter_object)

def reduceFraction(x) : 
    reduced = Fraction(x).limit_denominator(100)
    return reduced




# Levenshtein Distance for comparisons
def string_preprocess(input):
    #preprocess the strings, take out white space, to all lower cae, take out ' & ".
    str1 = "".join(input.lower().split())
    s1 = re.sub("'", '', str1)
    s1 = re.sub("-", ' ', s1)
    s1 = re.sub("_", ' ', s1)
    s1 = re.sub('"', '', s1)
    return s1

def levenshtein_distance(str,text):  
    s1 = string_preprocess(str)
    s2 = string_preprocess(text)
    
    len1 = len(s1)+1
    len2 = len(s2)+1
    lt = [[0 for i2 in range(len2)] for i1 in range(len1)]  # lt - levenshtein_table
    lt[0] = list(range(len2))
    i = 0
    for l in lt:
        l[0] = i
        i += 1
    for i1 in range(1, len1):
        for i2 in range(1, len2):
            if s1[i1-1] == s2[i2-1]:
                v = 0
            else:
                v = 1
            lt[i1][i2] = min(lt[i1][i2-1]+1, lt[i1-1][i2]+1, lt[i1-1][i2-1]+v)
    return lt[-1][-1]