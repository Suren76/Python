chess = [([(h,u) if h > 0 and h < 7 and u > 0 and u < 7 else ('---') for h in range(8)])  for u in range(8)]
# Վիդեոից պրինտն եմ վերցրել
for it_chess in chess:    
    print(it_chess)