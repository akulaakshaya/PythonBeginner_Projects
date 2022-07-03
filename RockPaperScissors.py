import random
def play():
    user=input("Enter Your Choice ? \n 'r' for Rock , \n 'p' for Paper , \n 's' for Scissors : ")
    computer=random.choice(['r','p','s'])
    if user== computer:
        return print('Tie');
    if is_win(user,computer):
        return print('You Won!');
    return print('You Lost');
def is_win(user,computer):
    if((user=='r' and computer=='s')  or (user=='p' and computer=="r" ) or(user=='s' and computer=="p")):
        return True;
play()    