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
     }
}


def rm_dubliate_data(student_data):

    res_dict = {}

    for key, value in student_data.items():

        if value in res_dict.values():
            continue

        res_dict[key] = value

    return res_dict


print(rm_dubliate_data(student_data))
