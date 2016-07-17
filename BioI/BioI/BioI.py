def PatternCount(text, pattern):
    """find the occurence of a pattern"""
    lent = len(text)
    lenp = len(pattern)
    n = 0
    for i in range(0, lent - lenp + 1):
        if text[i : i + lenp] == pattern:
            n += 1
    return n

#def FrequentWords(Text, k):
#    """find the most frequent k-mer, not optimized"""
#    lent = len(Text)
#    frequentPatterns = []
#    count = [0] * lent
#    for i in range(0, lent - k + 1):
#        pattern = Text[i: i + k]
#        count[i] = ori.PatternCount(Text, pattern)
#        maxCount = max(count)
#    for i in range(0, lent - k + 1):
#        if count[i] == maxCount:
#            frequentPatterns.append(Text[i: i + k])
#    frequentPatterns = set(frequentPatterns)
#    return frequentPatterns

def FrequentWords(Text, k):
    """find the most frequent k-mer, optimized"""
    lent = len(Text)
    frequentPatterns = []
    count = [0] * lent
    for i in range(0, lent - k + 1):
        pattern = Text[i: i + k]
        count[i] = ori.PatternCount(Text, pattern)
        maxCount = max(count)
    for i in range(0, lent - k + 1):
        if count[i] == maxCount:
            frequentPatterns.append(Text[i: i + k])
    frequentPatterns = set(frequentPatterns)
    return frequentPatterns

def Reverse(text):
    """the reverse strand of DNA"""
    pattern = {'A': 'T', 'T': 'A', 'C': 'G', 'G': 'C'}
    text = text[::-1]
    newtext = ''
    for t in text:
        newtext += pattern[t]
    return newtext

def PatternLocation(text, pattern):
    lent = len(text)
    lenp = len(pattern)
    result = ''
    for i in range(0, lent - lenp + 1):
        if text[i : i + lenp] == pattern:
            result += str(i)
            result += ' '
    return result


#f=open("dataset_2_10.txt")
#sequences = f.readlines()
#text = sequences[0].rstrip()
#k = int(sequences[1].rstrip())
#f.close()
#f = FrequentWords(text, k)
#for i in f:
#    print(i)

#f=open("dataset_3_5.txt")
#sequences = f.readlines()
#text = sequences[1].rstrip()
#pattern = sequences[0].rstrip()
#f.close()
#print(PatternLocation(text, pattern))

#text = sequences[0].rstrip()
#f.close()
#print(Reverse(text))

f=open("Vibrio_cholerae.txt")
sequences = f.readlines()
text = sequences[0].rstrip()
pattern = "CTTGATCAT"
#pattern = "ATGATCAAG"
f.close()
print(PatternLocation(text, pattern))
