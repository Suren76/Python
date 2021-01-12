a = input()
if a[-2:]==':p':
    print("<p>"+a[:-2] +"</p>")
elif a[-3:-1]==':h':
    x = a[-1:]
    print("<h"+x+">"+ a[:-3] +"</h"+x+">")
elif a[-6:]==':title':
    print("<title>"+a[:-6] +"</title>")

#Չէի տեսել պահանջի ներքևում գրածը , ուղարկելուց նկատեցի։

a = input("input tag: ")
a1 = input("input word: ")
def add_tags(tag, word):
	return "<%s>%s</%s>" % (tag, word, tag)
b = add_tags(a,a1)

print(b)
