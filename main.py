print('''
888                                                          
888                                                          
888                                                          
888888888d888 .d88b.  8888b. .d8888b 888  888888d888 .d88b.  
888   888P"  d8P  Y8b    "88b88K     888  888888P"  d8P  Y8b 
888   888    88888888.d888888"Y8888b.888  888888    88888888 
Y88b. 888    Y8b.    888  888     X88Y88b 888888    Y8b.     
 "Y888888     "Y8888 "Y888888 88888P' "Y88888888     "Y8888 
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.") 

#https://www.draw.io/?lightbox=1&highlight=0000ff&edit=_blank&layers=1&nav=1&title=Treasure%20Island%20Conditional.drawio#Uhttps%3A%2F%2Fdrive.google.com%2Fuc%3Fid%3D1oDe4ehjWZipYRsVfeAx2HyB7LCQ8_Fvi%26export%3Ddownload

#Write your code below this line 👇
choice1 = input('You\'re at a cross road. Where do you want to go? Type "left" or "right" \n').lower()
if choice1 == "right":
  print("You fell into a hole. Game Over.")
else:
  choice2 = input('You have come to a sea. There is an island in the middle of the lake.Type "wait" to wait for a boat. Type "swim" to swim across \n').lower()
  if choice2 == "swim":
    print("There are some sharks in the sea. You can not pass. Game Over.")
  else:
    choice3 = input('You have arrived at the island safely. There is a house of three doors. Red, yellow and blue. Which colour do you chooose? \n').lower()
    if choice3 == "yellow":
      print("CONGRATULTIONS!!! You find a treasure.")
      print(r"""
            

                    ____...------------...____
               _.-"` /o/__ ____ __ __  __ \o\_`"-._
             .'     / /                    \ \     '.
             |=====/o/======================\o\=====|
             |____/_/________..____..________\_\____|
             /   _/ \_     <_o#\__/#o_>     _/ \_   \
             \_________\####/_________/
              |===\!/========================\!/===|
              |   |=|          .---.         |=|   |
              |===|o|=========/     \========|o|===|
              |   | |         \() ()/        | |   |
              |===|o|======{'-.) A (.-'}=====|o|===|
              | __/ \__     '-.\uuu/.-'    __/ \__ |
              |==== .'.'^'.'.====|
              |  _\o/   __  {.' __  '.} _   _\o/  _|
              `""""-""""""""""""""""""""""""""-""""`
            """)    
    elif choice3 == "red":  
      print("Burned by fire. Game Over.")
    elif choice3 == "blue":
      print("Eaten by beasts. Game Over.")
    else:
      print("Game Over")
  
  

