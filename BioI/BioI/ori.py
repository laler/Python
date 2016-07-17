def patternCount(text, pattern):
    lent = len(text)
    lenp = len(pattern)
    n = 0
    for i in range(0, lent - lenp + 1):
        if text[i : i + lenp] == pattern:
            n += 1
    print(n)
    return

#f=open("PatternCount.txt")
f=open("dataset_2_7.txt")
sequences = f.readlines()
text = sequences[0].rstrip()
pattern = sequences[1].rstrip()
f.close()
patternCount(text, pattern)
