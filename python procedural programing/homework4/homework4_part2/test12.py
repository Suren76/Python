#import time
#start_time = time.time()
def sudoku_check(grid):

        ##########################   1
        h,h1,u,u1 = 3,0,3,0
        sum_3x3 =[]
        sum_3x3s =[]
        while h < 10:
                while u < 10:
                        for row in grid[h1:h]:
                                #print(row[u1:u:])
                                sum_3x3.append(sum(row[u1:u:]))
                        sum_3x3s.append(sum(sum_3x3[u1:u]))
                        u += 3
                        u1 += 3
                        #print("\n")
                h += 3
                h1 += 3
                u,u1 = 3,0
        #print(sum_3x3s)


        ##########################   2
        sum_row = []
        for row in grid:
                sum_row.append(sum(row))
        #print(sum_row)


        ##########################   3
        sum_col = 0
        sum_column = []
        index = 0
        while index < len(grid):
                for row in grid:
                        for column in str(row[index]):
                                sum_col +=int(column)
                sum_column.append(sum_col)
                sum_col = 0
                index +=1
        #print(sum_column)

        sums = []
        for _ in sum_3x3s :
                sums.append(_)
        for _ in sum_column :
                sums.append(_)
        for _ in sum_row :
                sums.append(_)
        #print(sums)

        true = 0
        for _ in sums:
                if _ == 45 :
                        true +=1
        if true == 27:
                return True 
        else :
                return False



###########################################################################
grid1 = [

        [1, 3, 2, 5, 4, 6, 9, 8, 7],
        [4, 6, 5, 8, 7, 9, 3, 2, 1],
        [7, 9, 8, 2, 1, 3, 6, 5, 4],
        [9, 2, 1, 4, 3, 5, 8, 7, 6],
        [3, 5, 4, 7, 6, 8, 2, 1, 9],
        [6, 8, 7, 1, 9, 2, 5, 4, 3],
        [5, 7, 6, 9, 8, 1, 4, 3, 2],
        [2, 4, 3, 6, 5, 7, 1, 9, 8],
        [8, 1, 9, 3, 2, 4, 7, 6, 5]
        
        ],[
        
        [1, 3, 2, 5, 4, 6, 9, 2, 7],
        [4, 6, 5, 8, 7, 9, 3, 8, 1],
        [7, 9, 8, 2, 1, 3, 6, 5, 4],
        [9, 2, 1, 4, 3, 5, 8, 7, 6],
        [3, 5, 4, 7, 6, 8, 2, 1, 9],
        [6, 8, 7, 1, 9, 2, 5, 4, 3],
        [5, 7, 6, 9, 8, 1, 4, 3, 2],
        [2, 4, 3, 6, 5, 7, 1, 9, 8],
        [8, 1, 9, 3, 2, 4, 7, 6, 5]
        
        ]
for _ in grid1:
        print(sudoku_check(_))
#print("\n"*3)
#print("--- %s seconds ---" % (time.time() - start_time))