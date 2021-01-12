picture = ["abc",
           "ded"]

def addBorder(picture):
    if type(picture) == list and 1<=len(picture)<=100 and picture != []:
        return [((len(picture[0])+2)*"*")]+[("".join(['*']+list(txt)+['*'])) for txt in picture if type(txt) == str and 1<=len(txt)<=100 and txt != '']+[((len(picture[0])+2)*"*")]

print(addBorder(picture))
