# As a team, we have gone through all required sections of the
# tutorial, and each team member understands the material
# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Names:        Het Koradia
#               Landry Lopez
#               Robbie Hahn
import random
import time
from datetime import date
import turtle as tg
#from playsound import playsound
# MacOS may be required to use PLAYSOUND import
# If code doesn't run delete line 364 which has the playsound call

# Sets the initial speed and conditions of the turtle
tg.speed(0)
tg.up()
tg.backward(400)
tg.down()




def moveto(x,y):
   '''Moves the turtle to a certain position without drawing a line to that point'''
   tg.pu()
   tg.goto(x,y)
   tg.pd()
   tg.setheading(0)




#x and y let the user place their numbers down, d is length of sides.
def nine(d):
   '''Draws a nine'''
   point = tg.pos()
   tg.fd(d)
   tg.rt(90)
   tg.fd(d*2)
   tg.bk(d)
   tg.rt(90)
   tg.fd(d)
   tg.rt(90)
   tg.fd(d)
   tg.pu()
   tg.goto(point)
   tg.pd()
   tg.setheading(0)




def eight(d):
   '''Draws an eight'''
   point = tg.pos()
   tg.fd(d)
   tg.rt(90)
   tg.fd(d*2)
   for i in range(3):
      tg.rt(90)
      tg.fd(d)
   tg.bk(d)
   tg.lt(90)
   tg.fd(d)
   tg.pu()
   tg.goto(point)
   tg.pd()
   tg.setheading(0)




def seven(d):
   '''Draws a seven'''
   point = tg.pos()
   tg.fd(d)
   tg.rt(90)
   tg.fd(d*2)
   tg.bk(d*2)
   tg.lt(90)
   tg.bk(d)
   tg.pu()
   tg.goto(point)
   tg.pd()
   tg.setheading(0)




def six(d):
   '''Draws a six'''
   point = tg.pos()
   tg.fd(d)
   tg.bk(d)
   tg.rt(90)
   tg.fd(d*2)
   for i in range(3):
       tg.lt(90)
       tg.fd(d)
   tg.rt(90)
   tg.fd(d)
   tg.pu()
   tg.goto(point)
   tg.pd()
   tg.setheading(0)




def five(d):
   '''Draws a five'''
   point = tg.pos()
   tg.fd(d)
   tg.bk(d)
   tg.rt(90)
   tg.fd(d)
   tg.lt(90)
   tg.fd(d)
   for i in range(2):
       tg.rt(90)
       tg.fd(d)
   tg.pu()
   tg.goto(point)
   tg.pd()
   tg.setheading(0)




def four(d):
   '''Draws a four'''
   point = tg.pos()
   tg.rt(90)
   tg.fd(d)
   for i in range(2):
       tg.lt(90)
       tg.fd(d)
   tg.bk(d * 2)
   tg.pu()
   tg.goto(point)
   tg.pd()
   tg.setheading(0)




def three(d):
   '''Draws a three'''
   point = tg.pos()
   for i in range(2):
       tg.fd(d)
       tg.rt(90)
   tg.fd(d)
   for i in range(2):
       tg.bk(d)
       tg.rt(90)
   tg.bk(d)
   tg.pu()
   tg.goto(point)
   tg.pd()
   tg.setheading(0)




def two(d):
   '''Draws a two'''
   point = tg.pos()
   tg.fd(d)
   tg.rt(90)
   tg.fd(d)
   tg.lt(90)
   for i in range(2):
       tg.bk(d)
       tg.lt(90)
   tg.bk(d)
   tg.pu()
   tg.goto(point)
   tg.pd()
   tg.setheading(0)




def one(d):
   '''Draws a one'''
   point = tg.pos()
   tg.pu()
   tg.fd(d)
   tg.pd()
   tg.rt(90)
   tg.fd(d*2)
   tg.pu()
   tg.goto(point)
   tg.pd()
   tg.setheading(0)




def zero(d):
   '''Draws a zero'''
   point = tg.pos()
   tg.fd(d)
   tg.rt(90)
   tg.fd(d*2)
   tg.rt(90)
   tg.fd(d)
   tg.rt(90)
   tg.fd(d*2)
   tg.pu()
   tg.goto(point)
   tg.pd()
   tg.setheading(0)




def drawnum(n):
   '''Determines what number is going to be drawn'''
   d=100
   if (n == 1):
       one(d)
   if (n ==2):
       two(d)
   if (n==3):
       three(d)
   if (n==4):
       four(d)
   if (n==5):
       five(d)
   if (n==6):
       six(d)
   if (n==7):
       seven(d)
   if (n==8):
       eight(d)
   if (n==9):
       nine(d)
   if (n==0):
       zero(d)
   tg.pu()
   tg.fd(1.5*d)
   tg.pd()




def drawScore(scores):
  moveto(0,400)
  # Iterates over the digits and then draws that digit
  for digit in scores:
      drawnum(int(digit))
  tg.pu()
  tg.goto(0,0)




def unique(list1):
  '''Returns a list of all of the unique values in a list'''
  unique_list = []
  for x in list1:
      # Iterateis over a list and adds only the values that aren't already in the list
      if x not in unique_list:
          unique_list.append(x)
  return unique_list




def dice(face,side=100,color='black',width=2):
   '''Draws the dice face based on the number that is passed'''
   tg.color(color if face else 'white')
   tg.width(width)
   for _ in range(4):
       tg.forward(side)
       tg.left(90)
   # Instantiates all of the dice faces
   faces = { 0: [(1,1),(1,3),(1,5),(3,3),(5,1),(5,3),(5,5)],
               1: [(3,3)],
               2: [(1,1),(5,5)],
               3: [(1,1),(3,3),(5,5)],
               4: [(1,1),(1,5),(5,1),(5,5)],
               5: [(1,1),(1,5),(3,3),(5,1),(5,5)],
               6: [(1,1),(1,3),(1,5),(5,1),(5,3),(5,5)] }
   x,y     = tg.pos()
   offset  = side/15
   dotSize = (side-2*offset)/7
   tg.penup()
   px,py   = 0,0
   # Iterates over the dot locations to draw the dots
   for dx,dy in faces[face]:
       rx,ry = dx*dotSize+dotSize/2+offset,dy*dotSize+dotSize/2+offset
       tg.forward(rx-px)
       tg.left(90)
       tg.forward(ry-py)
       tg.right(90)
       px,py = rx,ry
       tg.dot(dotSize*1.5,color if face else 'white')
   tg.goto(x,y)
   tg.up()
   tg.forward(150)
   tg.down()


def drawDice(dices):
   '''Draws the dice faces for all of the numbers'''
   tg.clear()
   tg.up()
   tg.setx(-400)
   tg.down()
   for i in dices:
       dice(i)




def setKeepers(rolls, keeps):
   '''Saves all of the dices values you want to keep and re-rolls the remaining dice for a new set of 5 dice'''
   # Asks which index of dice the user wants
   keepers = input('Indexes of dice to keep (separated by commas): ')
   keepers = keepers.split(',')
   # Saves the values at the given index to this list
   keeps = [rolls[int(x)] for x in keepers]
   print('Current Keepers:',keeps)
   rolls, keeps = rollDice(rolls, keeps)
   print('Current Dice:', rolls)
   return rolls, keeps,




def rollDice(rolls, keeps):
   '''Gives random numbers besides the dice that want to be kept'''
   rolls = []
   for i in range(5-len(keeps)):
       rolls.append(random.randint(1, 6))
   rolls = rolls + keeps
   return rolls, keeps




def displayCategories(listCat, listRules):
   '''Displays the possible categories that are still available '''
   for i in range(len(listCat)):
       print(f'{i+1}) {listCat[i]} -- {listRules[i]}')




def pickCategory(listCat, listRules, score, nums):
   '''Asks user for which category they want than then scores the dice based on that category'''
   choiceIndex = int(input('Pick a Category NUMBER to Score: ')) - 1
   score += scoreTheDice(listCat, choiceIndex, nums)
   # Plays the chime sound whenever a choice is picked
   #playsound('chime.mp3')
   # Deletes the choice they made from the original list so they can't score based on that option again
   listCat.pop(choiceIndex)
   listRules.pop(choiceIndex)
   return listCat, listRules, score




def scoreTheDice(listCat, choiceIndex, nums):
   '''Determines how much points a list of dice is worth'''
   choice = listCat[choiceIndex]
   if(choice == 'Ones'):
       return 1 * nums.count(1)
   elif(choice == 'Twos'): 
       return 2 * nums.count(2)
   elif(choice == 'Threes'):
       return 3 * nums.count(3)
   elif(choice == 'Fours'):
       return 4 * nums.count(4)
   elif(choice == 'Fives'):
       return 5 * nums.count(5)
   elif(choice == 'Sixes'):
       return 6 * nums.count(6)
   elif(choice == '3 of a Kind'):
       # Sees if ones of the numbers in the list shows up at least three times
       for i in nums:
           if(nums.count(i) >= 3):
               return sum(nums)
       return 0
   elif(choice == '4 of a Kind'):
       # Sees if one of the numbers in the list shows up at least four times
       for i in nums:
           if(nums.count(i) >= 4):
               return sum(nums)
       return 0
   elif(choice == 'Full House'):
       nums.sort()
       # Sees if the first number appears 2 times while the last appears 3 times
       if(nums.count(nums[0]) == 2 and nums.count(nums[4]) == 3):
           return 25
       # Sees if the first number appears 3 times while the last appears 2 times
       elif(nums.count(nums[0]) == 3 and nums.count(nums[4]) == 2):
           return 25
       else:
           return 0
   elif(choice == 'Small Straight'):
       unique_list = unique(nums)
       unique_list.sort()
       # Four numbers are in increasing order
       if(len(unique_list) >= 4 and all(unique_list[i] == unique_list[i-1] + 1 for i in range(1, len(unique_list)))):
           return 30
       else:
           return 0
   elif(choice == 'Large Straight'):
       unique_list = unique(nums)
       unique_list.sort()
       # Five numbers are in increasing order
       if(len(unique_list) == 5 and all(unique_list[i] == unique_list[i-1] + 1 for i in range(1, len(unique_list)))):
           return 40
       else:
           return 0
   elif(choice == 'Yahtzee'):
       # There is only one unique number in the list meaning all five numbers are the same
       if(len(unique(nums)) == 1):
           return 50
       else:
           return 0
   elif(choice == 'Chance'):
       return sum(nums)
   else:
       # Error handling here if here
       return 0






if __name__ == '__main__':
   '''Main function were all of the code gets put together'''
   # Saves the list of different categories
   List_of_Cat = ['Ones', 'Twos', 'Threes', 'Fours', 'Fives', 'Sixes', '3 of a Kind', '4 of a Kind', 'Full House', 'Small Straight', 'Large Straight', 'Yahtzee', 'Chance']
   List_of_Rules = ['Total value of Ones Only (Points equal amount of Ones present)', 'Total of Twos Only (Points equal amount of Twos present)', 'Total of Threes Only (Points equal amount of Threes present)', 'Total of Fours Only (Points equal amount of Fours present)', 'Total of Fives Only (Points equal amount of Fives present)', 'Total of Sixes Only (Points equal amount of Sixes present)', 'Three of the same Kind (Points are total of the five dice)', 'Four of the same Kind (Points are total of the five dice)', 'Three of One number and Two of Another (25 points)', 'Four dice that start at either numbers 1,2, or 3 and increase by increments of 1 (30 Points)', 'Five dice that start at either 1 or 2 and increase by increments of 1 (40 points)', 'Five of a Kind (50 points)', 'Random for the five dice (Points equal the total of the dice)']


   print('Welcome to Aggie Yahtzee!!!')
   print("The rules are as follows: \nThis is a single player game in which your goal is to accumulate as many points as possible. \nThere are a total of Thirteen rounds, in which a random draw of five dice are presented. \nEach round grants a total of two rerolls, in which the player is allowed to keep any dice of their choosing in order to fulfill as many categories as possible. \nThe categories and the points the player could accumulate will appear alongside a list of numbers, when the player wants to assign their dice to a category they will be prompted to pick one of the thirteen numbers.\nHowever, after they assign their dice to a category, they will not be allowed to change or reassign their dice to it. \nIf the dice the player assigns to a category does not follow the boundaries for that specific category, the player will receive no points for the assignment. \nThe name of the game is chance, try your luck and have fun! Thanks and Gig 'em.")


   score = 0
   try:
       # Checks if this file exists if not it makes it
       file = open('oldScores.txt', 'x')
   except:
       pass
   # Opens the file in append mode so we can add the new replay to it once the game is over
   file = open('oldScores.txt', 'a')


   # Iterates 13 times as there are 13 categories
   for i in range(13):
       # Instanties all of the variables that will control the game
       print()
       keeps = []
       rolls = []
       rolls, keeps = rollDice(rolls, keeps)
       scored = False
       iter = 0  
       print('Current Roll',rolls)
       drawDice(rolls)
       drawScore(str(score))


       # Iterates less than 3 times as there can only be 2 extra re-rolls
       while iter < 3 and scored == False:




           print('RE-ROLLS LEFT =', 2-iter, '\n')
           if(iter != 2):
               # Makes sure that the number is either 1, 2 or 3
               try:
                   decision = int(input('\nPick plan of action:\n1) Fill a Box\n2) Set Keepers\n3) Roll Again\n\nNumber Here: '))
                   if(decision == 1): # Fill in a box
                       print()
                       # Shows the availble catogories
                       displayCategories(List_of_Cat, List_of_Rules)
                       List_of_Cat, List_of_Rules, score = pickCategory(List_of_Cat, List_of_Rules, score, rolls)
                       # Changes to true as the extra re-rolls are no longer needed
                       scored = True
                       print(score)


                   elif(decision == 2): # Set Keepers
                       print()
                       rolls, keeps = setKeepers(rolls, keeps)
                       drawDice(rolls)
                       drawScore(str(score))
                      
                   elif(decision == 3): # Roll Again
                       if(keeps != []):
                           print('Current Keepers', keeps)
                           # Asks them if they want to remove any of their keeps
                           yes_no = input('Clear your keeps? (Y/N): ')
                           while yes_no != "Y" and yes_no != "N":
                               print("Please use an uppercase Y or N for your choice")
                               yes_no = input("Clear your keeps? (Y/N) ")
                           if(yes_no == 'Y'):
                               keeps = []
                           elif(yes_no == 'N'):
                               pass
                       rolls, keeps = rollDice(rolls, keeps)
                       print('\nCurrent Roll',rolls)
                       drawDice(rolls)
                       drawScore(str(score))
                   else:
                       raise Exception("Not a choice")
                   iter+=1
               except:
                   print('\nINVALID OPTION!!!!!!')
                   time.sleep(2)
           else:
               print('You have to pick a catagory now!!!')
               displayCategories(List_of_Cat, List_of_Rules)
               List_of_Cat, List_of_Rules, score = pickCategory(List_of_Cat, List_of_Rules, score, rolls)
               scored = True
               print(score)
               # pickCatagory(score, rolls)
               iter += 1


   name = input('Enter your name here: ')
   # writes the new score onto the doc
   file.write(f'{score}, {date.today()}, {name}\n')
   file.close()


   tg.done