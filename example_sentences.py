import urllib2
#from BeautifulSoup import BeautifulSoup
# or if you're using BeautifulSoup4:
from bs4 import BeautifulSoup
import json


test_html_doc = """
<html>
<head>
<title>Beispiels&auml;tze-Datenbank Englisch Deutsch</title>
</head>
<body bgcolor="#FFFFFF" text="#000000" onLoad=setFocus()>
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

vocab = {}
#for word in open("0-1000.txt").read().split():
word = "hi"
if len(word) < 3:
  word = word.ljust(3, "+")

try:
  #soup = BeautifulSoup(html_doc)
  soup = BeautifulSoup(urllib2.urlopen('http://www.vokaboly.de/bs/index.php?q=as+&submit=Suchen&lang=en').read())
  content = soup('table')[1]
  rows = content.find_all('tr')[1:]
  for row in rows:
    english_tag, german_tag = row.find_all('font')[:2]
    en = ''.join(english_tag.findAll(text=True))
    de = ''.join(german_tag.findAll(text=True))
    vocab[word] = (en, de)
except Exception, e:
  print e
print json.dumps(vocab)
