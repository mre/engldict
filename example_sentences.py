"""
Finds example sentences for the n most common english words.
By default it uses the http://www.vokaboly.de/bs corpus.
"""

import urllib2
#from BeautifulSoup import BeautifulSoup
# or if you're using BeautifulSoup4:
from bs4 import BeautifulSoup
from string import punctuation



test_html_doc = """
<html>
<head>
<title>Beispiels&auml;tze-Datenbank Englisch Deutsch</title>
</head>
<body bgcolor="#FFFFFF" text="#000000" onLoad=setFocus()>
<table></table>
<table width=100% border=1 align=center  bordercolor=#a6bddc>
<tr><td><div align=center><b><font size=-1>Englisch<font></b></div></td><td><div align=center><b><font size=-1>Deutsch<font></b></div></td></tr>
<tr><td><font size=-1>Her list of wishes is <b>as </b>long as your arm.</font></td><td><font size=-1>Ihr Wunschzettel ist ellenlang.<font></td></tr>
<tr><td><font size=-1>The work is not <b>as </b>difficult as you imagine.</font></td><td><font size=-1>Die Arbeit ist nicht so schwer, wie du dir vorstellst.<font></td></tr>
<tr><td><font size=-1><b>As </b>she left the room she remembered the book.</font></td><td><font size=-1>Als sie aus dem Zimmer ging, fiel ihr das Buch wieder ein.<font></td></tr>
<tr><td><font size=-1>I'm just <b>as </b>clever as you.</font></td><td><font size=-1>Ich bin genauso klug wie du.<font></td></tr>
<tr><td><font size=-1>His greatness <b>as </b>a writer is unquestioned.</font></td><td><font size=-1>Seine Bedeutung als Schriftsteller ist unbestritten.<font></td></tr>
<tr><td><font size=-1>I can offer my land <b>as </b>a guarantee.</font></td><td><font size=-1>Ich kann mein Land als Garantie anbieten.<font></td></tr>
</table>
</body>
</html>
"""

def unique_words(sentence):
    """
    From Artem Rudenko's Blog
    http://artemrudenko.wordpress.com/2013/04/17/python-getting-unique-words-from-text/
    """
    print sentence
    return set(sentence.translate(None, punctuation).lower().split())

word_corpus = set()
sentence_corpus = [] #

# Get example sentences for the n most common english words
for word in open("20.txt").read().split():
  if word in word_corpus:
    # We already have an example sentence for this word.
    continue

  # The API requires padding for short words.
  print "Looking up '{word}'...".format(word=word)
  if len(word) < 3:
    word = word.center(3, "+")

  # Make an API call and extract all example sentences.
  try:
    soup = BeautifulSoup(test_html_doc)
    #url = 'http://www.vokaboly.de/bs/index.php?q={}&submit=Suchen&lang=en'.format(word)
    #soup = BeautifulSoup(urllib2.urlopen(url).read())
    content = soup('table')[1]
    rows = content.find_all('tr')[1:]
    for row in rows:
      english_tag, german_tag = row.find_all('font')[:2]
      en = ''.join(english_tag.findAll(text=True))
      de = ''.join(german_tag.findAll(text=True))
      word_corpus = word_corpus.union(unique_words(en))
      sentence_corpus.append((en, de))
  except Exception, e:
    print e

print ", ".join(word_corpus)
print
#print sentence_corpus
