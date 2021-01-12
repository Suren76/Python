N = int(input())

def num_num(N):
    dict_res = {}
    for n in range(1,N+1):
        dict_res[n]=int(n*n)
    return dict_res

print(num_num(N))