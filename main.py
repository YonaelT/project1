def check_p(word):
    if word == word[::-1]:
        return True
    else:
        return False

word = "abc"
print(check_p(word))
