import math

def initArrays():
    with open('on2bestcase.txt') as file_bc:
        bestCaseArray = []
        for line in file_bc:
            bestCaseArray.append(int(line))
        
    with open('on2worstcase.txt') as file_wc:
        worstCaseArray = []
        for line in file_wc:
            worstCaseArray.append(int(line))

    with open('on2avgcase.txt') as file_ac:
        avgCaseArray = []
        for line in file_ac:
            avgCaseArray.append(int(line))
            
    with open('reverse1000.txt') as file_r1000:
        reverse1000 = []
        for line in file_r1000:
            reverse1000.append(int(line))
            
    with open('sorted1000.txt') as file_s1000:
        sorted1000 = []
        for line in file_s1000:
            sorted1000.append(int(line))
            
    with open('random1000.txt') as file_rn1000:
        random1000 = []
        for line in file_rn1000:
            random1000.append(int(line))
            
    with open('randomorg300.txt') as file_ro300:
        ro300 = []
        for line in file_ro300:
            ro300.append(int(line))
            
    with open('random300skewed.txt') as file_r300s:
        r300s = []
        for line in file_r300s:
            r300s.append(int(line))
            
    with open('random300dist.txt') as file_r300d:
        r300d = []
        for line in file_r300d:
            r300d.append(int(line))
            
    return bestCaseArray, worstCaseArray, avgCaseArray, reverse1000, sorted1000, random1000, ro300, r300s, r300d

def ranges_init(len):
    i = 0
    arr = []
    while (i < len):
        arr.append(i)
        i += 1
    return arr
    

def test_cases_init(size):
    dataArrays = initArrays()

    ranges = ranges_init(size)
    presort = []
    reverse = []
    random = []
    r1000 = []
    r300s = []
    r300d = []
    s1000 = []
    rv1000 = []
    
    for r in ranges:
        i = 0
        presort_arr = []
        reverse_arr = []
        random_arr = []
        r1000_arr = []
        r300s_arr = []
        r300d_arr = []
        s1000_arr = []
        rv1000_arr = []
        while (i < r):
            presort_arr.append(dataArrays[0][i])
            reverse_arr.append(dataArrays[1][i])
            random_arr.append(dataArrays[2][i])
            r1000_arr.append(dataArrays[5][i])
            r300s_arr.append(dataArrays[7][i])
            r300d_arr.append(dataArrays[8][i])
            s1000_arr.append(dataArrays[4][i])
            rv1000_arr.append(dataArrays[3][i])
            i += 1
            
        presort.append(presort_arr)
        reverse.append(reverse_arr)
        random.append(random_arr)
        r1000.append(r1000_arr)
        r300s.append(r300s_arr)
        r300d.append(r300d_arr)
        s1000.append(s1000_arr)
        rv1000.append(rv1000_arr)
    
    return presort, reverse, random, r1000, r300s, r300d, s1000, rv1000

'''O(n^2) Algorithms'''
def selection_sort(data):
    count = 0
    for index in range(len(data)):
        min = index
        
        for scan in range(index + 1, len(data)):
            count += 1
            if (data[scan] < data[min]):
                min = scan
        if min != index:
            data[index], data[min] = data[min], data[index]
    return count, data

def insertion_sort(data):
    count = 0
    for index in range(1, len(data)):
        # count += 1
        while 0 < index and data[index] < data[index - 1]:
            count += 1
            data[index], data[
                index - 1] = data[index - 1], data[index]
            index -= 1

    return count, data

def bubble_sort(data):
    count = 0
    while True:
        swapped = False
        for index in range(1, len(data)):
            count += 1
            if data[index-1] > data[index]:
                data[index-1], data[index] = data[index], data[index-1]
                swapped = True
        if not swapped:
            break
    return count, data

def get_unsortedness(data):
    counter = 0
    comparisons = 0
    for index in range(1, len(data)):
        counter+=1
        while 0 < index and data[index] < data[index - 1]:
            counter += 1
            index -= 1

    return counter

''' Shell sort with insertion sort subroutine '''
def shell_sort(data, gapSequence):
    unsortedness = []
    comparisons = []
    comparisonSumSS = 0
    swapSumSS = 0
   
    for gap in gapSequence:
        unsortedness.append(get_unsortedness(data))
        comparisons.append(comparisonSumSS)
        
        # Subroutine call
        insertionSortResult = insertion_subroutine(data, gap)
        comparisonSumSS = comparisonSumSS + insertionSortResult[1]
        swapSumSS = swapSumSS + insertionSortResult[2]
    
    comparisons.append(comparisonSumSS)
    unsortedness.append(0)
        
    return data, comparisonSumSS, swapSumSS, unsortedness, comparisons

def insertion_subroutine(data, gap):
    comparisons = 0
    comparisonSumIS = 0
    
    swaps = 0
    swapSumIS = 0
    
    for index in range(gap, len(data)):
        comparisons = 0
        swaps = 0
        
        while 0 < index and data[index] < data[index - gap]:
            comparisons += 1
            # Do the swap!
            data[index], data[
                index - gap] = data[index - gap], data[index]
            swaps += 1
            index -= gap
            
        comparisons += 1
        comparisonSumIS += comparisons
        
        swapSumIS += swaps
       
    return data, comparisonSumIS, swapSumIS

''' Getting Shell's gap sequence '''
def shell_gap_seq(dataLength):
    gap = dataLength
    gapSequence = []
    i = 100

    while gap > 1:
        gap = math.floor(gap // 2)
        gapSequence.append(gap)
        
    return gapSequence

''' Getting Ciura's gap sequence '''
def ciura_gap_seq(dataLength):
    ciuraSeq = [701, 301, 132, 57, 23, 10, 4, 1]
    gapSequence = []
    
    for gap in ciuraSeq:
        if gap < dataLength:
            gapSequence.append(gap)
            
    return gapSequence

''' Bucket Sort '''
def bucket_sort(data, bucketSize):
    biggest = 0
    comparisonSumBS = 0
    sorted = []
    
    for number in data:
        if number > biggest:
            biggest = number
    buckets = []
    
    for i in range ((int(biggest / bucketSize + 1))):
        buckets.append([])
        
    for number in data:
        buckets[int(number / bucketSize)].append(number)
        
    for index, bucket in enumerate(buckets):
        insertionSortResult = insertion_subroutine(bucket, 1)
        buckets[index] = insertionSortResult[0]
        
        comparisonSumBS += int(insertionSortResult[1])
        sorted.extend(buckets[index])
    
    return sorted, comparisonSumBS, buckets

''' Radix Sort with Counting Sort subroutine '''
def radix_sort_cs(data):
    accessSum = 0
    max_radix = max(data)
    
    accessSum = 0
 
    exp = 1
    while max_radix/exp > 0:
        cs = counting_sort(data,exp)
        accessSum += counting_sort(data,exp)[1]
        exp *= 10
        
    return data, accessSum

def counting_sort(data, exp):
    access = 0
    n = len(data)
    
    output = [0] * (n)
 
    count = [0] * (10)
 
    for i in range(0, n):
        index = (data[i]/exp)
        count[ int((index)%10) ] += 1
 
    for i in range(1,10):
        count[i] += count[i-1]
 
    i = n-1
    while i>=0:
        index = (data[i]/exp)
        output[ count[ int((index)%10) ] - 1] = data[i]
        count[ int((index)%10) ] -= 1
        i -= 1
 
    i = 0
    for i in range(0,len(data)):
        data[i] = output[i]
        access += 1
    
    return data, access

''' Radix sort with insertion sort subroutine '''
def radix_sort_is(array, radix):
    accessSum = 0
    if len(array) == 0:
        return array
    
    minValue = min(array)
    maxValue = max(array)

    # lsd
    exponent = 1
    while (maxValue - minValue) / exponent >= 1:
        accessSum += insertion_subroutine_radix(array, 1, exponent, radix)
        
        exponent *= radix

    return array, accessSum

def insertion_subroutine_radix(array, gap, exp, radix):
    accesses = 0
    comparisons = 0
    for i in range(gap, len(array)):
        comparisons += 1
        accesses += 1
        val = array[i]
        j = i
        while j >= gap and array[j - gap] / exp % radix > val  / exp % radix:
            array[j] = array[j - gap]
            j -= gap
            comparisons += 1
            accesses += 1
        array[j] = val

    return accesses

''' Merge Sort '''
def merge_sort(data):
    comparisons = 0

    if len(data)>1:
        intMidValue = len(data)//2
        listLeftHalf = data[:intMidValue]
        listRightHalf = data[intMidValue:]

        left_part = merge_sort(listLeftHalf)
        right_part = merge_sort(listRightHalf)

        comparisons += left_part[1] + right_part[1]

        i=0
        j=0
        k=0
        while i < len(listLeftHalf) and j < len(listRightHalf):
            comparisons += 1
            if listLeftHalf[i] < listRightHalf[j]:
                data[k]=listLeftHalf[i]
                i =i+1

            else:
                data[k]=listRightHalf[j]
                j=j+1

            k=k+1

        while i < len(listLeftHalf):
            data[k]=listLeftHalf[i]
            i=i+1
            k=k+1
            comparisons += 1

        while j < len(listRightHalf):
            data[k]=listRightHalf[j]
            j=j+1
            k=k+1
            comparisons += 1

    return data, comparisons

''' Quick Sort '''
def partition(data, start, end):
    comparisonSum = 0
    pos = start
    for i in range(start, end):
        comparisonSum += 1
        if data[i] < data[end]:
            data[i], data[pos] = data[pos], data[i]
            pos += 1
    data[pos], data[end] = data[end], data[pos]
    return pos, comparisonSum

def quick_sort_helper(data, start, end):
    comparisonSum = 0
    if start < end:
        pos, comparisonSum = partition(data, start, end)        
        comparisonSum += quick_sort_helper(data, start, pos - 1)
        comparisonSum += quick_sort_helper(data, pos + 1, end)
    return comparisonSum

def quick_sort(data, start, end):
    if start is None:
        start = 0
    if end is None:
        end = len(data) - 1
    return quick_sort_helper(data, start, end)