sentences = ["The Hubble Space telescope has spotted", 
             "a formation of galaxies that resembles", 
             "a smiling face in the sky", 
             "The image taken with the Wide Field Camera", 
             "shows a patch of space filled with galaxies", 
             "of all shapes, colours and sizes"]

stopwords = ['for', 'a', 'of', 'the', 'and', 'to', 'in', 'on', 'with']



#for char1 in sentences :
#    char1 = char1.split()
#    #print(char1)
#    for char in char1:
#        for x in stopwords:
#            if x == char:
#                char1.remove(char)
#    sentences_stw.append(char1)
def filter_by_word(sentences,skip_words):
    sentences_stw = []
    for char1 in sentences :
        char1 = char1.split()

        [char1.remove(char)  for x in skip_words for char in char1 if x == char]
        sentences_stw += [char1]
    return sentences_stw
print(filter_by_word(sentences,stopwords))
