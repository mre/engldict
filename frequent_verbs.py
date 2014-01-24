"""
Find most frequent irregular verbs from Google word corpus and a list of
irregular verbs from ego4u.com
"""

import csv, codecs

with open('irregular-verbs-de.csv') as verbs:
    reader = csv.reader(verbs)
    verbs = {verb[0]: verb[1:] for verb in reader}


with open('google-10000-english.txt') as words:
    for word in words.read().split("\n"):
        if word in verbs.keys():
            print(",".join([word] + verbs[word]))
