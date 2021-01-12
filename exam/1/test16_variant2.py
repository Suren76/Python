def arrayChange(inputArray):
    step = 0

    for i in range(len(inputArray)):
        
        if i == len(inputArray)-1:
            return step

        print(i)
    
        a = inputArray[i+1]-inputArray[i]

        if a < 1 :

            while inputArray[i+1]-inputArray[i] < 1:
                print(inputArray)
                inputArray[i+1] +=1
                step +=1

        if a > 1:

            while inputArray[i+1]-inputArray[i] > 1:
                print(inputArray)
                inputArray[i+1] -=1
                step +=1

        if inputArray[i+1]-inputArray[i] == 1:
            print(inputArray)
            step +=1