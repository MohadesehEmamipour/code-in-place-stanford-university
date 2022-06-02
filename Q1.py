"""
There are many solutions to this problem. Here are a few
"""

# Example Solution 1
def main():
   # get the user height, cast it to a float, save as a variable
   user_height = float(input('Enter your height in meters: '))
   # first rule out that they are too short
   if user_height < 1.6:
      print('Below minimum astronaut height')
   # then rule out that they are too tall
   elif user_height > 1.9:
      print('Above maximum astronaut height')
   # at this point you know they are the correct height
   else:
      print('Correct height to be an astronaut')


# Example Solution 2
def main():
   user_height = float(input('Enter you height in meters: '))
   if user_height >= 1.6 and user_height <= 1.9:
      print('Correct height to be an astronaut')
   elif user_height < 1.6:
      print('Below minimum astronaut height')
   else:
      print('Above maximum astronaut height')
