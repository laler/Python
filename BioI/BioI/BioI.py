import math
import random

#week1
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
        return list(SymToNum.keys())[list(SymToNum.values()).index(index)]   ###get the key based on value in dictionary
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

#week2
def MinSkew(genome):
    """Minimum Skew value for DNA replication to find ori"""
    lenG = len(genome)
    skew = [0] * (lenG + 1)
    for i in range(0, lenG):
        if genome[i] == 'C':
            skew[i + 1] = skew[i] - 1
        elif genome[i] == 'G':
            skew[i + 1] = skew[i] + 1 
        else:       
            skew[i + 1] = skew[i]
    minSkew = min(skew)
    loc = [i for i, x in enumerate(skew) if x == minSkew]    ###index for duplicate list elements
    return loc
def HammingDistance(p, q):
    """count mismatch between two DNA sequences"""
    lenp = len(p)
    hd = 0
    for i in range(0, lenp):
        if p[i] != q[i]:
            hd += 1
    return hd
def ApproxPatternCount(pattern, text, d):
    """pattern as substring of text with at most d mismatches"""
    lent = len(text)
    lenp = len(pattern)
    n = 0
    for i in range(0, lent - lenp + 1):
        if HammingDistance(text[i : i + lenp], pattern) <= d:
            #print(i)
            n += 1
    return n
def FrequentWordsWithMismatches(Text, k, d):
    """find neighbor k-mers first, plus reversed complement"""
    lent = len(Text)
    FrequentPatterns = set([])
    Close = [0] * pow(4, k)
    FrequencyArray = [0] * pow(4, k)
    for i in range(0, lent - k + 1):
        Neighborhood = Neighbors(Text[i: i + k], d)
        for Pattern in Neighborhood:
            index = PatternToNumber(Pattern)
            Close[index] = 1
    for i in range(0, pow(4, k)):
        TextRev = Reverse(Text)
        if Close[i] == 1:
            Pattern = NumberToPattern(i, k)
            FrequencyArray[i] = ApproxPatternCount(Pattern, Text, d)\
                             + ApproxPatternCount(Pattern, TextRev, d)
#Not counting reversed complement
            #FrequencyArray[i] = ApproxPatternCount(Pattern, Text, d)
        maxCount = max(FrequencyArray)
    for i in range(0, pow(4, k)):
        if FrequencyArray[i] == maxCount:
            Pattern = NumberToPattern(i, k)
            FrequentPatterns.add(Pattern)
    #lent = len(Text)
    #FrequentPatterns, Neighborhoods= set([]), []
    #for i in range(0, lent - k + 1):
    #    for Neighbor in Neighbors(text[i: i + k], d):
    #        Neighborhoods.append(Neighbor)
    #lenN = len(Neighborhoods)
    #Index, Count = [0] * lenN, [0] * lenN
    #for i in range(0, lenN):
    #    Pattern = Neighborhoods[i]
    #    Index[i] = PatternToNumber(Pattern)
    #    Count[i] = 1
    #SortedIndex = sorted(Index)
    #for i in range(0, lenN):
    #    if SortedIndex[i] == SortedIndex[i + 1]:
    #        Count[i + 1] = Count[i] + 1
    #maxCount = max(Count)
    #for i in range(0, lenN):
    #    if Count[i] == maxCount:
    #        Pattern = NumberToPattern(SortedIndex[i], k)
    #        FrequentPatterns.add(Pattern)
    return FrequentPatterns
def Neighbors(Pattern, d):
    """set of neighbors with at most d mismatches"""
    lenP = len(Pattern)
    if d == 0:
        return {Pattern}
    if lenP == 1:
        return {'A', 'C', 'G', 'T'}
    Neighborhood = set([])
    SuffixNeighbors = Neighbors(Pattern[1:], d)
    Nuceltide = ['A', 'C', 'G', 'T']
    for Text in SuffixNeighbors:
        if HammingDistance(Pattern[1:], Text) <= d:
            for x in Nuceltide:
                Neighborhood.add(x + Text)
        else:
            Neighborhood.add(Pattern[0] + Text)
    return Neighborhood
   
#week3-Motif finding among t sequences (regulatory motifs)
def MotifEnumeration(Dna, k, d):
    """k-mer motif with at most d mismatches"""
    Patterns = set([])
    kmer = set([])
    Neighborhood = set([])
    for p in Dna:
        lenp = len(p)
        for i in range(0, lenp - k + 1):
            kmer.add(p[i: i + k])
    for pattern in kmer:
        pNeighbors = Neighbors(pattern, d)
        for p in pNeighbors:
            Neighborhood.add(p)
    for pn in Neighborhood:
        flag = 0
        for p in Dna:
            for i in range(0, len(p) - k + 1):
                if HammingDistance(pn, p[i: i + k]) <= d:
                    flag += 1
#                    print(pn +' '+ p[i: i + k])
                    break
        if flag == len(Dna):
            Patterns.add(pn)
    return Patterns
def MedianString(Dna, k):
    """find pattern in t Dna strings, min score"""
    distance = float('infinity')
    for i in range(0, pow(4, k) - 1):
        Pattern = NumberToPattern(i, k)
        if distance > DistanceBetweenPatternAndStrings(Pattern, Dna):
            distance = DistanceBetweenPatternAndStrings(Pattern, Dna)
            Median = Pattern
    #MedianTotal =[]
    #for i in range(0, pow(4, k) - 1):
    #    Pattern = NumberToPattern(i, k)
    #    if DistanceBetweenPatternAndStrings(Pattern, Dna) == distance:
    #         MedianTotal.append(Pattern)
    #return MedianTotal
    return Median
def DistanceBetweenPatternAndStrings(Pattern, Dna):
    """find the least score in a specific Pattern"""
    k = len(Pattern)
    distance = 0
    for Text in Dna:
        lend = len(Text)
        HammingDis = float('infinity')
        for i in range(0, lend - k + 1):
            PatternP = Text[i: i + k]
            if HammingDis > HammingDistance(Pattern, PatternP):
                HammingDis = HammingDistance(Pattern, PatternP)
        distance += HammingDis
    return distance
def ProfileProb(Text, k, Profile):
    """find a profile-most probable k-mer in a string"""
    lent = len(Text)
    Value = 0
    maxPattern = Text[0: k]
    for i in range(0, lent - k + 1):
        Pattern = Text[i: i + k]
        curValue = ProfileScore(Pattern, k, Profile)
        if Value < curValue:
            Value = curValue
            maxPattern = Text[i: i + k]    
    return maxPattern
def ProfileScore(Pattern, k, Profile):
    """compute the profile score based on Profile table"""
    Value = 1
    global SymToNum
    for j in range(0, k):
        Nucleotide = SymToNum[Pattern[j]]
        Value *= float(Profile[Nucleotide][j])
    return Value
def ProfileForm(Motifs, k):
    """generate Profile table from known Motifs, meets oliver cromwell"""
    global SymToNum
    t = len(Motifs)
    Profile = [[1/(t + 4)] * k, [1/(t + 4)] * k, [1/(t + 4)] * k, [1/(t + 4)] * k]
    for i in range(0, k):
        for j in range(0, t):
            Nucleotide = Motifs[j][i]
            Profile[SymToNum[Nucleotide]][i] += 1.0 / (t + 4)
    return Profile
def GreedyMotifSearch(Dna, k, t):
    """motif-profile-update motif-update profile"""
    BestMotifs = [row[0: k] for row in Dna]
    BestPattern = Consensus(BestMotifs, k)
    BestScore = DistanceBetweenPatternAndStrings(BestPattern, BestMotifs)
    Motifs = [''] * t
    for i in range(0, len(Dna[0]) - k + 1):
        Motifs[0] = Dna[0][i: i + k]
        for j in range(1, t):
            Profile = ProfileForm(Motifs[0: j], k)
            Motifs[j] = ProfileProb(Dna[j], k, Profile)
        NewMotifs = Motifs
        NewPattern = Consensus(NewMotifs, k)
        NewScore = DistanceBetweenPatternAndStrings(NewPattern, NewMotifs)
        if NewScore < BestScore:
            BestMotifs = NewMotifs[:] ###copy a list by values
            BestScore = NewScore
    return BestMotifs
def Consensus(Motifs, k):
    """find the consensus pattern from motifs"""
    global SymToNum
    lenm = len(Motifs)
    Pattern = [''] * k
    for i in range(0, k):
        Nucount = [0] * 4
        for j in range(0, lenm):
            Nucount[SymToNum[Motifs[j][i]]] += 1
        maxCount = max(Nucount)
        NucNum = Nucount.index(maxCount)
        Pattern[i] = list(SymToNum.keys())[list(SymToNum.values()).index(NucNum)]
    return Pattern
def MotifsScore(Motifs, k):
    """compute score from the current Motifs"""
    Pattern = Consensus(Motifs, k)
    Score = DistanceBetweenPatternAndStrings(Pattern, Motifs)
    return Score

#week4-Randomized algorithm for regulatory motifs
def MotifForm(Dna, k, Profile):
    Motifs = []
    for j in range(0, len(Dna)):
        Motifs.append(ProfileProb(Dna[j], k, Profile))
    return Motifs
def RandomizedMotifSearch(Dna, k, t): #results are not always consistent, maybe improved by choosing lowest score
    """random choose first motifs, then profile-motifs-profile"""
    lend = len(Dna[0])
    Motifs = []
    for i in range(0, t):
        loc = random.randint(0, lend - k)
        Motifs.append(Dna[i][loc: loc + k])
    BestMotifs = Motifs[:]
    #print(BestMotifs)
    BestScore = MotifsScore(BestMotifs, k)
    while True:
        Profile = ProfileForm(Motifs, k)
        Motifs = MotifForm(Dna, k, Profile)
        #print (Motifs)
        Score = MotifsScore(Motifs, k)
        if Score < BestScore:
            BestMotifs = Motifs[:] ###copy a list by values
            BestScore = Score
        else:
            return BestMotifs
def RandomizedNTimes(Dna, k, t, n):
    """run randomized algorithm n times and return the most frequent result"""
    MotifsSet = []
    Count = []
    for i in range(0, n):
        NewMotifs = RandomizedMotifSearch(Dna, k, t)
        if NewMotifs in MotifsSet:
            Count[MotifsSet.index(NewMotifs)] += 1
        else:
            #print(NewMotifs) 
            MotifsSet.append(NewMotifs)
            Count.append(1)
    print(Count)
    Motifs = MotifsSet[Count.index(max(Count))] #choose by count, not by lowest score
    return Motifs
def GibbsSampler(Dna, k, t, N): #very bad algorithm
    """random choose motifs by Gibbs Sampler"""
    lend = len(Dna[0])
    Motifs = []
    for i in range(0, t):
        loc = random.randint(0, lend - k)
        Motifs.append(Dna[i][loc: loc + k])
    BestMotifs = Motifs[:]
    BestScore = MotifsScore(BestMotifs, k)
    for j in range(1, N):
        i = random.randint(0, t - 1)
        Motifs.pop(i)
        Profile = ProfileForm(Motifs, k)
        MotifInsert = ProfileProb(Dna[i], k, Profile)
        Motifs.insert(i, MotifInsert)
        Score = MotifsScore(Motifs, k)
        if Score < BestScore:
            BestMotifs = Motifs[:]
            BestScore = Score
    return BestMotifs, BestScore
def GibbsSamplerNTimes(Dna, k, t, n):
    """run Gibbs Sampler n times and return the lowest score result"""
    Score = pow(4, k)
    for i in range(0, n):
        NewMotifs, NewScore = GibbsSampler(Dna, k, t, 50)
        if NewScore < Score:
            Score = NewScore
            Motifs = NewMotifs[:]
    print (Score)
    return Motifs

SymToNum = dict(A = 0, C = 1, G = 2, T = 3)
