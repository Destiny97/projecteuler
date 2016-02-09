from modules.matlib import isPalindrome

mx = 0

for x in range(100, 1000, 1):
    for y in range(100, 1000, 1):
        if x*y > mx and isPalindrome(x*y): mx = x*y
print(mx)
