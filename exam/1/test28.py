def chessBoardCellColor(cell1, cell2):
    
    return True if bool((abs(ord(cell1[0]) - ord(cell2[0])))%2 == 0) == bool((abs(abs(int(cell1[1]) - int(cell2[1]))))%2 == 0)  else False

print(chessBoardCellColor("A3","C1"))