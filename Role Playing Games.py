import check

class Character:
  ''' 
  Fields: 
     name(Str) 
     st(Nat)
     hp(Nat)
     max_hp(Nat)
     mp(Nat)
     max_mp(Nat)
     level(Nat)
     
  Requires:  
     st, max_hp are both strictly greater than 0.
  '''
  def __init__(self, new_name, strength, 
               maximumHP, maximumMP):
    '''
    Initializes a Character object self with 
    name new_name, st strength,
    hp and max_hp of maximumHP, and
    mp and max_mp of maximumMP, and
    level should start at 1.
    
    Effects: Mutates self
    
    __init__: Character Str Nat Nat Nat -> None
    Requires
      0 < strength, maximumHP, level
      maximumHP > hp
      maximumMP > mp
    '''
    self.name = new_name
    self.st = strength
    self.hp = maximumHP
    self.max_hp = maximumHP
    self.mp = maximumMP
    self.max_mp = maximumMP
    self.level = 1
    pass

    
  def __eq__(self, other):
    '''
    Returns True if self and other are equal and False otherwise
    
    __eq__: Character Any -> Bool
    '''
    return isinstance(other, Character) and\
           other.name == self.name and\
           other.st == self.st and\
           other.level == self.level and\
           other.hp == self.hp and\
           other.max_hp == self.max_hp and\
           other.mp == self.mp and\
           other.max_mp == self.max_mp
     
  
  def __repr__(self):
    '''
    Returns a string representation of self
    
    __repr__: Character -> Str
    '''
    s1 = '{0.name}\nLevel: {0.level}\nStrength: {0.st}\n'
    s2 = "HP: {0.hp}/{0.max_hp}\nMP: {0.mp}/{0.max_mp}"
    return (s1+s2).format(self)
    pass

  
  def cast_spell(self, cost, damage, enemy):
    '''
    Casts a spell if self is able that requires cost mp to cast and
    deals damage to enemy. A message is printed if the enemy is 
    defeated or there was not enough mp to cast the spell.
    
    Effects: 
       Prints to screen
       Mutates self
       Mutates enemy
    
    cast_spell: Character Nat Nat Character -> None
    
    Examples:
       c = Character("Test", 1, 4, 5)
       e = Character("Test", 1, 4, 5)
       c.cast_spell(3, 10, e) => None
       and e.hp is mutated to 0
       and c.mp is mutated to 2
       and "Enemy defeated" is printed (no quotes).
       
       c = Character("Test", 1, 4, 5)
       e = Character("Test", 1, 4, 5)
       c.cast_spell(13, 10, e) => None
       and "Not enough MP" is printed (no quotes).
       
       c = Character("Test", 1, 4, 5)
       e = Character("Test", 1, 4, 5)
       c.cast_spell(3, 2, e) => None
       and e.hp is mutated to 2
       and c.mp is mutated to 2
    '''
    error_msg = "Not enough MP"
    defeated_msg = "Enemy defeated"
    if cost <= self.mp:
      self.mp -= cost
      enemy.hp -= damage
      if enemy.hp <= 0:
        enemy.hp = 0
        print(defeated_msg)
    else:
      print(error_msg)
    pass


  def level_up(self):
    '''
    Performs a level-up for self. Increase stats 10% plus 1
    via mutation of self.
    
    Effects: Mutates self
    
    level_up: Character -> None
    
    Examples:
       c = Character("Test", 1, 4, 5)
       c.level_up() => None
       and c.level is mutated to 2
       and c.st is mutated to 2
       and c.hp is mutated to 5
       and c.max_hp is mutated to 5
       and c.mp is mutated to 6
       and c.max_mp is mutated to 6
    '''
    self.level += 1
    self.st = self.st + 1 + int(0.1*self.st)
    self.hp = self.hp + int(self.max_hp * 0.1) + 1
    self.mp = self.mp + int(self.max_mp * 0.1) + 1   
    self.max_hp = int(self.max_hp + int(self.max_hp * 0.1) + 1)
    self.max_mp = int(self.max_mp + int(self.max_mp * 0.1) + 1)
    pass
    

def all_punch(players, enemy):
  '''
  Returns None but simulates all the players punching an enemy by given 
  a (listof Character) in players and a single Character in enemy. 
  Each Character in players will hit the enemy and deal damage 
  to them by decreasing their hp by twice the st strength 
  statistic of each individual Character in players. 
  If the enemy runs out of hp, their hp is set to 0 
  and everyone in players levels up (see previous bullet). 
  You may assume enemy is not in players.
  
  Effects: Mutates players and enemy
  
  all_punch: (listof Character) Character -> None
  Requires:
    * enemy is not in players.
    * 0 < strength, maximumHP, level
      maximumHP > hp
      maximumMP > mp
    * st, max_hp are both strictly greater than 0.  
    
  Examples:
  player1 = Character('top', 20, 70, 100)
  player2 = Character('mid', 30, 60, 80)
  player3 = Character('jungle', 25, 90, 80)
  enemy = Character('Irelia', 20, 50, 80)
  L = [player1, player2, player3]
  all_punch(L, enemy) => None
  and player1.level is mutated to 2
      player1.st is mutated to 23
      player1.hp is mutated to 78
      player1.max_hp is mutated to 78
      player1.mp is mutated to 111
      player1.max_mp is mutated to 111
      player2.level is mutated to 2
      player2.st is mutated to 34
      player2.hp is mutated to 67
      player2.max_hp is mutated to 67
      player2.mp is mutated to 89
      player2.max_mp is mutated to 89
      player3.level is mutated to 2
      player3.st is mutated to 28
      player3.hp is mutated to 100
      player3.max_hp is mutated to 100
      player3.mp is mutated to 89
      player3.max_mp is mutated to 89
  '''
  for player in players:
    enemy.hp -= player.st * 2
  if enemy.hp <= 0:
    enemy.hp = 0
    for player in players:
      player.level_up()
    
##Example of testing all_Punch
player1 = Character('Top', 20, 70, 100)
player2 = Character('Mid', 30, 60, 80)
player3 = Character('Jungle', 25, 90, 80)
enemy = Character('Irelia', 20, 50, 80)
L = [player1, player2, player3]
check.expect('Example', all_punch(L, enemy), None)
check.expect('test for mutation', str(player1),\
"Top\nLevel: 2\nStrength: 23\nHP: 78/78\nMP: 111/111")
check.expect('test for mutation', str(player2),\
"Mid\nLevel: 2\nStrength: 34\nHP: 67/67\nMP: 89/89")
check.expect('test for mutation', str(player3),\
"Jungle\nLevel: 2\nStrength: 28\nHP: 100/100\nMP: 89/89")
check.expect('test for mutation', str(enemy),\
"Irelia\nLevel: 1\nStrength: 20\nHP: 0/50\nMP: 80/80")

##Tests of testing all_Punch
a1 = Character("Sion", 1, 20, 7)
enemy = Character('Irelia', 10, 10, 10)
L = [a1]
check.expect('Example', all_punch(L, enemy), None)
check.expect('test for mutation', str(a1),\
"Sion\nLevel: 1\nStrength: 1\nHP: 20/20\nMP: 7/7")
check.expect('test for mutation', str(enemy),\
"Irelia\nLevel: 1\nStrength: 10\nHP: 8/10\nMP: 10/10")

A1 = Character("Irelia", 1000, 20, 70000)
A2 = Character("Sion", 1000, 20, 100000)
A3 = Character("Lee", 1000, 20, 30000)
enemy = Character('Garon', 1, 1000000, 1)
L = [A1,A2,A3]
check.expect('Example', all_punch(L, enemy), None)
check.expect('test for mutation', str(A1),\
"Irelia\nLevel: 1\nStrength: 1000\nHP: 20/20\nMP: 70000/70000")
check.expect('test for mutation', str(A2),\
"Sion\nLevel: 1\nStrength: 1000\nHP: 20/20\nMP: 100000/100000")
check.expect('test for mutation', str(A3),\
"Lee\nLevel: 1\nStrength: 1000\nHP: 20/20\nMP: 30000/30000")
check.expect('test for mutation', str(enemy),\
"Garon\nLevel: 1\nStrength: 1\nHP: 994000/1000000\nMP: 1/1")

d1 = Character("Top", 5, 10, 7)
d2 = Character("Jung", 7, 8, 8)
d3 = Character("Mid", 9, 7, 6)
e2 = Character("Adc", 9, 7, 6)
e3 = Character("Support", 3, 10, 8)
enemy = Character('Irelia', 10, 10, 10)
L = [d1, d2, d3, e2, e3]
check.expect('Example', all_punch(L, enemy), None)
check.expect('test for mutation', str(d1),\
"Top\nLevel: 2\nStrength: 6\nHP: 12/12\nMP: 8/8")
check.expect('test for mutation', str(d2),\
"Jung\nLevel: 2\nStrength: 8\nHP: 9/9\nMP: 9/9")
check.expect('test for mutation', str(d3),\
"Mid\nLevel: 2\nStrength: 10\nHP: 8/8\nMP: 7/7")
check.expect('test for mutation', str(e2),\
"Adc\nLevel: 2\nStrength: 10\nHP: 8/8\nMP: 7/7")
check.expect('test for mutation', str(e3),\
"Support\nLevel: 2\nStrength: 4\nHP: 12/12\nMP: 9/9")
check.expect('test for mutation', str(enemy),\
"Irelia\nLevel: 1\nStrength: 10\nHP: 0/10\nMP: 10/10")

##Testing __init__
Andy = Character("Irelia", 10, 100, 100)

check.expect("Testing Andy field name", Andy.name, "Irelia")
check.expect("Testing Andy field hp", Andy.hp, 100)
check.expect("Testing Andy field st", Andy.st, 10)

##Testing __repr__
andy = Character('andy', 100, 200, 200)
check.set_print_exact('andy', "Level: 1", "Strength: 100", \
"HP: 200/200", "MP: 200/200")
check.expect("Testing Canada print", print(andy), None)

##Testing __eq__
Bob = Character('Bob', 10, 100, 100)
Bob_copy = Character(Bob.name, Bob.st, Bob.max_hp, Bob.max_mp)
check.expect("Testing == True", Bob == Bob_copy, True)
check.expect("Testing == False", Bob == andy, False)
check.expect("Testing is False", Bob is Bob_copy, False)

##Testing cast_spell
c = Character("Test", 1, 4, 5)
e = Character("Test", 1, 4, 5)
check.set_print_exact("Enemy defeated")
check.expect('test_cast_spell', c.cast_spell(3, 10, e), None)
check.expect("Testing e field hp", e.hp, 0)
check.expect("Testing c field mp", c.mp, 2)

c = Character("Test", 1, 4, 5)
e = Character("Test", 1, 4, 5)
check.set_print_exact("Not enough MP")
check.expect('test_cast_spell', c.cast_spell(13, 10, e), None)

c = Character("Test", 1, 4, 5)
e = Character("Test", 1, 4, 5)
check.expect('test_cast_spell', c.cast_spell(3, 2, e), None)
check.expect("Testing e field hp", e.hp, 2)
check.expect("Testing c field mp", c.mp, 2)

##Testing level_up
c = Character("Test", 1, 4, 5)
check.expect('test_cast_spell', c.level_up(), None)
check.expect("Testing c field level", c.level, 2)
check.expect("Testing c field st", c.st, 2)
check.expect("Testing c field hp", c.hp, 5)
check.expect("Testing c field max_hp", c.max_hp, 5)
check.expect("Testing c field mp", c.mp, 6)
check.expect("Testing c field max_mp", c.max_mp, 6)
