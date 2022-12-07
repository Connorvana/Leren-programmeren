from random import randint


play = True
ronde = 1
bomb = randint(1,10)

while play == True:
    guess= input('ronde '+str(ronde)+' :op welk getal denkt u dat de bom niet ligt?')
   
    if int(guess) == bomb:
        play = False
        print('BOOM! game over. u heef een score van', ronde-1 'gehaald')

    ronde = ronde + 1 
    vraag= input('wilt u naar ronde '+str(ronde)+'?(y/n)').lower()
    if vraag == 'y':
        ronde = ronde + 1
else:
    print('u heeft een score van:', ronde-1)

        