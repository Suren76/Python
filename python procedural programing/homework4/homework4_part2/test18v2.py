books_list = [

	{ "book": "Catcher in the Rye", "readStatus": True, "percent": 40},
	{ "book": "Animal Farm", "readStatus": True, "percent": 20},
	{ "book": "Solaris", "readStatus": False, "percent": 90 },
	{ "book": "The Fall", "readStatus": True, "percent": 50 },
	{ "book": "White Nights", "readStatus": False, "percent": 60 } ,
	{ "book": "After Dark", "readStatus": True, "percent": 70 }
]
def sort_by_readS_percent(books_list):
	################################     1 

	books_list_read =[]
	books_list_noread =[]
	for books_read_status in books_list:
		if books_read_status['readStatus']==True:
			books_list_read.append(dict(books_read_status))
		else:
			books_list_noread.append(dict(books_read_status))
	#print(books_list_read)
	#print("\n")
	#print(books_list_noread)
	#print("\n")



	###########################       2
	def books_list_sort(books_list):
		x = 0
		max_percent = []
		z = []

		for _ in books_list:
			max_percent.append(_['percent'])
			x +=1


		x = 0
		while x < len(max_percent):
			if max_percent[x] ==max(max_percent):	
				z.append(books_list[x])
				#print(max_percent,max_percent[x])
				del max_percent[x] ,books_list[x]
				x = 0
				continue
			x +=1
		return z

	return {"read":books_list_sort(books_list_read)}

print(sort_by_readS_percent(books_list))