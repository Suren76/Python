student_data = {
 'id1': 
   {'name': ['Sara'], 
    'class': ['V'], 
    'subject_integration': ['english, math, science']
   },
 'id2': 
  {'name': ['David'], 
    'class': ['V'], 
    'subject_integration': ['english, math, science']
   },
 'id3': 
    {'name': ['Sara'], 
    'class': ['V'], 
    'subject_integration': ['english, math, science']
   },
 'id4': 
   {'name': ['Surya'], 
    'class': ['V'], 
    'subject_integration': ['english, math, science']
   },
}
def rm_dubliate_data(student_data):
    name = []
    clas = []
    subject_integration = []
    for x,y in student_data.items():
        vals = y.values()
        keys = list(y.keys())
        name += list(vals)[0]
        clas += list(vals)[1]
        subject_integration += list(vals)[2]
    name = set(name)
    clas = set(clas)
    subject_integration = set(subject_integration)
    #print(keys)
    #print( name,clas,subject_integration)
    vals = [name,clas,subject_integration]
    x = 0
    student_data={}
    while x<len(keys):
        student_data[keys[x]]=vals[x]
        x +=1
    return student_data

print(rm_dubliate_data(student_data))
