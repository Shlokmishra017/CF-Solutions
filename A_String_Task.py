s = input()
vowels = "aeiouy"
result = []
for char in s:
    lower_char = char.lower()
    if lower_char not in vowels:
        result.append(".")
        result.append(lower_char)
print("".join(result))
