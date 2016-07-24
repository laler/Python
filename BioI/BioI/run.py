import BioI

######week 1 boss question
#f=open("dataset_4_5.txt")
#sequences = f.readlines()
#genome = sequences[0].rstrip()
#k, L, t = sequences[1].split()
#k, L, t = int(k), int(L), int(t)
##genome = 'CGGACTCGACAGATGTGAAGAACGACAATGTGAAGACTCGACACGACAGAGTGAAGAGAAGAGGAAACATTGTAA'
##k, t, L = 5, 4, 50
#f.close()
#print(BioI.BetterClumpFinding(genome, k, t, L))

######week 2
#f=open("dataset_9_8.txt")
#sequences = f.readlines()
#pattern = sequences[0].rstrip()
#k, d = sequences[1].split()
#k, d = int(k), int(d)
#f.close()
#p = BioI.FrequentWordsWithMismatches(pattern, k, d)
#f=open('1.txt', 'w')
#for x in p:
#    f.write(x + '\n')
#f.close()

######week 34
f=open("dataset_163_4.txt")
sequences = f.readlines()
k, t, N = sequences[0].split()
k, t = int(k), int(t)
Text = sequences[0].rstrip()
Dna = []
for i in range(1, t + 1):
    Dna.append(sequences[i].rstrip())
#Profile = [['0.2', '0.2', '0.3', '0.2', '0.3'],\
#            ['0.4', '0.3', '0.1', '0.5', '0.1'],\
#            ['0.3', '0.3', '0.5', '0.2', '0.4'],\
#            ['0.1', '0.2', '0.1', '0.1', '0.2']]
#Dna = ['CGCCCCTCTCGGGGGTGTTCAGTAAACGGCCA','GGGCGAGGTATGTGTAAGTGCCAAGGTGCCAG',\
#    'TAGTACCGAGACCGAAAGAAGTATACAGGCGT','TAGATCAAGTTTCAGGTGCACGTCGGTGAACC',\
#    'AATCCACCAGCTCCACGTGCAATGTTGGCCTA']
#k=8
#t=5
#print(BioI.GreedyMotifSearch(Dna, k, t))
#print(BioI.GibbsSamplerNTimes(Dna, k, t, 2000))
f.close()
fo=open('1.txt', 'w')
for i in BioI.GibbsSamplerNTimes(Dna, k, t, 2000):
    fo.write(i + '\n')
fo.close()

#week 5
