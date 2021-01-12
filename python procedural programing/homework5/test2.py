import string 
num = {}
st = string.ascii_letters
#    for c in string.ascii_letters :
#        if index >26 :
#            break
#        num[c] = index
#        index +=1
#
num = {c:st.index(c)+1 for c in st if st.index(c)<26 }

print(num)