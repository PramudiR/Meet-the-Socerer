import time
import replit
import colorama as cr


def affirm():
  input('Click [Enter] to continue ')


def clear():
  replit.clear()


def score():
  print('Your score,\n' + f'Curious: {curious} \n' +
        f'Thoughtful: {thoughtful} \n' + f'Lovely: {lovely} \n' +
        f'Brave: {brave} \n')


def rank():
  rank = thoughtful + curious + lovely + brave
  if (rank == 4):
    print(
      f'{cr.Fore.MAGENTA} Your Rank, \n \t Newbie Explorer ! {cr.Fore.RESET}')
  if (rank > 4 and rank < 8):
    print(f'{cr.Fore.MAGENTA} Your Rank, \n \t Explorer ! {cr.Fore.RESET}')
  if (rank == 8):
    print(f'{cr.Fore.MAGENTA} Your Rank, \n \t Adventurer ! {cr.Fore.RESET}')
  if (rank > 8 and rank < 12):
    print(f'{cr.Fore.MAGENTA} Your Rank, \n \t Young Wizard ! {cr.Fore.RESET}')
  if (rank == 12):
    print(f'{cr.Fore.MAGENTA} Your Rank, \n \t Wizrd ! {cr.Fore.RESET}')


#-  -  -  start  -  -  #
print(
  f'{cr.Fore.GREEN} Before going further be warned your journey is greately affected by your choices. Yet magic can do changes too.\n \n Each choice may or may not add scores about 4 aspects of your personality. \n At the end you will know more about yourself.{cr.Fore.RESET}'
)
print(
  f'{cr.Fore.YELLOW} Also your rank in the game go up as follows, \n\n Level 1 --> Newbie Explorer\n Level 2 --> Explorer\n Level 3 --> Adventurer\n Level 4 --> Young Wizard\n Level 5 --> Wizrd \n {cr.Fore.RESET}'
)
affirm()
clear()
#-  -  - score sheme  -  -  #
curious = 0
thoughtful = 0
lovely = 0
brave = 0

#-  -  -  select the role  -  -  #
print(
  f'{cr.Fore.GREEN} You are, \n \n \t (1) a brave young boy named Jack who lived in a small village nestled in the rolling hills of the countryside. 👦 \n \n \t (2) a young girl named Sophie who is kind and curious, and loved nothing more than to explore the fields and forests around her home. 👧 \n {cr.Fore.RESET}'
)

role = None
while role != ['1', '2']:
  role = input('Choose your role: ')
  if (role == '1'):
    print('Here we go Jack! \n')
    thoughtful += 1
    brave += 1
    break
  elif (role == '2'):
    print('Hello Sophie, \n')
    lovely += 1
    curious += 1
    break
  else:
    print('Your input should be either 1 or 2. \n')

affirm()
clear()
#  -  -  -  trial 1  -  -  -  #
print(
  f'{cr.Fore.GREEN} One day when you were wandering through the woods,\n \n \t (1) You stumbled upon a beautiful clearing filled with wildflowers. 🌻🌼🌷 \n \n \t (2) You came upon a clearing where you saw an old man sitting on a tree stump. 👴 \n {cr.Fore.RESET}'
)

trial1 = None
while trial1 != ['1', '2']:
  trial1 = input('Choose what happened: ')
  if (trial1 == '1'):
    print(
      f'{cr.Fore.GREEN} As you walked through the clearing, you saw a small, sparkling pond and a tiny cottage nestled among the trees. 🛖 \n \n {cr.Fore.RESET}'
    )
    lovely += 1
    break
  elif (trial1 == '2'):
    print(
      f'{cr.Fore.GREEN} The old man had a long, white beard and a kind face, and he was surrounded by a strange, sparkling aura. 🪄 \n \n {cr.Fore.RESET}'
    )
    curious += 1
    brave += 1
    break
  else:
    print('Your input should be either 1 or 2. \n')

affirm()
clear()
#  -  -  -  trial 2  -  -  -  #
trial2 = None
if (trial1 == '1'):  # cottage
  print(
    f'{cr.Fore.GREEN} You were fascinated by the cottage, \n \n \t (1) You decided to have a closer look.\n \n \t (2) You decided not ot go closer.\n {cr.Fore.RESET}'
  )
  while trial2 != ['1', '2']:
    trial2 = input('Choose what would you do: ')
    if (trial2 == '1'):
      print(
        f'{cr.Fore.GREEN} As you approached the door, you heard a faint humming sound coming from inside. 🎶 \n {cr.Fore.RESET}'
      )
      curious += 1
      break
    elif (trial2 == '2'):
      print(
        f'{cr.Fore.GREEN} When you turn around to go back, You heard a sound. 🤨 \n {cr.Fore.RESET}'
      )
      thoughtful += 1
      break
    else:
      print('Your input should be either 1 or 2. \n')

else:  # old man
  print(
    f'{cr.Fore.GREEN} "Hello, young man," the old man said with a smile. "What brings you to this clearing?" \n \n You answered,\n \n \t (1) "None of your business, Old bones." 😠 \n \n \t (2) "I was just exploring, I love to wander through the woods and see what I can find." 🙂 \n {cr.Fore.RESET}'
  )
  while trial2 != ['1', '2']:
    trial2 = input('Choose how would you answer: ')
    if (trial2 == '1'):
      print(
        f'{cr.Fore.MAGENTA} It truns out to be that old man was a socerer. Now that you made him angry, he turned you into a stone. 🪨\n {cr.Fore.RESET}'
      )
      print('Gamw Over !\n')
      time.sleep(0.5)
      score()
      rank()
      exit('You are welcome to play again 🤠\n ')
    elif (trial2 == '2'):
      print(
        f'{cr.Fore.GREEN} The old man nodded. "I, too, have always had a love of exploration," he said. 👴\n  {cr.Fore.RESET}'
      )
      lovely += 1
      brave += 1
      break
    else:
      print('Your input should be either 1 or 2. \n')

#--------------Level 1 Completed------------#
print(f'{cr.Fore.MAGENTA} Level 1 Completed. 🫡 \n {cr.Fore.RESET}')
score()
rank()
affirm()
clear()
#  -  -  -  trial 3  -  -  -  #
trial3 = None
if (trial1 == '1' and trial2 == '1'):  # old woman
  print(
    f'{cr.Fore.GREEN} You knocked gently and called out, "Hello? Is anyone there?"\n The humming stopped, and a soft voice answered, "Yes, dear. Come in." \n \n \t (1) You went inside. 🤠 \n \n \t (2) "Not untill you tell me who you are." You said back. 🤨 \n \n {cr.Fore.RESET}'
  )
  while trial3 != ['1', '2']:
    trial3 = input('Choose what would you do: ')
    if (trial3 == '1'):
      print(
        f'{cr.Fore.GREEN}The cottage was small and cozy, filled with the warm glow of candlelight. 🕯️ \n {cr.Fore.RESET}'
      )
      brave += 1
      curious += 1
      break
    elif (trial3 == '2'):
      print(
        f'{cr.Fore.GREEN}"I am a healer," the same voice replied. 🧝 \n {cr.Fore.RESET}'
      )
      thoughtful += 1
      brave += 1
      break
    else:
      print('Your input should be either 1 or 2. \n ')

elif (trial1 == '1' and trial2 == '2'):  # old woman
  print(
    f'{cr.Fore.GREEN} Someone called you. "Hello? Is anyone there?"\n \n \t (1) You silently walked away from the cottage. 🛖 \n \n \t (2) "Yes, I am from the near by village. Who are you?" 😊 \n \n {cr.Fore.RESET}'
  )
  while trial3 != ['1', '2']:
    trial3 = input('Choose what would you do: ')
    if (trial3 == '1'):
      print(
        f'{cr.Fore.MAGENTA} It truns out that you are not quite fit for an adventure. 😶‍🌫️ \n {cr.Fore.RESET}'
      )
      print('Gamw Over !\n')
      time.sleep(0.5)
      score()
      rank()
      exit('You are welcome to play again 🤠\n')
    elif (trial3 == '2'):
      print(f'{cr.Fore.GREEN} "I am a healer. You may come inside."\n')
      brave += 1
      thoughtful += 1
      break
    else:
      print('Your input should be either 1 or 2.\n')
else:  # old man
  print(
    f'{cr.Fore.GREEN} "I studied magic and socery in my whole life and you seem to be a kind and brave soul."\n "Would you like to learn some?" The old man asked. \n \n \t (1) "Yes of course, Thnak you sir." 😍\n \n \t (2) "No, thank you sir. Magic is scary." 🤗 \n \n {cr.Fore.RESET}'
  )
  while trial3 != ['1', '2']:
    trial3 = input('Choose what would you do: ')
    if (trial3 == '1'):
      print(
        f'{cr.Fore.GREEN} "Very well then, meet me here tomorrow morning at 7." 🌄🕗 \n {cr.Fore.RESET}'
      )
      curious += 1
      brave += 1
      break
    elif (trial3 == '2'):
      print(
        f'{cr.Fore.GREEN} "Hmm, It seems you need more time to think. \n You can find me here if you change your mind." 🕗 \n {cr.Fore.RESET}'
      )
      thoughtful += 1
      break
    else:
      print('Your input should be either 1 or 2.\n')

affirm()
clear()
#   -  -  - trial 4 and 5  -  -  -  #
trial4 = None
trial5 = None
if (trial1 == '1' and trial2 == '1' and trial3 == '1'):
  print(
    f'{cr.Fore.GREEN} An old woman sat at a table, surrounded by pots of herbs and bottles of strange-looking liquids. "Who are you?" you asked. \n \n The old woman smiled and said, \n \n \t (1) "I am a healer," "I learn and discover medicine from nature." 🧝 \n \n \t (2) "I am a sorcerer and what brings you here?" 🧙‍♀️ \n \n {cr.Fore.RESET}'
  )
  while trial4 != ['1', '2']:
    trial4 = input('Choose what did she said: ')
    if (trial4 == '1'):
      thoughtful += 1
      curious += 1
      print(
        f'{cr.Fore.GREEN} "Really, I came from the near by village. Can you teach me some healing magic?" You asked. She thought for a moment and said,\n \n \t (1) "I can teach you but will have to work very hard to master it." 📚 \n \n \t (2) "Healing magic is very hard to learn, How about I give you some potion bottles instead." 🍶 \n \n  {cr.Fore.RESET}'
      )
      while trial5 != ['1', '2']:
        trial5 = input('Choose your answer carefully: ')
        if (trial5 == '1'):
          thoughtful += 1
          lovely += 1
          curious += 1
          print(f'{cr.Fore.MAGENTA} Level 2 Completed. 🫡 \n {cr.Fore.RESET}')
          print(
            f'{cr.Fore.YELLOW} Couple of years later you have become a successful healer 🍃🪄\n \n {cr.Fore.RESET}'
          )
          score()
          rank()
          break
        elif (trial5 == '2'):
          curious += 1
          print(
            f'{cr.Fore.MAGENTA} It was a total hazard when you tried to use potions without proper knowledge. {cr.Fore.RESET}'
          )
          print('Gamw Over !\n')
          time.sleep(0.5)
          score()
          rank()
          exit('You are welcome to play again 🤠\n ')
        else:
          print('Your input should be either 1 or 2.\n')
      break
    elif (trial4 == '2'):
      print(
        f'{cr.Fore.MAGENTA} "I did not mean to disturbe you Madam, but your home was strangly fasinating." \n You said to get on the good side of the sorcerer but she saw right though you and turn you into a house cat. 🙀 \n {cr.Fore.RESET}'
      )
      brave += 1
      curious += 1
      print('Gamw Over !\n')
      time.sleep(0.5)
      score()
      rank()
      exit('You are welcome to play again 🤠\n ')
      break
    else:
      print('Your input should be either 1 or 2.\n')

elif (trial1 == '1' and trial2 == '1' and trial3 == '2'):
  print('x')

elif (trial1 == '1' and trial2 == '2' and trial3 == '2'):
  print('y')

elif (trial1 == '2' and trial2 == '2' and trial3 == '1'):
  print('z')

else:
  print('100')
