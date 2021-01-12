def variableName(name):
    
    import string as st
    for char in name:
        if char not in (st.ascii_letters+st.digits+"_") or name[0] not in (st.ascii_letters+"_"): 
            return False
    
    return True

print(variableName("hgg_-1"))