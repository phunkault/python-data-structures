def hash_function(key):
    summable = [
        idx * ord(char) for idx, char in enumerate(repr(key).lstrip("'"), 1)
    ]
    return sum(summable)


print(hash_function(1))
print(hash_function(222))
print(hash_function(222))
print(hash_function("zhopa"))
print(hash_function("apozh"))
print(hash_function((1, 2)))
print(hash_function([1, 2, 3]))
print(hash_function([2, 3, 1]))
