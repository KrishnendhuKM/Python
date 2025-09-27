s = input("enter a string:")
result = ""
count = 1

for i in range(1, len(s)):
    if s[i] == s[i-1]:
        count += 1
    else:
        result += s[i-1] + str(count)
        count = 1
if s:
    result += s[-1] + str(count)
print("entered string is:", s)
print("the result is:", result)