play_more=True
while play_more:
    print('you are a knight, a army of ogres and trolls are attacking the kingdom. you are part of the kings grand army.')
       selection = int(input('what position do you take,1 frontline or 2 rear guard.'))
    if selection == 1: 
        print('you take a frontline position and ready your sword, you fight hard but are slain by a 20 foot tall ogre. THE END')
    if selection == 2:
        print('you take your position, the front line troops are chewed up but overpower the ogres and trolls.')
    if selection == 1: break
    select =int(input('do you 3 go home or 4 march with the army .'))
    if select ==3:
            print('as you walk home one of the army trolls hiding in the feilds after the battle slays you. THE END')
    if select==4 :
            print('you march for weeks until you reach the troll land, a enemy army is sighted by scouts you arm up and prepare for battle.')
    if select == 3: break
    dinoforce = int(input(' what weapon do you take 5 a sword or 6 spear'))
    if dinoforce == 5:
                print('you rush into battle and slay many trolls and ogers before the enemy scatters and runs off.')
    if dinoforce== 6:
                print('you charge ahead spear ready. soon the head of your spear is cut of and you are slain. THE END')
    if dinoforce == 6: break
    bob = int(input('what do you do, 7 march on the troll capital or 8 go home'))
    if bob == 7:
                    print('you bravely attack on the front line and slay the troll king him self. you are made heir of the kindom and for all of your rule you are never trobled by invaders. GOOD JOB, YOU WON THE GAME')
    if bob == 8:
                    print ('you join a group of soldiers going home but you are attacked by trolls and are slain. THE END.')
    if bob == 8: break
    uinput = input ('type y if you want to play agian or q if you want to quit ')
    play_more =uinput.lower() == 'y'
    if uinput =='q':
        break
