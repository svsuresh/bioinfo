from Bio.Alphabet import IUPAC
import random
from datetime import datetime

n=int(input("type the length of the sequence: "))
j=int(input("type the number of sequences: "))
k=(input("choose S for standard code and I for IUPAC: "))
if k == "S":
  sequnce=IUPAC.IUPACUnambiguousDNA.letters
elif k == "I":
  sequnce=IUPAC.IUPACAmbiguousDNA.letters
dnafile = open("dnasequence_"+datetime.now().strftime("%Y%m%d_%H%M%S")+".fa", "a")
for j in range(j):
	my_seq=''.join(random.choice(sequnce) for i in range(n))
	id="seq "+str(j+1)
	my_seq = ">"+id+"\n"+my_seq 
	dnafile.write(my_seq+"\n")
dnafile.close()
