sentences = ["The Hubble Space telescope has spotted", 
             "a formation of galaxies that resembles", 
             "a smiling face in the sky"]
st_index = []
#for chr1 in sentences:
#    for chr2 in chr1.split(' '):
#        st_index.append((chr2,sentences.index(chr1)))
st_index = [(chr2,sentences.index(chr1)) for chr1 in sentences for chr2 in chr1.split(' ')]
print(st_index)
