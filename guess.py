import random
password = input("Enter the password: ")
chars = "1234567890abcdefghijklmnopqrstuvwxyz"
done = False 
count = 0 
tried = set()
for char in chars:
    attempt = char * 5
    count = count + 1
    if attempt == password:
        print(count)
        done = True
        raise SystemExit
weights = [1]*10 + [3]*26  
while done == False:
    randomchars = "".join(random.choices(chars, weights=weights, k=5))
    if randomchars not in tried:
        count = count + 1
        tried.add(randomchars)
        if randomchars == password:
            done = True
            print (count)