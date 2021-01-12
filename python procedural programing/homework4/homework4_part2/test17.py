dict1 = [{ 'a': '1', 'b': '2' },{ 'a': '1', 'b': '2', 'c': '2'  },{ 'a': '1', 'b': '2', 'c': '2', 'd': '2'  },{ 'a': '1', 'b': '2' , 'c': '3', 'r':'3' }]

def switch_key_value(input_dict):
    dict_x_key = {}
    keys = []
    vals = []

    #print(input_dict)

    for key,val in input_dict.items():
        keys += val
        vals += key

    #print(keys,vals)
    dic = {}
    x = 0
    z =[]
    while x < len(input_dict) :

        y = x+1
        
        if y > len(keys)-1 :
            y =x
        
        if keys[x] != keys[y]:
            dic[keys[x]]=vals[x]
            #print('1')
        elif keys[x] == keys[y]:
            z.append(vals[x])
            #print('2')
            if len(z)<2:
                dic[keys[x]]=vals[x]
            else:
                dic[keys[x]]=z
            
        
        x +=1

    return dic
#for _ in dict1:
#    print(switch_key_value(_))

print(switch_key_value({ 'a': '1', 'b': '2' , 'c': '2', 'r':'3' }))
