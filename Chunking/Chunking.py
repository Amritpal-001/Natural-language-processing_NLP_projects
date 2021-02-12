#Sentdex
#https://pythonprogramming.net/chunking-nltk-tutorial/


import nltk
from nltk.corpus import state_union
from nltk.tokenize import PunktSentenceTokenizer


path = 'Textdata/'
filepath = 'Textdata\Covid-wikipedia-Intro.txt'
train_text =''
with open( 'Textdata\Covid-wikipedia-Intro.txt' , 'r') as f:
    for a in f:
        train_text += a
#print(type(b) , len(b))

#train_text = state_union.raw(filepath)

sample_text =''
with open( 'Textdata/DeepLearningWikipedia-Intro.txt', 'r') as f:
    for a in f:
        sample_text += a

#sample_text = state_union.raw("2006-GWBush.txt")

custom_sent_tokenizer = PunktSentenceTokenizer(train_text)
tokenized = custom_sent_tokenizer.tokenize(sample_text)

def process_content():
    try:
        for i in tokenized:
            words = nltk.word_tokenize(i)
            tagged = nltk.pos_tag(words)
            chunkGram = r"""Chunk: {<RB.?>*<VB.?>*<NNP>+<NN>?}"""
            chunkParser = nltk.RegexpParser(chunkGram)
            chunked = chunkParser.parse(tagged)
            #chunked.draw()

    except Exception as e:
        print(str(e))
    return(chunked)

Chunkeddata = process_content()

print(len(Chunkeddata))

