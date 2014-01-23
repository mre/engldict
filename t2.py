

from string import punctuation
 
def unique_words(sentence):
    return set(sentence.translate(None, punctuation).lower().split())
 
s1 = unique_words("Hello, my Name is jim")
s1 = s1.union(unique_words("Her list of wishes is as long as your arm."))


print s1
