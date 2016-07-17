import BioI

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

#f=open("Vibrio_cholerae.txt")
#sequences = f.readlines()
#text = sequences[0].rstrip()
#pattern = "CTTGATCAT"
##pattern = "ATGATCAAG"
#f.close()
#print(PatternLocation(text, pattern))

#print(BioI.PatternToNumber('AATTTAGAAAGCGATTCCT'))
#print(BioI.NumberToPattern(7256, 11))
#r = BioI.ComputingFrequencies('AGCAACAAAAAGTCAATCCTGAGATCTCAGCCGTGGAGTATTCTAATGCCTTCATCTTGCCGGAAAAACTTCGTACCTAGCATTTACAAAATGGGACATCTTAACCCACGTTTTTCGGAAAGGCCGCAAATAGATGTCTGAGTGGGCTGCGCTCACAAGCCTGTAGTGGGAGGCCATTGGGAAACATAGATTAATAGCGTATGTAGTCGAAACCTGTTGGCCGGGCCAGGCTTGCAGACATAACGTAGGTTGGTAAAAATATTAAAGGCTGCCATCCCCGGATTATAGTGAAGAATGCACCAGTTTAGAGTGTGCTATCCAAATCCATACGAGCGGCAACGCTATACACTGTGTCTAGGATGGTATGTCGATTACCCTACGCCCCCGGTCTTACCTACACCAGGCCTTTGGAAACTGCCAGCGACACGGCACAACCGCATTGACCGTGCCGCTTATTGGATACACCGGACGATCTCACGTAGACGTTTTTGGTATTAGCGCATGGACCGGAGAGAATAATCATCTTCGGAACGCACCCTCTTTCCACGCTGGCGTAACGGAAATACCGGATTTGACACATAGCGTACATCCATTAGGGGTAACACTGGTACCCCCCGGTTTAGGGCAGTTTTAAAATACTCGT', 6)
#for item in r:
#    print(str(item) + " ", end = "")

f=open("dataset_4_5.txt")
sequences = f.readlines()
genome = sequences[0].rstrip()
k, L, t = sequences[1].split()
k, L, t = int(k), int(L), int(t)
#genome = 'CGGACTCGACAGATGTGAAGAACGACAATGTGAAGACTCGACACGACAGAGTGAAGAGAAGAGGAAACATTGTAA'
#k, t, L = 5, 4, 50
f.close()
print(BioI.BetterClumpFinding(genome, k, t, L))
