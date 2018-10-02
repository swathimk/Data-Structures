char = "abcdefghijklmnopqrstuvwxyz"
check_string = "String z c"

for ch in char:
    count = check_string.count(ch)
    if count > 1:
        print("Has repititive characters of ", ch)
        break
    
if count <= 1:
    print("Has all unique characters")
        

