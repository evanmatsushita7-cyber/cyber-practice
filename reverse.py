while True:
    text = input("Please Enter The Text:")
    stack = ""
    for char in text:
        stack = char + stack
    print (stack)
    if stack == text:
        print("It's a palindrome!")

