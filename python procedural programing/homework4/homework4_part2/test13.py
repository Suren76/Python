num = int(input("enter the size of the list  :")) 
def p_spiral(): 
    def spiral(n):
        def go(rows, cols, x):
            return [list(range(x, x + cols))] + [
                list(reversed(x)) for x
                in zip(*go(cols, rows - 1, x + cols))
            ] if 0 < rows else []
        return go(n, n, 1)

    a = spiral(num)
    for x in a:
        print(x)

p_spiral()
