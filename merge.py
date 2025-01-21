def merge_alternately(word1, word2):
    merged = []
    len1, len2 = len(word1), len(word2)
    min_len = min(len1, len2)
    for i in range(min_len):
        merged.append(word1[i])
        merged.append(word2[i])
    if len1 > len2:
        merged.append(word1[min_len:])
    elif len2 > len1:
        merged.append(word2[min_len:])
    return ''.join(merged)
word1 = "abc"
word2 = "pqrstu"
result = merge_alternately(word1, word2)
print(result)
