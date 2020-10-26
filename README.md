engldict
========

Language learning is hard. Especially because words can have ambiguous meanings.
One solution might be to learn a word only in the context of an example sentence.

This program will be a bit similar to [GnuVocabTrain](http://de.wikipedia.org/wiki/GnuVocabTrain), but it will be open source
and work on all platforms.
Basically, you have English sentences and their German translations randomly
arranged on the screen. One word in the English sentence is marked and you
have to select the correct translation. Once the player made a correct choice,
the word will be asked less frequently in the future.

Featuring the [most common english words project](https://github.com/first20hours/google-10000-english) by [first20hours](https://github.com/first20hours).

I needed a good API to query example sentences for words.
The first thing that came to mind was Wiktionary, but the API was horrendous.
Therefore I wrote a scraper for [Vocaboly](http://www.vokaboly.de/bs/index.php) to get example sentences.
I realize there are many other web resources for English example sentences but
most of them lack the German translation.
