"""
This problem is complex because you need to keep track of several variables. 
There are so many ways to solve this problem! They generally fall into two main categories.
"""

# Those who used a while loop which goes while curr >= last
def main():
   print("Enter a sequence of non-decreasing numbers. ")
   count = 0                      # essential to keep track of length
   last_num = float(input('Enter num: '))
   curr_num = last_num            # can have another enter num here
   while curr_num >= last_num:    # there are many ways to write this!
      count += 1                  # this line can go anywhere in body
      last_num = curr_num         # update the last num first!
      curr_num = float(input('Enter num: '))
   print("Thanks for playing!")   # watch for string
   print("Sequence length: " + str(count))
   
   
# Those who used a while True loop where they only needed to have a single last_value
# declared before the loop. This required use of the break keyword.
def main():
   print("Enter a sequence of non-decreasing numbers. ")
   count = 1                      # length is at least 1
   last_num = float(input('Enter num: '))
   while True:
      curr_num = float(input('Enter num: '))
      if curr_num < last_num:
         # some people optionally put the thanks for playing here
         break   # this makes python exit the loop immediately
      count += 1
      last_num = curr_num
   print("Thanks for playing!")
   print("Sequence length: ", count)
if __name__ == "__main__":
    main()
