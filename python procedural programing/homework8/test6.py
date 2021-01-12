# |“Picsart pipelines”                 	| “3.14csart 3.14pelines”
# |“picturespicturespictures”       	|“3.14ctures3.14ctures3.14ctures”

def pi_to_num(string, st=0):

    string = list(string)

    if len(string) <= st:
        return "".join(string)

    if string[st:2+st:] == ["p", "i"] or string[st:2+st:] == ["P", "i"] \
            or string[st:2+st:] == ["P", "I"] or string[st:2+st:] == ["p", "I"]:

        string[st:2+st:] = ["3", ".", "1", "4"]

    return pi_to_num(string, st+1)


print(pi_to_num("Picsart pipelines"))
print(pi_to_num("picturespicturespictures"))
