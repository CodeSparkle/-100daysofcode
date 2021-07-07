'''
This function is useful for finding the correct position of element it basically work llke a binary search and having same requirement of sorted array
it requires to import bisect module like this:
import bisect 
It mainly contains two function:- 
# it does not consider the current position of element is we want to search. It means it return position of element if it is present in array.
1- bisect_left  
# it consider the current element present in array and return pos+1 i.e pos= position of current element.
2-bisect_right 
'''
#example implementation
from bisect import bisect_left as bl, bisect_right as br
arr =[1,3,5,7,23,27,29,35]
posl= bl(arr,5)
posr= br(arr,5)
print(posl,posr)
