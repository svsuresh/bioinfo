from Bio.Alphabet import IUPAC
import random
from datetime import datetime

n=int(input("type the length of the sequence: "))
j=int(input("type the number of sequences: "))

sequnce=IUPAC.IUPACProtein.letters.upper()

# print(sequnce)
# print(list(sequnce))
# print (random.choice(sequnce))
# print (random.sample(sequnce,2))
# print (''.join(random.sample(sequnce,4)))

pfile = open("aasequence_"+datetime.now().strftime("%Y%m%d_%H%M%S")+".fa", "a")
for j in range(j):
	my_seq=''.join(random.choice(sequnce) for i in range(n))
	id="seq "+str(j+1)
	my_seq = ">"+id+"\n"+my_seq 
	pfile.write(my_seq+"\n")
pfile.close()
