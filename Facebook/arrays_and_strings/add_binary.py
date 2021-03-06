# Add Binary
# time: O(n)
# space: O(n)
"""
Input: a = "1010", b = "1011"
Output: "10101"
carry = 1
end_a = 0
end_b = 0

"1 0 1 1"
*
"1 0 1 0"
*

new_digit = "10101"

"""

class Solution:
    def addBinary(self, a: str, b: str) -> str:
        end_a, end_b, carry = len(a) - 1, len(b) - 1, 0 #start at the end for adding purposes
        new_digit = '' #this string will be returned
        while end_a >= 0 and end_b >= 0: #continue while both can be iterated over
            if int(a[end_a]) + int(b[end_b]) > 1: #  a= 1, b = 1, carry =1, append the carry value
                new_digit += str(carry)
                carry = 1 #as a and b both sum to 1, carry will be set to 1
            elif int(a[end_a]) + int(b[end_b]) + carry > 1: #a= 1, b = 0, carry =1, append the 0 value 
                new_digit += '0'
                carry = 1
            else:
                new_digit += str(int(a[end_a]) + int(b[end_b]) + carry) #values sum to 1 or 0 
                carry = 0 
            end_a -= 1
            end_b -= 1
        while end_a >= 0: #continue while a
            if int(a[end_a]) + carry > 1:
                carry = 1
                new_digit += '0'
            else:
                new_digit += str(int(a[end_a]) + carry)
                carry = 0 
            end_a -= 1
        while end_b >= 0: #continue while b
            if int(b[end_b]) + carry > 1:
                carry = 1
                new_digit += '0'
            else:
                new_digit += str(int(b[end_b]) + carry)
                carry = 0 
            end_b -= 1
        if carry: # check if carry exists, if so add it to the digits
            new_digit += str(carry)
 
        return new_digit[::-1] #return new digit reversed
