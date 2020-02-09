import random
from time import sleep
print("""
                COMMAND-LINE CRICKET
                                    """)
# asking name for furthur use
name=input(':> What is ur name ? ')
sleep(0.5)
print(":> OK !  We will have a toss now.....")
sleep(1)


toss_val=("head","tail","head","tail","head","tail","head","tail")
toss_val=random.choice(toss_val)
toss=input(":> What will you take ? (head / tail) : ").lower()
sleep(0.2)
print('\n tossing....')
sleep(1)
print(" It's a ","\033[41m",toss_val,"\033[0m")
count=0
score=0

# if the user wins the toss
if toss_val in toss:
	print("\033[04m","You won the toss...","\033[0m")
	choose=input("\n:> What you want to choose (bat / ball) : ").lower()
	if "bat" in choose:
		try:
			wickets=int(input(":> OF How many wickets you want to play : "))
		except:
			print("Invalid value Entered ! ")
			exit()
		while count!=wickets:
			comp=random.randint(1,6)
			sleep(0.1)
			try:
				user=int(input("\n:> YOU - "))
			except:
				continue
			if user >6:
				print("# Run cannot be greater than 6....")
				continue
			sleep(0.2)
			print(":< COMPUTER - ",comp)
			score=score+user
			
			if user == comp:
				count=count+1
				print("\033[01m","\033[31m","\t\t\tOUT ! ",f"\nTotal Wicket : {count}/{wickets}","\033[0m")
				score=score-user
								
			print("\033[32m","\t\t\t\tYour Score : ",score,"\033[0m")
		sleep(0.3)
		print(f"\n:< You are out with a score of |{score}|")
		# comp. batting starts
		print(':< NOW, Its my turn to bat....')
		score1 =0
		count=0
		while count!=wickets:
			comp=random.randint(1,6)
			sleep(0.1)
			try:
				user=int(input('\n:> YOU - '))
			except:
				continue
			if user>6:
				print("# Run cannot be greater than 6....")
				continue
				
			sleep(0.2)
			print(":< COMPUTER - ",comp)
			score1=score1+comp
			
			
			if user == comp:
				count=count+1
				print("\033[01m","\033[31m","\t\t\tOUT ! ",f"\nTotal Wicket : {count}/{wickets}","\033[0m")
				score1=score1-user
				
			print("\033[32m","\t\t\t\tComputer Score : ",score1,"\033[0m")
			if score1>score:
				break
		sleep(0.4)
		print("$ Your Score",score)
		print("$ Computer Score",score1)
		sleep(0.5)
		if score>score1:
			print("\ncongrats! , You won...")
		else:
			print("\nComputer won the match....")
			print("It seems You are a big LOsEr....☆KEEP IT UP☆")
	

	
	
	elif "ball" in choose:
		try:
			wickets=int(input(":> OF How many wickets you want to play : "))
		except:
			print("Invalid value Entered ! ")
			exit()
		sleep(0.3)
		print("\nSO, First Its my turn to bat...")
		score1 =0
		count=0
		while count!=wickets:
			comp=random.randint(1,6)
			sleep(0.1)
			try:
				user=int(input('\n:> YOU - '))
			except:
				continue
			if user>6:
				print("# Run cannot be greater than 6....")
				continue
				
			sleep(0.2)
			print(":< COMPUTER - ",comp)
			score1=score1+comp
			
			
			if user == comp:
				count=count+1
				print("\033[01m","\033[31m","\t\t\tOUT ! ",f"\nTotal Wicket : {count}/{wickets}","\033[0m")
				score1=score1-user
				
			print("\033[32m","\t\t\t\tComputer Score : ",score1,"\033[0m")
		print(f"\n:< My ToTal score |{score1}|")
		print('\n:> NOW, Its your turn to bat....')
		score=0
		count=0
		while count!=wickets:
			comp=random.randint(1,6)
			sleep(0.1)
			try:
				user=int(input("\n:> YOU - "))
			except:
				continue
			if user >6:
				print("# Run cannot be greater than 6....")
				continue
			sleep(0.2)
			print(":< COMPUTER - ",comp)
			score=score+user
			
			if user == comp:
				count=count+1
				print("\033[01m","\033[31m","\t\t\tOUT ! ",f"\nTotal Wicket : {count}/{wickets}","\033[0m")
				score=score-user
								
			print("\033[32m","\t\t\t\tYour Score : ",score,"\033[0m")
			if score>score1:
				break
		sleep(0.4)
		print("$ Computer Score",score1)
		print("$ Your Score",score)
		sleep(0.5)
		if score>score1:
			print("\nYou beat the ComPuter\ncongrats! , You won...")
		else:
			print("\nCoMpuTer won the match....\nIt seems You are a big LOsEr....☆KEEP IT UP☆")

# if the user looses the match
elif toss_val not in toss:
	print(" You Lose the Toss.../")
	comp_choose=("BAT","BALL","BAT","BALL","BAT","BALL","BALL","BAT")
	comp_choose=random.choice(comp_choose)
	print("\033[04m","\n Umm...I want to",comp_choose,"\033[0m")		
	
	if comp_choose=="BAT":
		try:
			wickets=int(input(":> OF How many wickets you want to play : "))
		except:
			print("Invalid value Entered ! ")
			exit()
		sleep(0.3)
		print("\nSO, First Its my turn to bat...")
		score1 =0
		count=0
		while count!=wickets:
			comp=random.randint(1,6)
			sleep(0.1)
			try:
				user=int(input('\n:> YOU - '))
			except:
				continue
			if user>6:
				print("# Run cannot be greater than 6....")
				continue
				
			sleep(0.2)
			print(":< COMPUTER - ",comp)
			score1=score1+comp
			
			
			if user == comp:
				count=count+1
				print("\033[01m","\033[31m","\t\t\tOUT ! ",f"\nTotal Wicket : {count}/{wickets}","\033[0m")
				score1=score1-user
				
			print("\033[32m","\t\t\t\tComputer Score : ",score1,"\033[0m")
		print(f"\n:< My ToTal score |{score1}|")
		print('\n:> NOW, Its your turn to bat....')
		score=0
		count=0
		while count!=wickets:
			comp=random.randint(1,6)
			sleep(0.1)
			try:
				user=int(input("\n:> YOU - "))
			except:
				continue
			if user >6:
				print("# Run cannot be greater than 6....")
				continue
			sleep(0.2)
			print(":< COMPUTER - ",comp)
			score=score+user
			
			if user == comp:
				count=count+1
				print("\033[01m","\033[31m","\t\t\tOUT ! ",f"\nTotal Wicket : {count}/{wickets}","\033[0m")
				score=score-user
								
			print("\033[32m","\t\t\t\tYour Score : ",score,"\033[0m")
			if score>score1:
				break
		sleep(0.4)
		print("$ Computer Score",score1)
		print("$ Your Score",score)
		sleep(0.5)
		if score>score1:
			print("\nYou beat the ComPuter\ncongrats! , You won...")
		else:
			print("\nCoMpuTer won the match....\nIt seems You are a big LOsEr....☆KEEP IT UP☆")
			
	elif comp_choose=="BALL":
		try:
			wickets=int(input(":> OF How many wickets you want to play : "))
		except:
			print("Invalid value Entered ! ")
			exit()
		print("Its First Your turn to bat...")
		while count!=wickets:
			comp=random.randint(1,6)
			sleep(0.1)
			try:
				user=int(input("\n:> YOU - "))
			except:
				continue
			if user >6:
				print("# Run cannot be greater than 6....")
				continue
			sleep(0.2)
			print(":< COMPUTER - ",comp)
			score=score+user
			
			if user == comp:
				count=count+1
				print("\033[01m","\033[31m","\t\t\tOUT ! ",f"\nTotal Wicket : {count}/{wickets}","\033[0m")
				score=score-user
								
			print("\033[32m","\t\t\t\tYour Score : ",score,"\033[0m")
		sleep(0.3)
		print(f"\n:< You are out with a score of |{score}|")
		# comp. batting starts
		print(':< NOW, Its my turn to bat....')
		score1 =0
		count=0
		while count!=wickets:
			comp=random.randint(1,6)
			sleep(0.1)
			try:
				user=int(input('\n:> YOU - '))
			except:
				continue
			if user>6:
				print("# Run cannot be greater than 6....")
				continue
				
			sleep(0.2)
			print(":< COMPUTER - ",comp)
			score1=score1+comp
			
			
			if user == comp:
				count=count+1
				print("\033[01m","\033[31m","\t\t\tOUT ! ",f"\nTotal Wicket : {count}/{wickets}","\033[0m")
				score1=score1-user
				
			print("\033[32m","\t\t\t\tComputer Score : ",score1,"\033[0m")
			if score1>score:
				break
		sleep(0.4)
		print("$ Your Score",score)
		print("$ Computer Score",score1)
		sleep(0.5)
		if score>score1:
			print("\ncongrats! , You won...")
		else:
			print("\nComputer won the match....")
			print("It seems You are a big LOsEr....☆KEEP IT UP☆")
		          
