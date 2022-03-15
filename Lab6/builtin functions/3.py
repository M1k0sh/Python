#def isPalindrome(string):
#	 left_pos = 0
#	 right_pos = len(string) - 1
#	
#	 while right_pos >= left_pos:
#		 if not string[left_pos] == string[right_pos]:
#			 return 'No it is not Palindrom'
#		 left_pos += 1
#		 right_pos -= 1
#	 return 'Yes it is Palindrom'
#
#s = input()
#
#print(isPalindrome(s)) 

def isPalindrome(s):
    rev = ''.join(reversed(s))
    if rev == s:
        return "Yes it is Palindrome"
    return "No it is not Palindrome"

s = input()

print(isPalindrome(s))