from RobotArm import RobotArm

robotArm = RobotArm('exercise 12')

# Jouw python instructies zet je vanaf hier:

y = 1 
for i in range(8):
    robotArm.moveRight()

for x in range(9):
    robotArm.grab()
    color = robotArm.scan()

   
    y= y + 1 

    if color == "red":
        for c in range(y-1):
            robotArm.moveRight()
        robotArm.drop()

        for a in range(y):
            robotArm.moveLeft()
    else:
        robotArm.drop()
        robotArm.moveLeft()





# Na jouw code wachten tot het sluiten van de window:
robotArm.wait()