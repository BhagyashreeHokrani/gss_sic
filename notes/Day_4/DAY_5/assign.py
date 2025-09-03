def my_find(text, pattern):
    if pattern == "":
        return 0
    for i in range(len(text) - len(pattern) + 1):
        if text[i:i+len(pattern)] == pattern:
            return i
    return -1

text ="hello world"
pattern = "world"
print(my_find(text, pattern))
