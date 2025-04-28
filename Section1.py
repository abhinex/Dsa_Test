# DSA Test
# Section 1 Arrays and Strings 
# Find the missing Number
# Given an array containing n-1 distinct number from 1 to n, find the missing number in the sequence
# Time Complexity O(n)

# first define a missing number function with parameters arr and n


def missingNumber(arr,n): 

    total_sum=n*(n+1)//2   # for total sum of number from 1 to n
    actual_sum=sum(arr)    # for sum of elements in an array
    missingNumber=total_sum-actual_sum # the missing number is the differenc between excepeted and actual

    return missingNumber
arr=[1,2,4,5] # missing number 3
n=5 # total number 
print("The missing number is:",missingNumber(arr,n))

# Output:The missing number is: 3


# Question 2: Longest the substring without the reapating characters
# given the string s, find the length of the longest the substring
# Implement using the sliding windows technique
#

# define the function longestsubstring 
def longestsubstring(s):

    seen=set() # to store unquie charaters
    left=0     # pointers for the sliding windows
    max_length=0 

    # now iterate the string

    for right in range(len(s)): # if the characters is seen already, remove the window from the left 
        while s[right] in seen:
            seen.remove(s[left])
            left +=1

        seen.add(s[right]) # add the current character to set

        max_length=max(max_length,right-left+1) # update the max length

    return max_length

# Example

s="abcabcbb"
print("the length of the longest substring without repeat:",longestsubstring(s))

   




