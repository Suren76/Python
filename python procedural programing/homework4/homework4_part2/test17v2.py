dict1 = [{ 'a': '1', 'b': '2' },{ 'a': '1', 'b': '2', 'c': '2'  },{ 'a': '1', 'b': '2', 'c': '2', 'd': '2'  },{ 'a': '1', 'b': '2' , 'c': '3', 'r':'3' },{ 'a': '1', 'b': '2' , 'c': '2', 'r':'1' }]

def switch_key_value(input_dict):
    dict_x_key = {}
    keys = []
    

    #print(input_dict)

    for key,val in input_dict.items():
        keys += val
        
    

    #print(keys)
    dic = {}
    x = 0
    
    
    for i in set(keys):
        z = []
        for val,k in input_dict.items():
            if k == i:
                z.append(val)

        if len(z)==1:
            dic[i] = "".join(z)
        elif len(z)>1:
            dic[i] = z 
        

    return dic
for _ in dict1:
    print(switch_key_value(_))

