import random
'''
Dealer Ai modle actually contains probablities for diffrent number summaries and according to that randomize between probabilities
the chances of hit or stand
chance that i will pre make
each number will contain probabilities for stand or hit

the function will take in a number between 1 to 20 inclucive and check the probabilities set for him by randomizing
eventually it will return True for Hit and  False for stand
'''
def hit_answer_rules(cards_sum):
	if cards_sum < 17:
		return True
	else:
		return False

def hit_answer_challenge(cards_sum):
	'''
	this play is not according to the rules but allows a more intresting and challenging game.
	takes in only a number between 1-20 inclucive and returns boolean
	'''
	if cards_sum == 20 and cards_sum < 21:
		#for 20 , 5% to ask for hit. because it is very unlikel for a human to do so
		if random.randint(0,100) in range(0,5):
			return True
		else:
			return False
	elif cards_sum == 19 and cards_sum < 21:
		#for 19 , 10% to ask for hit.
		if random.randint(0,100) in range(0,10):
			return True
		else:
			return False
	elif cards_sum == 18 and cards_sum < 21:
		#for 18 , 15% to ask for hit
		if random.randint(0,100) in range(0,15):
			return True
		else:
			return False
	elif cards_sum == 17 and cards_sum < 21:
		#for 17 , 30% to ask for hit
		if random.randint(0,100) in range(0,30):
			return True
		else:
			return False
	elif cards_sum == 16 and cards_sum < 21:
		#for 16 , 40% becoming more likely to ask for hit
		if random.randint(0,100) in range(0,40):
			return True
		else:
			return False
	elif cards_sum == 15 and cards_sum < 21:
		#for 15 , 60%
		if random.randint(0,100) in range(0,60):
			return True
		else:
			return False
	elif cards_sum == 14 and cards_sum < 21:
		#for 14: 80%
		if random.randint(0,100) in range(0,80):
			return True
		else:
			return False
	elif cards_sum in range(10,14) and cards_sum < 21:
		#for 10-13 , 92%
		if random.randint(0,100) in range(0,92):
			return True
		else:
			return False
	elif cards_sum in range(8,10) and cards_sum < 21:
		#for  8,9 95%
		if random.randint(0,100) in range(0,95):
			return True
		else:
			return False
	elif cards_sum in range(0,8)  and cards_sum < 21:
		#(100%)
		return True
	else:
		return False

def ace_ans(cards_sum):
	'''
	check if is possible to use ace is 11
	'''
	if cards_sum+10 in range(17,22):
		return True
	else:
		return False


if __name__ == '__main__':
	n = input('enter a number between 1-20: ')
	if get_answer(n) is True:
		print('True')
	else:
		print('False')