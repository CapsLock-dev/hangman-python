import random

words = ["python", "kotlin", "java", "javascript"]
running = True

while running:
	print("H A N G M A N")
	option = input('Type "play" to play the game, "exit" to quit:')
	if option == "play":
		#Выбор рандомного слова, откат попыток и использованных букв
		correct_word = random.choice(words)
		word = "-" * len(correct_word)
		tries = 8
		ascii_lowercase = "abcdefghijklmnopqrstuvwxyz"
		used_letters = set()

		print()
		print(word)
		while True:
			letter = input("Input a letter:")
	
			#Проверка на правильность ввода
			if len(letter) != 1:
				print("You should input a single letter")
			elif letter not in ascii_lowercase:
				print("It is not an ASCII lowercase letter")
			elif letter in used_letters:
				print("You already typed this letter")
			else:
				#Сравнение ввода и букв из слова
				if letter in correct_word:
					for i in range(0, len(correct_word)):
						x = correct_word.find(letter, i, i+1)
						if x != -1:
							word = word[:x] + letter + word[x+1:]
				else:
					tries -= 1
					print("No such letter in the word")

				#Проверка отгадал ли игрок слово или у него закончились попытки
				if word == correct_word:
					print(f"You guessed the word {correct_word}!")
					print("You survived!")
					break
				elif tries < 1:
					print("You are hanged!")
					break

			used_letters.add(letter)
			print()
			print(word)
	elif option == "exit":
		break
	else:
		continue