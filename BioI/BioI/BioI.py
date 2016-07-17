import math

def PatternCount(text, pattern):
    """find the occurence of a pattern"""
    lent = len(text)
    lenp = len(pattern)
    n = 0
    for i in range(0, lent - lenp + 1):
        if text[i : i + lenp] == pattern:
            n += 1
    return n

def FrequentWords(Text, k):
    """find the most frequent k-mer, not optimized"""
    lent = len(Text)
    frequentPatterns = []
    count = [0] * lent
    for i in range(0, lent - k + 1):
        pattern = Text[i: i + k]
        count[i] = PatternCount(Text, pattern)
        maxCount = max(count)
    for i in range(0, lent - k + 1):
        if count[i] == maxCount:
            frequentPatterns.append(Text[i: i + k])
    frequentPatterns = set(frequentPatterns)
    return frequentPatterns

def FasterFrequentWords(Text, k):
    """find the most frequent k-mer, optimized"""
    lent = len(Text)
    frequentPatterns = {}
    FrequencyArray = ComputingFrequencies(Text, k)
    maxCount = max(FrequencyArray)
    for i in range(0, pow(4, k)):
        if FrequencyArray(i) == maxCount:
            Pattern = NumberToPattern(i, k)
            frequentPatterns.add(Pattern)
    return frequentPatterns

def ComputingFrequencies(Text, k):
    """output the Frequency Array for k-mers"""
    lent = len(Text)
    FrequencyArray = [0] * pow(4, k)    
    for i in range(0, lent - k + 1):
        Pattern = Text[i: i + k]
        j = PatternToNumber(Pattern)
        FrequencyArray[j] += 1
    return FrequencyArray

def PatternToNumber(Pattern):
    """change DNA k-mer to index"""
    global SymToNum
    if len(Pattern) == 0:
        return 0
    symbol = Pattern[-1]
    prefix = Pattern[:-1]
    return 4 * PatternToNumber(prefix) + SymToNum[symbol]

def NumberToPattern(index, k):
    """change index to DNA k-mer"""
    global SymToNum
    if k == 1:
        return list(SymToNum.keys())[list(SymToNum.values()).index(index)]
    prefixIndex = index // 4
    r = index % 4
    symbol = list(SymToNum.keys())[list(SymToNum.values()).index(r)]
    PrefixPattern = NumberToPattern(prefixIndex, k - 1)
    return PrefixPattern + symbol

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

def BetterClumpFinding(Genome, k, t, L):
    """window length L, find k-mers occurs at least t times"""
    lenG = len(Genome)
    FrequentPatterns = set([])
    Clump = [0] * pow(4, k)
    Text = Genome[0:  L]
    FrequencyArray = ComputingFrequencies(Text, k)
    for index in range(0, pow(4, k)):
        if FrequencyArray[index] >= t:
            Clump[index] = 1
    for i in range(1, lenG - L + 1):
        FirstPattern = Genome[i - 1 : i - 1 + k]
        index = PatternToNumber(FirstPattern)
        FrequencyArray[index] -= 1
        LastPattern = Genome[i + L - k : i + L]
        index = PatternToNumber(LastPattern)
        FrequencyArray[index] += 1
        if FrequencyArray[index] >= t:
            Clump[index] = 1
    for i in range(0, pow(4, k)):
        if Clump[i] == 1:
            Pattern = NumberToPattern(i, k)
            FrequentPatterns.add(Pattern)
    return FrequentPatterns

SymToNum = dict(A = 0, C = 1, G = 2, T = 3)
