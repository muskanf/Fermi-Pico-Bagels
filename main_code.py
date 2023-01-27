import random as random
count=0
#generating a random number
random_number=(random.randint(000, 999))
#re-generating a random number if duplicates or if digits less than 3
#converting number into set because they dont allow duplicates
while len(set(str(random_number))) != 3:
    random_number = random.randint(000,999)
#checking for duplicate numbers
# for i in range(20):
#     random_number=(random.randint(000, 999))
#     while len(set(str(random_number))) != 3:
#         random_number = random.randint(000,999)
#     print(random_number)
    #Docstring required within each function:
    """
        Description of function: This function will repeat the input by user until they input properly. 
        return: none.
    """
def user_input():
    user_guess=input('Please enter a 3-digit number. No duplicates:')
    guess_bad=True # Repeating below until the user gives a good input
    while guess_bad:
      if len(user_guess) != 3: #this should make sure that all digits can be converted to integers!
          print('Must contain three digits.')
          user_guess = input('Please enter a 3-digit number. No duplicates:')
      elif len(set(str(user_guess))) != 3:
              print('No duplicates.')
              user_guess = input('Please enter a 3-digit number. No duplicates:')
      else:
        guess_bad=False
    return user_guess
#Docstring required within each function:
    """
        Description of function: This function will convert the digits into lists to compare and output the answer to user. It also takes in the number of tries and outputs the count.
        return: The number of tries.
    """
def add_user_lists(num_tries)->int: 
  user_guess=user_input()
  result=[]
  random_number_list=[]
  user_input_list=[]
  for digit in str(random_number):
    random_number_list.append(digit)
  for digit in str(user_guess):
    user_input_list.append(digit)
#   Just to check the answers:  
#   print(random_number_list)
#   print(user_input_list)
  count=0
  for i in range (0, len(random_number_list)):
    if random_number_list[i]==user_input_list[i]:
      print("Fermi!",end='')
      count +=1
    elif random_number_list[i] in user_input_list:
      print("Pico! ",end='')
      count+=.1
  if count==0:
      print('Bagles!',end='') 
  elif count==3:
      print(f'You win and it took you {num_tries} tries!')
      exit()
  print()
  return count


num_tries=1
while add_user_lists(num_tries) <3: #This checks if the count is less than three
  num_tries+=1
