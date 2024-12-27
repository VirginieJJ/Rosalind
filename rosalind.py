# ################################################################
# ##################     Rosalind     ############################
# ################################################################


# ##################     FONCTIONS    ############################


def read_fichier(fichier):
	with open(fichier, 'r') as f_input:
		return [i for i in f_input.read().split('\n') if i]


# ##################     Exercices    ############################


# ##### INI 1

import this

"""
The Zen of Python, by Tim Peters

Beautiful is better than ugly.
Explicit is better than implicit.
Simple is better than complex.
Complex is better than complicated.
Flat is better than nested.
Sparse is better than dense.
Readability counts.
Special cases aren't special enough to break the rules.
Although practicality beats purity.
Errors should never pass silently.
Unless explicitly silenced.
In the face of ambiguity, refuse the temptation to guess.
There should be one-- and preferably only one --obvious way to do it.
Although that way may not be obvious at first unless you're Dutch.
Now is better than never.
Although never is often better than *right* now.
If the implementation is hard to explain, it's a bad idea.
If the implementation is easy to explain, it may be a good idea.
Namespaces are one honking great idea -- let's do more of those!
"""


# ##### Variables and somes arithmetic
a = input("a = ")
b = input("b = ")
reponse = a*a+b*b
print(reponse)


# ##### INI5
F = open('rosalind_ini5.txt', 'r')
fic = F.readlines()
F.close()

F = open('resultats.txt', 'w')
for i in range(1, len(fic)):
	if i % 2:
		F.write(fic[i])

F.close()


# ##### INI6
F = open('rosalind_ini6.txt', 'r')
fic = F.read()
F.close()

dico = {}
fic = fic.split('\r\n')
for i in range(len(fic)):
	fic[i] = fic[i].split(' ')
	for v in fic[i]:
		if not dico.has_key(v):
			dico[v] = 1
		else:
			dico[v] += 1

F = open('resultats.txt', 'w')
for i in range(1,len(fic)):
	for k, v in dico.iteritems():
		if k:
			F.write(str(k)+'\t'+str(v)+'\n')
F.close()


# ##### DNA : Counting DNA Nucleotides
fic = read_fichier(fichier='rosalind_dna.txt')
dico = {'A': 0, 'T': 0, 'C' : 0, 'G': 0}
for nt in fic[0]:
	dico[nt] += 1

F = open('resultats.txt', 'w')
F.write(str(dico['A']) + str(dico['C']) + str(dico['G']) + str(dico['T']))
F.close()
	

# ##### RNA : Transcribing DNA into RNA
fic = read_fichier(fichier='rosalind_rna.txt')
F = open('resultats.txt','w')
for nt in fic[0]:
	if nt == 'T':
		F.write('U')
	else:
		F.write(nt)

F.close()


# ##### REVC : Complementing a Strand of DNA
fic = read_fichier(fichier='rosalind_revc.txt')
dico = {'A': 'T', 'T': 'A', 'C': 'G', 'G': 'C'}
l = len(fic[0])-1
F = open('resultats.txt', 'w')
for i in xrange(l+1):
	F.write(dico[fic[0][l-i]])
F.close()


# ##### sset - Counting Subsets
n = 833
print(2**n % 1000000)


# ##### lexf - Enumerating k-mers Lexicographically
import itertools

text = "A B C D E F".replace(" ", "")
r = 3
text="ATCG"; r=2
result = set()
for i in itertools.combinations_with_replacement(text, r):
	for j in itertools.permutations(i, r):
		result.add("".join(j))

for i in sorted(result):
	print(i)




