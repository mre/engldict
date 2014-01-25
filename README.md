engldict
========

Language learning is hard. Especially because words can have ambiguous meanings.
One solution might be to learn a word only in the context of an example sentence.

This program will be a bit similar to [GnuVocabTrain](http://de.wikipedia.org/wiki/GnuVocabTrain), but it will be open source
and work on all platforms.
Basically, you have english sentences and their german translations randomly
arranged on the screen. One word in the english sentence is marked and you
should select the correct translation. If the player made a correct selection,
the word will be asked less frequent in the future.

Featuring the [most common english words project](https://github.com/first20hours/google-10000-english) by [first20hours](https://github.com/first20hours).


I needed a good API to query example sentences for words.
The first thing that came to mind was Wiktionary, but the API was horrendous.
Therefore I wrote a scraper for [Vocaboly](http://www.vokaboly.de/bs/index.php) to get example sentences.
I realize there are many other web resources for english example sentences but
most of them lack the German translation.
