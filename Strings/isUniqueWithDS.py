import collections

check_string = "String z c"
check_string = check_string.lower()

results = collections.Counter(check_string)
if ' ' in results.keys():
    results.pop(' ')
for count in results.values():
    if count > 1:
        print("Has repititive values")
        break
if count <= 1:
    print("Has unique values")
        

