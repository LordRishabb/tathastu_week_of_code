p1run=int(input("Enter run by player 1 in 60 balls:"))
p2run=int(input("Enter run by player 2 in 60 balls:"))
p3run=int(input("Enter run by player 3 in 60 balls:"))
p1s=p1run*100/60
p2s=p2run*100/60
p3s=p3run*100/60
print("Strike rate of player 1=",p1s)
print("Strike rate of player 2=",p2s)
print("Strike rate of player 3=",p3s)
print("Runs of player 1 if he play 60 balls more=",p1run*2)
print("Runs of player 2 if he play 60 balls more=",p2run*2)
print("Runs of player 3 if he play 60 balls more=",p3run*2)
print("Maximum sixes that could be hit by player 1=",p1run//6)
print("Maximum sixes that could be hit by player 2=",p2run//6)
print("Maximum sixes that could be hit by player 3=",p3run//6)
