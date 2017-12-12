from Algorithms import initArrays, ranges_init, test_cases_init, selection_sort, insertion_sort, bubble_sort, get_unsortedness, shell_sort, insertion_subroutine, shell_gap_seq, ciura_gap_seq, bucket_sort, radix_sort_cs, counting_sort, radix_sort_is, insertion_subroutine_radix, merge_sort, partition, quick_sort_helper, quick_sort

import matplotlib.pyplot as plt

''' O(n^2) line graph '''
def on2_eval():
    x_values = ranges_init(300)
  
    ''' PRESORTED SEQUENCES '''
    
    presorted_ss = test_cases_init(300)[0]
    presorted_is = test_cases_init(300)[0]
    presorted_bs = test_cases_init(300)[0]
    
    selection_y_values = []
    insertion_y_values = []
    bubble_y_values = []
    
    for case in presorted_ss:
        # result = shell_sort_shell(case, shell_gap_seq(len(case)))
        result = selection_sort(case)
        selection_y_values.append(result[0])
    plt.plot(x_values, selection_y_values, linewidth=3.0)
    
    for case in presorted_is:
        result = insertion_sort(case)
        insertion_y_values.append(result[0])
    plt.plot(x_values, insertion_y_values)
    
    for case in presorted_bs:
        # result = shell_sort_shell(case, shell_gap_seq(len(case)))
        result = bubble_sort(case)
        bubble_y_values.append(result[0])
        
    plt.plot(x_values, bubble_y_values)
    
    plt.title("Sorted Sequences")
    
    plt.xlabel('Dataset Size')
    plt.ylabel('Comparisons')
    
    plt.legend(['Selection Sort','Insertion sort', 'Bubble Sort'], loc='upper left')
    plt.show()
    
    
    ''' REVERSE SORTED SEQUENCES '''
    
    reversedsorted_ss = test_cases_init(300)[1]
    reversedsorted_is = test_cases_init(300)[1]
    reversedsorted_bs = test_cases_init(300)[1]
    
    selection_y_values = []
    insertion_y_values = []
    bubble_y_values = []
    
    for case in reversedsorted_ss:
        result = selection_sort(case)
        selection_y_values.append(result[0])
       
    plt.plot(x_values, selection_y_values)
   
    for case in reversedsorted_is:
        result = insertion_sort(case)
        insertion_y_values.append(result[0])
    plt.plot(x_values, insertion_y_values)
    
   
    for case in reversedsorted_bs:
       
        result = bubble_sort(case)
        bubble_y_values.append(result[0])
        
    plt.plot(x_values, bubble_y_values)
    
    plt.title("Reverse Sorted Sequences")
    
    plt.xlabel('Dataset Size')
    plt.ylabel('Comparisons')
    
    plt.legend(['Selection Sort','Insertion sort', 'Bubble Sort'], loc='upper left')
    plt.show()
    
    ''' RANDOM SEQUENCES '''
    
    randomsorted_ss = test_cases_init(300)[2]
    randomsorted_is = test_cases_init(300)[2]
    randomsorted_bs = test_cases_init(300)[2]
    
    selection_y_values = []
    insertion_y_values = []
    bubble_y_values = []
    
    for case in randomsorted_ss:
        result = selection_sort(case)
        selection_y_values.append(result[0])
    plt.plot(x_values, selection_y_values)
   
    for case in randomsorted_is:
        result = insertion_sort(case)
        insertion_y_values.append(result[0])
    plt.plot(x_values, insertion_y_values)
    
   
    for case in randomsorted_bs:
        result = bubble_sort(case)
        bubble_y_values.append(result[0])
        
    plt.plot(x_values, bubble_y_values)
    
    plt.title("Random Sequences")
    
    plt.xlabel('Dataset Size')
    plt.ylabel('Comparisons')
    
    plt.legend(['Selection Sort','Insertion sort', 'Bubble Sort'], loc='upper left')
    plt.show()
    
'''Insertion Sort vs Shell Sort Line Graph''' 
def insertion_vs_shell():
    x_values = ranges_init(300)
    test_cases = test_cases_init(300)
    
    presorted_is = test_cases[0]
    reversedsorted_is = test_cases[1]
    randomsorted_is = test_cases[2]
    
    presorted_ss = test_cases[0]
    reversedsorted_ss = test_cases[1]
    randomsorted_ss = test_cases[2]
    
    ''' PRESORTED SEQUENCES '''
    shell_y_values = []
    insertion_y_values = []
    
    for case in presorted_is:
        
        result = insertion_sort(case)
        insertion_y_values.append(result[0])

    plt.plot(x_values, insertion_y_values)

    for case in presorted_ss:
        # result = shell_sort_shell(case, shell_gap_seq(len(case)))
        result = shell_sort(case, shell_gap_seq(len(case)))
        shell_y_values.append(result[1])
        
    
    plt.plot(x_values, shell_y_values)
    plt.title("Sorted Sequences")
    
    plt.xlabel('Dataset Size')
    plt.ylabel('Comparisons')
    
    plt.legend(['Insertion Sort','Shell sort'], loc='upper left')
    plt.show()

    ''' REVERSE SORTED SEQUENCES '''
    shell_y_values = []
    insertion_y_values = []
    
    for case in reversedsorted_is:
        result = insertion_sort(case)
        insertion_y_values.append(result[0])

    plt.plot(x_values, insertion_y_values)
    
    for case in reversedsorted_ss:
        # result = shell_sort_shell(case, shell_gap_seq(len(case)))
        result = shell_sort(case, shell_gap_seq(len(case)))
        shell_y_values.append(result[1])
        
    
    plt.plot(x_values, shell_y_values)
    plt.title("Reverse Sorted Sequences")
    
    plt.xlabel('Dataset Size')
    plt.ylabel('Comparisons')
    
    plt.legend(['Insertion Sort','Shell sort'], loc='upper left')
    plt.show()
    
    ''' RANDOM SEQUENCES '''
    shell_y_values = []
    insertion_y_values = []
    
    for case in randomsorted_is:
        result = insertion_sort(case)
        insertion_y_values.append(result[0])

    plt.plot(x_values, insertion_y_values)

    for case in randomsorted_ss:
        # result = shell_sort_shell(case, shell_gap_seq(len(case)))
        result = shell_sort(case, shell_gap_seq(len(case)))
        shell_y_values.append(result[1])
        
    plt.plot(x_values, shell_y_values)
    plt.title("Random Sorted Sequences")
    
    plt.xlabel('Dataset Size')
    plt.ylabel('Comparisons')
    
    plt.legend(['Insertion Sort','Shell sort'], loc='upper left')
    plt.show()
    
'''Shell Gap Sequence vs Ciura Gap Sequence Line Graph with Unsortedness'''
def shell_vs_ciura():

    test_case_shell_rev = initArrays()[3]
    test_case_ciura_rev = initArrays()[3]
    
    test_case_shell_sorted = initArrays()[4]
    test_case_ciura_sorted = initArrays()[4]
    
    test_case_shell_random = initArrays()[5]
    test_case_ciura_random = initArrays()[5]
    
    '''SORTED 1000 NUMBERS'''
    comparisons_x_shell = []
    comparisons_x_ciura = []
    
    unsortedness_y_shell = []
    unsortedness_y_ciura = []
    
    shell_result_sorted = shell_sort(test_case_shell_sorted,  shell_gap_seq(len(test_case_shell_sorted)))
    comparisons_x_shell = shell_result_sorted[4]
    unsortedness_y_shell = shell_result_sorted[3]

    ciura_result_sorted = shell_sort(test_case_ciura_sorted, ciura_gap_seq(len(test_case_ciura_sorted)))
    comparisons_x_ciura = ciura_result_sorted[4]
    unsortedness_y_ciura = ciura_result_sorted[3]

    plt.title("Shell's Gap vs. Ciura's Gap on Sorted Numbers")
    plt.plot(comparisons_x_shell, unsortedness_y_shell, linewidth=3.0)
    plt.plot(comparisons_x_ciura, unsortedness_y_ciura)
    plt.xlabel('Comparisons')
    plt.ylabel('Unsortedness')
        
    plt.legend(['Shell','Ciura'], loc='lower left')
    plt.show()
    
    
    '''REVERSED 1000 NUMBERS'''
    comparisons_x_shell = []
    comparisons_x_ciura = []
    
    unsortedness_y_shell = []
    unsortedness_y_ciura = []
    
    shell_result_rev = shell_sort(test_case_shell_rev,  shell_gap_seq(len(test_case_shell_rev)))
    comparisons_x_shell = shell_result_rev[4]
    unsortedness_y_shell = shell_result_rev[3]

    ciura_result = shell_sort(test_case_ciura_rev, ciura_gap_seq(len(test_case_ciura_rev)))
    comparisons_x_ciura = ciura_result[4]
    unsortedness_y_ciura = ciura_result[3]


    plt.title("Shell's Gap vs. Ciura's Gap on Reversed Numbers")
    plt.plot(comparisons_x_shell, unsortedness_y_shell, linewidth=3.0)
    plt.plot(comparisons_x_ciura, unsortedness_y_ciura)
    plt.xlabel('Comparisons')
    plt.ylabel('Unsortedness')
        
    plt.legend(['Shell','Ciura'], loc='upper right')
    plt.show()
    
    
    '''RANDOM 1000 NUMBERS'''
    comparisons_x_shell = []
    comparisons_x_ciura = []
    
    unsortedness_y_shell = []
    unsortedness_y_ciura = []
    
    shell_result_random = shell_sort(test_case_shell_random,  shell_gap_seq(len(test_case_shell_random)))
    comparisons_x_shell = shell_result_random[4]
    unsortedness_y_shell = shell_result_random[3]

    ciura_result_random = shell_sort(test_case_ciura_random, ciura_gap_seq(len(test_case_ciura_random)))
    comparisons_x_ciura = ciura_result_random[4]
    unsortedness_y_ciura = ciura_result_random[3]


    plt.title("Shell's Gap vs. Ciura's Gap on Random Numbers")
    plt.plot(comparisons_x_shell, unsortedness_y_shell, linewidth=2.0)
    plt.plot(comparisons_x_ciura, unsortedness_y_ciura)
    plt.xlabel('Comparisons')
    plt.ylabel('Unsortedness')
    
    plt.legend(['Shell','Ciura'], loc='upper right')
    plt.show() 
    
def shell_vs_ciura_line():
    x_values = ranges_init(300)
    
    test_case_shell_sorted = test_cases_init(300)[0]
    test_case_ciura_sorted = test_cases_init(300)[0]
    
    test_case_shell_rev = test_cases_init(300)[1]
    test_case_ciura_rev = test_cases_init(300)[1]
    
    test_case_shell_random = test_cases_init(300)[2]
    test_case_ciura_random = test_cases_init(300)[2]
    
    '''SORTED NUMBERS'''
    comparisons_y_shell = []
    comparisons_y_ciura = []
    
    for case in test_case_shell_sorted:
        result = shell_sort(case,  shell_gap_seq(len(case)))
        comparisons_y_shell.append(result[1])
    plt.plot(x_values, comparisons_y_shell)
    
    for case in test_case_ciura_sorted:
        result = shell_sort(case,  ciura_gap_seq(len(case)))
        comparisons_y_ciura.append(result[1])
    plt.plot(x_values, comparisons_y_ciura)
    
    plt.title("Shell's Gap vs. Ciura's Gap on Sorted Numbers")
    plt.xlabel('Comparisons')
    plt.ylabel('Dataset Size')
    plt.legend(['Shell Gap Sequence','Ciura Gap Sequence'], loc='upper left')
    plt.show()
    
    '''REVERSED 300 NUMBERS'''
    comparisons_y_shell = []
    comparisons_y_ciura = []
    
    for case in test_case_shell_rev:
        result = shell_sort(case,  shell_gap_seq(len(case)))
        comparisons_y_shell.append(result[1])
    plt.plot(x_values, comparisons_y_shell)
    
    for case in test_case_ciura_rev:
        result = shell_sort(case,  ciura_gap_seq(len(case)))
        comparisons_y_ciura.append(result[1])
    plt.plot(x_values, comparisons_y_ciura)
    
    plt.title("Shell's Gap vs. Ciura's Gap on Reversed Numbers")
    plt.xlabel('Comparisons')
    plt.ylabel('Dataset Size')
    plt.legend(['Shell Gap Sequence','Ciura Gap Sequence'], loc='upper left')
    plt.show()
    
    '''RANDOM 300 NUMBERS'''
    comparisons_y_shell = []
    comparisons_y_ciura = []
    
    for case in test_case_shell_random:
        result = shell_sort(case,  shell_gap_seq(len(case)))
        comparisons_y_shell.append(result[1])
    plt.plot(x_values, comparisons_y_shell)
    
    for case in test_case_ciura_random:
        result = shell_sort(case,  ciura_gap_seq(len(case)))
        comparisons_y_ciura.append(result[1])
    plt.plot(x_values, comparisons_y_ciura)
    
    plt.title("Shell's Gap vs. Ciura's Gap on Random Numbers")
    plt.xlabel('Comparisons')
    plt.ylabel('Dataset Size')
    plt.legend(['Shell Gap Sequence','Ciura Gap Sequence'], loc='upper left')
    plt.show()

''' Bucket sort across different distributions bar graph'''
import matplotlib.pyplot as plt; plt.rcdefaults()
import numpy as np
import matplotlib.pyplot as plt

def bucket_sort_eval():
    dataArrays = initArrays()
    
    ''' BUCKET SORT WITH BEST CASE DISTRIBUTION '''
    height = []
    ex = []
    
    bucket_size = 30
    
    buckets = bucket_sort(dataArrays[0], bucket_size)[2]
    
    for i in range(0, len(buckets)):
        height.append(i + 1)
        
    for i in range(0, len(buckets)):
        ex.append(len(buckets[i]))
        
    y_pos = np.arange(len(height))
    x = [0, 30, 60, 90, 120, 150, 180, 210, 240, 270, 300]
    
    plt.bar(y_pos, ex, align='edge', alpha=0.5)
    plt.xticks(y_pos, x)
    
    plt.ylabel('Items Per Bucket')
    plt.xlabel('Buckets')
    plt.title('Bucket Sort with Best Case Distribution')

    plt.show()
    
    
    ''' BUCKET SORT WITH WORST CASE DISTRIBUTION '''
    height = []
    ex = []
    
    bucket_size = 30
    
    buckets = bucket_sort(dataArrays[7], bucket_size)[2]
    
    for i in range(0, len(buckets)):
        height.append(i + 1)
        
    for i in range(0, len(buckets)):
        ex.append(len(buckets[i]))
        
    y_pos = np.arange(len(height))
    x = [0, 30, 60, 90, 120, 150, 180, 210, 240, 270, 300]
    
    plt.bar(y_pos, ex, align='edge', alpha=0.5)
    plt.xticks(y_pos, x)
    
    plt.ylabel('Items Per Bucket')
    plt.xlabel('Buckets')
    plt.title('Bucket Sort with Worst Case Distribution')

    plt.show()
    
    ''' BUCKET SORT WITH RANDOM CASE DISTRIBUTION '''
    height = []
    ex = []
    
    bucket_size = 30
    
    buckets = bucket_sort(dataArrays[8], bucket_size)[2]
    
    for i in range(0, len(buckets)):
        height.append(i + 1)
        
    for i in range(0, len(buckets)):
        ex.append(len(buckets[i]))
        
    y_pos = np.arange(len(height))
    x = [0, 30, 60, 90, 120, 150, 180, 210, 240, 270, 300]
    
    plt.bar(y_pos, ex, align='edge', alpha=0.5)
    plt.xticks(y_pos, x)
    
    plt.ylabel('Items Per Bucket')
    plt.xlabel('Buckets')
    plt.title('Bucket Sort with Random Case Distribution')

    plt.show()
    
'''Bucket sort comparisons line graph'''
def bucket_sort_eval_line():
    x_values = ranges_init(300)
    bucket_size = 10
    
    best_y_values = []
    worst_y_values = []
    random_y_values = []
    
    best_case = test_cases_init(300)[0]
    worst_case = test_cases_init(300)[4]
    random_case = test_cases_init(300)[5]
    
    for case in best_case:
        result = bucket_sort(case, bucket_size)
        best_y_values.append(result[1])
    plt.plot(x_values, best_y_values)
    
    for case in worst_case:
        result = bucket_sort(case, bucket_size)
        worst_y_values.append(result[1])
    plt.plot(x_values, worst_y_values)
    
    for case in random_case:
        result = bucket_sort(case, bucket_size)
        random_y_values.append(result[1])
    plt.plot(x_values, random_y_values)

    plt.title("Bucket Sort With Different Distributions")
    
    plt.xlabel('Dataset Size')
    plt.ylabel('Comparisons')
    
    plt.legend(['Best Case Distribution','Worst Case Distribution','Random Case Distribution'], loc='upper left')
    plt.show()
   

'''Radix sort with counting sort and insertion sort subroutines line graph'''
def counting_vs_insertion_radix():
    x_values = ranges_init(300)
    test_cases = test_cases_init(300)
    
    ''' PRESORTED SEQUENCES '''
    count_y_values = []
    insertion_y_values = []
    
    presorted_cs = test_cases_init(300)[0]
    presorted_is = test_cases_init(300)[0]
    
    for case in presorted_cs:
        if (len(case) != 0):
            result = radix_sort_cs(case)
            count_y_values.append(result[1])
        else:
            count_y_values.append(0)
        
    plt.plot(x_values, count_y_values)

    for case in presorted_is:
        if(len(case) != 0):
            result = radix_sort_is(case, 10)
            insertion_y_values.append(result[1])
        else:
            insertion_y_values.append(0)
   
    plt.plot(x_values, insertion_y_values)
    plt.title("Sorted Sequences")
    
    plt.xlabel('Dataset Size')
    plt.ylabel('Comparisons')
    
    plt.legend(['Counting Sort Subroutine','Insertion Sort Subroutine'], loc='upper left')
    plt.show()
    
    ''' REVERSE SORTED SEQUENCES '''
    count_y_values = []
    insertion_y_values = []
    
    reversed_cs = test_cases_init(300)[1]
    reversed_is = test_cases_init(300)[1]
    
    for case in reversed_cs:
        if (len(case) != 0):
            result = radix_sort_cs(case)
            count_y_values.append(result[1])
        else:
            count_y_values.append(0)
    plt.plot(x_values, count_y_values)

    for case in reversed_is:
        if(len(case) != 0):
            result = radix_sort_is(case, 10)
            insertion_y_values.append(result[1])
        else:
            insertion_y_values.append(0)        
    plt.plot(x_values, insertion_y_values)
    
    plt.title("Reverse Sequences")
    plt.xlabel('Dataset Size')
    plt.ylabel('Comparisons')
    plt.legend(['Counting Sort Subroutine','Insertion Sort Subroutine'], loc='upper left')
    plt.show()
    
    ''' RANDOM SORTED SEQUENCES '''
    count_y_values = []
    insertion_y_values = []
    
    random_cs = test_cases_init(300)[2]
    random_is = test_cases_init(300)[2]
    
    for case in random_cs:
        if (len(case) != 0):
            result = radix_sort_cs(case)
            count_y_values.append(result[1])
        else:
            count_y_values.append(0)
    plt.plot(x_values, count_y_values)

    for case in random_is:
        if(len(case) != 0):
            result = radix_sort_is(case, 10)
            insertion_y_values.append(result[1])
        else:
            insertion_y_values.append(0)
    plt.plot(x_values, insertion_y_values)
    
    plt.title("Random Sequences")
    plt.xlabel('Dataset Size')
    plt.ylabel('Comparisons')
    
    plt.legend(['Counting Sort Subroutine','Insertion Sort Subroutine'], loc='upper left')
    plt.show()
    
''' Merge Sort vs Quick Sort Line Graph'''
def merge_vs_quick():
    x_values = ranges_init(300)

    ''' RANDOM SEQUENCE WITHIN 300 '''
    merge_y_values = []
    quick_y_values = []
  
    random_ms = test_cases_init(300)[2]
    random_qs = test_cases_init(300)[2]
    
    for case in random_ms:
        if (len(case) != 0):
            result = merge_sort(case)
            merge_y_values.append(result[1])
        else:
            merge_y_values.append(0)
    plt.plot(x_values, merge_y_values)

    for case in random_qs:
        if(len(case) != 0):
            result = quick_sort(case, None, None)
            quick_y_values.append(result)
        else:
            quick_y_values.append(0)
    plt.plot(x_values, quick_y_values)
    
    plt.title("Random Sequence within 1-300")
    plt.xlabel('Dataset Size')
    plt.ylabel('Comparisons')
    
    plt.legend(['Merge Sort','Quick Sort'], loc='upper left')
    plt.show()
    
    ''' RANDOM SEQUENCE WITHIN 1000 '''
    merge_y_values = []
    quick_y_values = []
  
    random_ms = test_cases_init(300)[3]
    random_qs = test_cases_init(300)[3]
    
    for case in random_ms:
        if (len(case) != 0):
            result = merge_sort(case)
            merge_y_values.append(result[1])
        else:
            merge_y_values.append(0)
    plt.plot(x_values, merge_y_values)

    for case in random_qs:
        if(len(case) != 0):
            result = quick_sort(case, None, None)
            quick_y_values.append(result)
        else:
            quick_y_values.append(0)
    plt.plot(x_values, quick_y_values)
    
    plt.title("Random Sequence within 1-1000")
    plt.xlabel('Dataset Size')
    plt.ylabel('Comparisons')
    
    plt.legend(['Merge Sort','Quick Sort'], loc='upper left')
    plt.show()