#python koda za moj prvi genetic algoritm napisan brez ksnih ml kniznic.
#!!!koda je najbrs trash!!!   ampak dela...
import random
dnatabela = []
scoreboard = []
mutanti = []

kolk_generacij = 20

kolk_zvali = 2000
kolk_genov_se_swapa = 1
kolk_lastnosti_vsak_gen = [10,1,1,1,3,20]          #DNA !!!! (kle poves kako naj zgleda dna teh zivali npr:[4,1,1,4,4,1,1,4,3,4])
#randomnes_v_prezivetju = 5 #to so procenti %%%% // zenkrat nima funkcije
kolk_naj_jih_prezivi = 30 # to so procenti %%%%

kolk_pogost_so_fine_mutacije = 1000 # 1 na 100 npr al pa 1 na 10 moznsot je to tko da ja..
max_randm_vrednost           = 0.1  # od -1 do 1 npr
print "======================================================================================================================="
def createdna(enatabela):
	dna = []
	for x in range(len(kolk_lastnosti_vsak_gen)):
		dna.append(random.uniform(-1,kolk_lastnosti_vsak_gen[x]))
	enatabela.append(dna)

def outworld(creature): # basically trenutno ta outworld favorizera te ka majo visje stevilke v genih, zato ker je tko v izi razporedit jih po "fitu"
#genereraj zivali v igrci vsaki pripada tut svoj dna, ki smo ga ze genererali
	#potem poteka igrca in se razvrstio tko od tega ka je najdl prezivel, do unga kaje najmn prezivel casa
	place = 0
	for x in range(len(scoreboard)):
		#print "notr sm x pa je: ", x ,"  place = x "
		place = x
		#print "sum(scoreboard[x]) <= sum(creature)" ,sum(scoreboard[x]) ," <= ", sum(creature)
		if sum(scoreboard[x]) <= sum(creature):
		#	print "drzi!! , break in zapisi na:", place
			break
		place = x+1
	scoreboard.insert(place,creature) 
	return scoreboard
	#print "scoreboard", scoreboard

def ubij():
	zivi , mrtvi = split_list(scoreboard)  #mrtvi me trenutno se ne zanimajo, mogoc kasnej ksna funkcija...
	return zivi, mrtvi

def split_list(a_list):
    half = int(kolk_zvali * kolk_naj_jih_prezivi / 100)
    return a_list[:half], a_list[half:]

def swap_genes(m1,m2):
	index_gen = [] 
	for x in range(kolk_genov_se_swapa): # kle dobim tabelo z dvema idexoma ki nista enaka aka starsa
		while True:
			tt = random.randint(0,len(m1 if len(m1) < len(m2) else m2)-1) # izbere radnom gen v dnaju
			if tt in index_gen:
				pass
			else:
				break
		index_gen.append(tt)
	#zdej morm swapat na lokacijah iz idex gen
	mutanti.append(m1)     # dodajo se na listo mutantov, to sta starsa, ki se ne muterata
	mutanti.append(m2)
	for x in range(len(index_gen)):
		zam2 = m1[index_gen[x]]
		m1[index_gen[x]] = m2[index_gen[x]]
		m2[index_gen[x]] = zam2

	randm = 0
	if random.uniform(0,kolk_pogost_so_fine_mutacije) == 0: #  to je random mutacija koda, verjetnost da se zgodi je 1 na 100 npr
		index_rand_mutacije = random.uniform(0,len(kolk_lastnosti_vsak_gen)-1)
		randm = random.uniform(-max_randm_vrednost,max_randm_vrednost)

		if m1[index_rand_mutacije]+randm <= kolk_lastnosti_vsak_gen[index_rand_mutacije] and m1[index_rand_mutacije]+randm >= 0:
			m1[index_rand_mutacije] = m1[index_rand_mutacije] + randm
			print "ja  to se zgodi"
		if m2[index_rand_mutacije]+randm <= kolk_lastnosti_vsak_gen[index_rand_mutacije] and m2[index_rand_mutacije]+randm >= 0:
			m2[index_rand_mutacije] = m2[index_rand_mutacije] + randm

	if random.uniform(0,1) == 0:   # dodajo se na listo mutantov, en otrok gre naprej dodal bom se to da so random fine mutacije tko +1 
		mutanti.append(m1)    
	else:
		mutanti.append(m2)


#===============================================================================================================================0
#make new creatures
for x in range(kolk_zvali):
	createdna(dnatabela)

for generacija in range(kolk_generacij):
	print generacija
	#oceni zvali
	for x in range(len(dnatabela)):
		bbb = outworld(dnatabela[x])
	# razdeli na prezivele in mrtve

	zivi , mrtvi = ubij()

	#print "zivi", zivi, len(zivi)
	#gene swap
	while len(zivi) > 0:
		index_m1 = random.randint(0,len(zivi)-1)  #imdex izbere starsa in hrati bosta tadva sla k mutantom brez mutacij
		m1 = zivi[index_m1]
		del zivi[index_m1]

		index_m2 = random.randint(0,len(zivi)-1)
		m2 = zivi[index_m2]
		del zivi[index_m2]
		swap_genes(m1,m2) # nrdi to in jih doda k mutantom
		


	for x in range(kolk_zvali-len(mutanti)): #k mutantom doda se tolk da pridemo nazaj na stevilo zvali, te so cist na novo na random generane.
		createdna(mutanti)

	#print "mutanti", mutanti, len(mutanti)
	dnatabela = mutanti
	mutanti = []
	scoreboard = []

print "scoreboard:  ",bbb, len(bbb)
print "najboljsi: ", bbb[0], sum(bbb[0])

# morm 
