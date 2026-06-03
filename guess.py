import random
password = input("Enter the password: ")
chars = "1234567890abcdefghijklmnopqrstuvwxyz"
done = False 
count = 0 
tried = set()

# Phase 1: Try all same-character passwords first (like "aaaaaa", "bbbbbb")
for char in chars:
    attempt = char * 6  # repeat the character 6 times
    count = count + 1
    if attempt == password:
        print(count)
        done = True
        raise SystemExit

# Phase 2: Random guessing with weights favoring letters over numbers
weights = [1]*10 + [3]*26  # numbers (0-9) get weight 1, letters (a-z) get weight 3

while done == False:
    randomchars = "".join(random.choices(chars, weights=weights, k=6))
    if randomchars not in tried:
        count = count + 1
        tried.add(randomchars)
        if randomchars == password:
            done = True
            print (count)


