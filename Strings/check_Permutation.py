import collections

check_string1 = "wef34f"
check_string2 = "wffe34"
check_string1 = check_string1.lower()
check_string2 = check_string2.lower()

results1 = collections.Counter(check_string1)
results2 = collections.Counter(check_string2)

if results1 == results2:
    print('True')
else:
    print('False')

