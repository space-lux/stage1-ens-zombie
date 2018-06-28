import random
import string

Voyelles="aeiouy"
Consonnes="".join(set(string.ascii_lowercase)-set(Voyelles))

def mot(l=6):
	m=""
	pl=random.randint(0,1)
	for i in range(l):
		if (i+pl)%2:
			m+=random.choice(Voyelles)
		else:
			m+=random.choice(Consonnes)
	return m
