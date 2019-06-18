left = ['A', 'K']
right = ['Q', 'J']
player1 = [left, right,'a','b']
print player1
player2 = player1
import copy

player3 = copy.copy(player1) # duplicate parameter
player4 = copy.deepcopy(player1) #duplicate parameter and it's containing object
print hex(id(player1)), hex(id(player2)), hex(id(player3)), hex(id(player4))
print player1, player2, player3, player4
left[0] = 'JOKER'
#left[2] = 'asdf'
print player1, player2, player3, player4
player1.append('10')
print player1, player2, player3, player4