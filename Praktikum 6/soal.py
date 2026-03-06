def insertionSort(data):

    for index in range(1,len(data)):
        currentvalue = data[index]
        position = index
        
        while position>0 and data[position-1]<currentvalue:
            data[position]=data[position-1]
            position = position-1
        data[position]=currentvalue
    
data = [43, 76, 12, 89, 33, 57, 98, 22, 68, 9]
insertionSort(data)

#Kandidat dengan nilai tertinggii adalah kandidat ke 7, 4, 2, 9, 6 




