#neural net  to bo pomojm treba met class, zato da lahko vsaka zival poklice tole vse
#amm caki kaj bo kle neural net spremenil ce mam gene? 
#okej za vajo bo to 
import math
import numpy as np

bias = 1
input_razdalja = 1
input_smer = 1
input_score = 1
zivali = [0.8086256867282475, 0.9956906516133281, 0.9960460607161905, 0.7143669477723541, 0.5927253642401962, 0.9649392052037664, 0.8883692484792839, 0.9891436494966412, 0.8986454571811485, 0.6534345835769122, 0.9131490989676732, 0.8398901523301883, 0.9208055644316344, 0.8737832776456874, 0.9877721555355826, 0.6965767890440947, 0.8594002208598754, 0.6764857864105821]
#zivali = [1,1,1, 1,1,1, 1,1,1, 1,1,1, 1,1,1, 1,1,1]
weights = []
kolk_skrith_n = 3 # o nodih se to govori
#restructre weights
for x in range(0,len(zivali),kolk_skrith_n):
	hhh = []
	for y in range(kolk_skrith_n):
		hhh.append(zivali[x+y])
	weights.append(hhh)

print "weights", weights

def neuralnet(teze,input_razdalja,input_smer,input_score):
	sloj = []
	sloj.append(input_razdalja)
	sloj.append(input_smer)
	sloj.append(input_score)
	# zdej je treba dot product narest med slojem in prvimi tremi seti weightsi, da dobim nasednje tri hiddne node
	nodes = []
	for x in range(kolk_skrith_n):
		sloj2 = skritinode = act(np.dot(sloj,teze[x]))
	for x in range(kolk_skrith_n):
		print "teze", teze[x+kolk_skrith_n]
		skritinode = np.dot(sloj2, teze[x+kolk_skrith_n])
		print "skritinode",skritinode
		nodes.append(skritinode)
	print "nodes:  ",nodes





def act(nev):
	print "nev:  ",nev
	return 1/(1+math.e**-nev)





neuralnet(weights, input_razdalja, input_smer, input_score)