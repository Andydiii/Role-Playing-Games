# Role-Playing-Games
This role playing game is a kind of board/video game where a player takes on the entity of another character. Characters have levels, classes and attributes which we'll define below that are used to determine how outcomes will fare for the player. 

************************************
class Character:
Fields:
- name(Str)
- st(Nat)
- hp(Nat)
- max_hp(Nat)
- mp(Nat)
- max_mp(Nat)
- level(Nat)
     
Requires:  
   st, max_hp are both strictly greater than 0.
Note above the field 
- name is the id of the player
- st corresponds to strength. 
- HP and MP stand for Hit Points, how much health a Character has, and Magic Points, how much magical ability a character has to cast spells.  
************************************
the __init__ method:
- initializes the fields of the class object.
The level should begin at 1 and hp and max_hp should both equal
the parameter maximumHP and similarly for mp and max_mp with parameter maximumMP.
***********************************
the __eq__ method:
- returns True if and only if the other object is a Character class object with all fields equal to the corresponding fields in self.
***********************************
the __repr__ method:
- returns a string in the following format
- Name
- Level: #
- Strength: #
- HP: #/#
- MP: #/#
where each # above is replaced by the appropriate number (see below for an example) and the Name in the first line is replaced by the Character's name. Each line excluding the last should end with a newline character.
***********************************
the class method cast_spell(self, cost, damage, enemy) 
- consumes a Character, two natural numbers cost and damage corresponding to how much MP the spell costs and how much damage the spell deals and an enemy Character. If self has enough current MP to cast the spell, the MP is deducted and the damage is dealt to the enemy's HP. If the enemy's HP becomes less than or equal to 0, move it back to 0, print the message:
    Enemy defeated
and return. 
If self does not have enough current MP to cast the spell, then print the message
     Not enough MP
and return.
***********************************
the class method level_up(self) 
consumes a Character and performs a level up of the Character. The level should increase by 1 and every stat (excluding hp and mp) should be increased by 1 plus 10% of the current statistic rounded down. The values for hp and mp should increase by the same amount that max_hp and max_mp increased by.
***********************************
 all_punch(players, enemy):
- consumes a (listof Character) in players and a single Character in enemy, returns None but simulates all the players punching an enemy. Each Character in players will hit the enemy and deal damage to them by decreasing their hp by twice the st strength statistic of each individual Character in players. If the enemy runs out of hp, their hp is set to 0 and everyone in players levels up (see previous bullet). You may assume enemy is not in players.
***********************************

Samples:

c1 = Character("Sloan", 12, 10, 11)  
e1 = Character("E1", 2, 5, 10)  
print(c1)  
print(e1)  
c1.cast_spell(20, 10, e1) => None  
c1.level_up()  
print(c1)  
d1 = Character("C1", 10, 10, 10)  
d2 = Character("C2", 1, 10, 10)  
d3 = Character("C3", 20, 20, 10)  
e2 = Character("E2", 20, 20, 10)  
L = [d1, d2, d3]  
all_punch(L, e2) => None  

and the following is printed:  
Sloan  
Level: 1  
Strength: 12  
HP: 10/10  
MP: 11/11  
E1  
Level: 1  
Strength: 2  
HP: 5/5  
MP: 10/10  
Not enough MP  
Sloan  
Level: 2  
Strength: 14  
HP: 12/12  
MP: 13/13  
and all of d1, d2, d3 have levelled up and e2's hp is now 0.  
