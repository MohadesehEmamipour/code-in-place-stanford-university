"""
There are many solutions to this problem. Here are a few
"""

# Example Solution 1
def main():
   # make the first three waves
   for i in range(3):
      build_wave()
      # you need to move twice to go between waves
      move()
      move()
   # because of the fencepost bug, we need a fourth wave
   build_wave()

def build_wave():
   put_beeper()
   move()
   put_beeper()
   turn_left()
   move()
   put_beeper()
   turn_around()
   move()
   turn_left()
   
   
# Example Solution 2
def main():
   # you can also solve this problem with a while loop
   while front_is_clear():
      build_wave()
      # you might be facing a wall at this point!
      if front_is_clear():
         move()
         move()
         
def build_wave():
   # same as in solution 1
