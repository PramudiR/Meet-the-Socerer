import time
import replit
import colorama as cr


def affirm():
  input('Click [Enter] to continue ')


def clear():
  replit.clear()


#-  -  -  start  -  -  #
print(
  f'{cr.Fore.GREEN} Before going further be warned your journey is greately affected by your choices. Yet magic can do changes too.\n Each choice may or may not add scores about 4 aspects of your personality. At the end you will know more about yourself.{cr.Fore.RESET}'
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
  f'{cr.Fore.GREEN} You are, \n (1) a brave young boy named Jack who lived in a small village nestled in the rolling hills of the countryside. 👦 \n (2) a young girl named Sophie who is kind and curious, and loved nothing more than to explore the fields and forests around her home. 👧 \n {cr.Fore.RESET}'
)

role = None
while role != ['1', '2']:
  role = input('Choose your role: ')
  if (role == '1'):
    print('Here we go Jack!')
    thoughtful += 1
    break
  elif (role == '2'):
    print('Hello Sophie,')
    lovely += 1
    break
  else:
    print('Your input should be either 1 or 2.')

affirm()
clear()
#  -  -  -  trial 1  -  -  -  #
print(
  f'{cr.Fore.GREEN} One day when you were wandering through the woods,\n (1) You stumbled upon a beautiful clearing filled with wildflowers. 🌻🌼🌷 \n (2) You came upon a clearing where you saw an old man sitting on a tree stump. 👴 \n {cr.Fore.RESET}'
)

trial1 = None
while trial1 != ['1', '2']:
  trial1 = input('Choose what happened: ')
  if (trial1 == '1'):
    print(
      f'{cr.Fore.GREEN} As you walked through the clearing, you saw a small, sparkling pond and a tiny cottage nestled among the trees. 🛖 \n {cr.Fore.RESET}'
    )
    lovely += 1
    break
  elif (trial1 == '2'):
    print(
      f'{cr.Fore.GREEN} The old man had a long, white beard and a kind face, and he was surrounded by a strange, sparkling aura. 🪄 \n {cr.Fore.RESET}'
    )
    curious += 1
    break
  else:
    print('Your input should be either 1 or 2.')

affirm()
clear()
#  -  -  -  trial 2  -  -  -  #
trial2 = None
if (trial1 == '1'):  # cottage
  print(
    f'{cr.Fore.GREEN} You were fascinated by the cottage, \n (1) You decided to have a closer look.\n (2) You decided not ot go closer.\n {cr.Fore.RESET}'
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
      break
    else:
      print('Your input should be either 1 or 2.')

else:  # old man
  print(
    f'{cr.Fore.GREEN} "Hello, young man," the old man said with a smile.\n "What brings you to this clearing?" You answered,\n (1) "None of your business, Old bones." 😠 \n (2) "I was just exploring, I love to wander through the woods and see what I can find." 🙂 \n {cr.Fore.RESET}'
  )
  while trial2 != ['1', '2']:
    trial2 = input('Choose how would you answer: ')
    if (trial2 == '1'):
      print(
        f'{cr.Fore.MAGENTA} It truns out to be that old man was a socerer. Now that you made him angry, he turned you into a stone. 🪨\n {cr.Fore.RESET}'
      )
      print('Gamw Over !\n')
      time.sleep(0.5)
      print('Your score,\n' + f'Curious: {curious} \n' +
            f'Thoughtful: {thoughtful} \n' + f'Lovely: {lovely} \n' +
            f'Brave: {brave} ')
      exit('You are welcome to play again 🤠')
    elif (trial2 == '2'):
      print(
        f'{cr.Fore.GREEN} The old man nodded. "I, too, have always had a love of exploration," he said. 👴 {cr.Fore.RESET}'
      )
      lovely += 1
      break
    else:
      print('Your input should be either 1 or 2.')

affirm()
clear()
#  -  -  -  trial 3  -  -  -  #
trial3 = None
if (trial1 == '1' and trial2 == '1'):  # old woman
  print(
    f'{cr.Fore.GREEN} You knocked gently and called out, "Hello? Is anyone there?"\n The humming stopped, and a soft voice answered, "Yes, dear. Come in." \n (1) You went inside. 🤠 \n (2) "Not untill you tell me who you are." You said back. 🤨 \n {cr.Fore.RESET}'
  )
  while trial3 != ['1', '2']:
    trial3 = input('Choose what would you do: ')
    if (trial3 == '1'):
      print(
        f'{cr.Fore.GREEN}The cottage was small and cozy, filled with the warm glow of candlelight. 🕯️ {cr.Fore.RESET}'
      )
      brave += 1
      break
    elif (trial3 == '2'):
      print(
        f'{cr.Fore.GREEN}"I am a healer," the same voice replied. 🧝{cr.Fore.RESET}'
      )
      thoughtful += 1
      break
    else:
      print('Your input should be either 1 or 2.')

elif (trial1 == '1' and trial2 == '2'):  # old woman
  print(
    f'{cr.Fore.GREEN} Someone called you. "Hello? Is anyone there?"\n (1) You silently walked away from the cottage. 🛖 \n (2) "Yes, I am from the near by village. Who are you?" 😊 \n {cr.Fore.RESET}'
  )
  while trial3 != ['1', '2']:
    trial3 = input('Choose what would you do: ')
    if (trial3 == '1'):
      print(
        f'{cr.Fore.MAGENTA} It truns out that you are not quite fit for an adventure. 😶‍🌫️ {cr.Fore.RESET}'
      )
      print('Gamw Over !\n')
      time.sleep(0.5)
      print('Your score,\n' + f'Curious: {curious} \n' +
            f'Thoughtful: {thoughtful} \n' + f'Lovely: {lovely} \n' +
            f'Brave: {brave} ')
      exit('You are welcome to play again 🤠')
    elif (trial3 == '2'):
      print(f'{cr.Fore.GREEN} "I am a healer. You may come inside."')
      brave += 1
      break
    else:
      print('Your input should be either 1 or 2.')
else:  # old man
  print(
    f'{cr.Fore.GREEN} "I studied magic and socery in my whole life and you seem to be a kind and brave soul."\n "Would you like to learn some?" The old man asked. \n (1) "Yes of course, Thnak you sir." 😍\n (2) "No, thank you sir. Magic is scary." 🤗 \n {cr.Fore.RESET}'
  )
  while trial3 != ['1', '2']:
    trial3 = input('Choose what would you do: ')
    if (trial3 == '1'):
      print(
        f'{cr.Fore.GREEN} "Very well then, meet me here tomorrow morning at 7." 🌄🕗 {cr.Fore.RESET}'
      )
      curious += 1
      brave += 1
      break
    elif (trial3 == '2'):
      print(
        f'{cr.Fore.GREEN} "Hmm, It seems you need more time to think. \n You can find me here if you change your mind." 🕗 {cr.Fore.RESET}'
      )
      thoughtful += 1
      break
    else:
      print('Your input should be either 1 or 2.')

affirm()
clear()
#   -  -  - trial 4  -  -  -  #
