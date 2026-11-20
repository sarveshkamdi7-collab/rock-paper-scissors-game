import random

print('______________________________'*3)



print('ROCK PAPER SCISSOR GAME')
score_player=0
score_pc=0

print('GAME BEGINS ')
choices=['ROCK',"PAPER",'SCISSORS']
while True:
    print('🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦')
    print('🟦1:ROCK 🪨              🟦')
    print('🟦2:PAPER📃             🟦')
    print('🟦3:SCISSOR ✂️           🟦')
    print('🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦 ')


    try:
     choice=int(input('Enter choice between (1-3)  '))
    except ValueError as e:
       print(e)


    while choice <1 or choice>3:
       choice=int(input('Enter valid choice between 1 to 3 '))
    computer_choice=random.randint(1,3)
    chosen_user=choices[choice-1]
    chosen_pc=choices[computer_choice-1]
    print('PLAYER: ',chosen_user)
    print('COMPUTER: ',chosen_pc)
    print()
    if computer_choice==choice:
       print('__TIE__')
    elif (choice==1 and computer_choice==3)or (choice==2 and computer_choice==1)or (choice==3 and computer_choice==2):
       score_player+=1
       print('PLAYER WINS THE GAME 🎉')
       print('Computer have better luck next time ')
    else:
       score_pc+=1
       print('Computer wins the game 🎉')
       print('PLAYER HAVE BETTER LUCK NEXT TIME 👍')

    while True:
       ans=input('DO you want to continue playing (Y/N) : ')
       if ans in ['y','n','Y','N']:
          break
       print('PLEASE Enter input in (y/n) or (Y/N) form other letters not allowed  ')

    if ans=='n' or ans=='N':
       break

print('Thanks for visiting our site 🙂')
       



print('______________________________'*3)
