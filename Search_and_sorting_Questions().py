# -*- coding: utf-8 -*-
"""
Created on Tue Jan 22 08:08:33 2019

@author: fovie
"""

#Sorting ordered array with arbitrary spaces and binary search

#strings: sorted list of strings in which some of the strings can be empty ('')
#x: string to be searched
#Returns: index of x in the strings list if found, -1 otherwise
def search(strings, x) :
    low = 0
    high = len(strings) - 1
 
    while (low <= high) :
        #If we hit an empty string at position high, then keep decreasing
        #high until we get a non-empty string
        while (low <= high and strings[high] == '') :
            high = high - 1
         
        #If we have only empty strings between low and high, then return
        #not found
        if (low > high):
            return -1
 
        mid = (low + high) // 2
 
        #If we get an empty element at mid, then keep incrementing mid.
        #We are guaranteed to find a non-empty string since strings[high]
        #is non-empty
        while (strings[mid] == ''):
            mid += 1
 
        #Compare the mid element with the element being searched
        if (strings[mid] == x) :
            return mid
        elif (strings[mid] < x) :
            low = mid + 1
        else :
            high = mid - 1
         
    return -1

x=["","","",3,"",4,5,"","",""]

search(x,5)


#Find the first element larger than k in a sorted array

#a: sorted list containing elements in non-decreasing order
#k: we are searching for the number immediately above k
#Returns: the number immediately greater than k in the list if it exists,
#       MAX_INT otherwise
def find_next_higher(a, k) :
    low = 0
    high = len(a) - 1
 
    result = -1
    while (low <= high) :
        mid = (low + high) // 2
 
        if (a[mid] > k) :
            result = a[mid] #update the result and continue
            high = mid - 1
        else :
            low = mid + 1
 
    return result 


#Find max and min using the least operations
#Since we will be picking pairs of consecutive numbers, if we have odd number of elements in the array, the last element will be left unpaired. 
#To avoid this problem, if we have odd elements, we will initialize the max value and the min value to the first element in the
# array and then go on picking pairs of numbers from the second element onwards.

#a: input list 
#Returns: the minimum value and maximum value in list are returned
def find_min_max(a) :
    length = len(a)
    max_value = 0
    min_value = 0
 
    i = 0
    if (length % 2 == 1) :
        #If there are odd number of elements, then initialize 
        #max_value and min_value with a[0]
        max_value = min_value = a[0]
        i = 1
     
    while ( i < length ) :
        if (a[i] > a[i+1]) :
            if (a[i] > max_value) :
                max_value = a[i]
            if (a[i+1] < min_value):
                min_value = a[i+1]
        else :
            if (a[i] < min_value):
                min_value = a[i]
            if (a[i+1] > max_value):
                max_value = a[i+1]
         
        i += 2
 
    return min_value, max_value

find_min_max([8,3,4,9,1])

#Find two smallest values by going through the array once

#a:input list 
#Return value: the two smallest values will be returned 
def find_two_smallest(a) :
    length = len(a)
 
    min_value = [MAX_INT, MAX_INT]
 
    for  cur_val in a:
        if (cur_val < min_value[0]) :
            min_value[1] = min_value[0]
            min_value[0] = cur_val 
        elif (cur_val  < min_value[1]) :
            min_value[1] = cur_val 
         
     
    return min_value[0], min_value[1]


def twoStrings(s1, s2):
    for stringa in s1:
        for stringb in s2:
            if stringa==stringb:
                return "True"
            else:
                return "False"
            
twoStrings("felipe","cat")

#########################################################3
####################SORTING ##############################

def bubbleSort(alist):
    for passnum in range(len(alist)-1,0,-1):
        for i in range(passnum):
            if alist[i]>alist[i+1]:
                temp = alist[i]
                alist[i] = alist[i+1]
                alist[i+1] = temp

alist = [54,26,93,17,77,31,44,55,20]
bubbleSort(alist)
print(alist)

#Insertion sort

def insertionSort(alist):
   for index in range(1,len(alist)):

     currentvalue = alist[index]
     position = index

     while position>0 and alist[position-1]>currentvalue:
         alist[position]=alist[position-1]
         position = position-1

     alist[position]=currentvalue

alist = [54,26,93,17,77,31,44,55,20]
insertionSort(alist)
print(alist)

#Merge sort

def mergeSort(fdsfd):
    

