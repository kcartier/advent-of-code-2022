## ************************************************************************** ##
## **************                   FUNCTION                   ************** ##
## ************************************.************************************* ##
def aoc_day_02():
   """
   Geez, this is really hacky.  But it works.
   """
   # ---------------------------------------------------------------------------
   log.info(">>> aoc_day_02()")
   localpath = YAML_DOC['local_path']
   filename = "aoc_input_day_02.txt"
   aoc_file = open(f"{localpath}/{filename}", 'r')
   lines = aoc_file.readlines()
   aoc_file.close()

   # lines = [
   #    "A Y",
   #    "B X",
   #    "C Z"
   # ]

   # Read the data into a list and transform the play encodings
   rochambeau_rounds = []
   round_number = 0
   for line in lines:
      round_number += 1
      item = line.split()
      round_score = 0
      my_play_score = 0

      # Transform the play encodings
      if item[0] == 'A':
         op_play = 'R'
      elif item[0] == 'B':
         op_play = 'P'
      elif item[0] == 'C':
         op_play = 'S'

      if item[1] == 'X':
         my_play = 'R'
      elif item[1] == 'Y':
         my_play = 'P'
      elif item[1] == 'Z':
         my_play = 'S'

   # Calculate the scores
      if my_play == 'R':
         my_play_score = 1
         if op_play == 'R':
            round_score = 3 # We tie
         elif op_play == 'P':
            round_score = 0 # I lose
         if op_play == 'S':
            round_score = 6 # I win

      elif my_play == 'P':
         my_play_score = 2
         if op_play == 'R':
            round_score = 6 # I win
         elif op_play == 'P':
            round_score = 3 # We tie
         if op_play == 'S':
            round_score = 0 # I lose

      elif my_play == 'S':
         my_play_score = 3
         if op_play == 'R':
            round_score = 0 # I lose
         elif op_play == 'P':
            round_score = 6 # I win
         if op_play == 'S':
            round_score = 3 # We tie

      round_total_score = my_play_score + round_score
      rochambeau_rounds.append((round_number, op_play, my_play, my_play_score, round_score, round_total_score))
   final_score = 0
   for i in range(len(rochambeau_rounds)):
      final_score += rochambeau_rounds[i][5]
   print(f"Final score Part 1: {final_score}")

   # -----------------------------------------------------------------------------
   # Part 2:  Re-Interpretation of the encodings
   # -----------------------------------------------------------------------------
   rochambeau_rounds = []
   round_number = 0
   for line in lines:
      round_number += 1
      item = line.split()
      round_score = 0
      my_play_score = 0

      # Transform the play encodings
      if item[0] == 'A':
         op_play = 'R'
      elif item[0] == 'B':
         op_play = 'P'
      elif item[0] == 'C':
         op_play = 'S'

      if item[1] == 'X':
         my_play = 'R'
      elif item[1] == 'Y':
         my_play = 'P'
      elif item[1] == 'Z':
         my_play = 'S'

   # Calculate the scores
      if my_play == 'R': # Need to Lose
         round_score = 0 
         if op_play == 'R':    # Need to lose to R --> switch my_play to S
            my_play_score = 3
         elif op_play == 'P':  # Need to lose to P --> switch my_play R
            my_play_score = 1
         if op_play == 'S':    # Need to lose to S --> switch my_play P
            my_play_score = 2

      elif my_play == 'P': # Need to Tie
         round_score = 3
         if op_play == 'R':    # Need to tie with R --> switch my_play to R
            my_play_score = 1
         elif op_play == 'P':  # Need to tie with P --> switch my_play P
            my_play_score = 2
         if op_play == 'S':    # Need to tie with S --> switch my_play S
            my_play_score = 3

      elif my_play == 'S': # Need to Win
         round_score = 6
         if op_play == 'R':    # Need to win over R --> switch my_play to P
            my_play_score = 2
         elif op_play == 'P':  # Need to win over P --> switch my_play S
            my_play_score = 3
         if op_play == 'S':    # Need to win over S --> switch my_play R
            my_play_score = 1

      round_total_score = my_play_score + round_score
      rochambeau_rounds.append((round_number, op_play, my_play, my_play_score, round_score, round_total_score))
      # print(f"{round_number}, {op_play}, {my_play}, {my_play_score}, {round_score}, {round_total_score}")
   final_score = 0
   for i in range(len(rochambeau_rounds)):
      final_score += rochambeau_rounds[i][5]
   print(f"Final score Part 2: {final_score}")
   return


## ************************************************************************** ##
## **************                   FUNCTION                   ************** ##
## ************************************.************************************* ##
def aoc_day_01():
   """
   Advent of Code:  Day 1
   Which elf is packing the most calories?
   """
   # ---------------------------------------------------------------------------
   log.info(">>> aoc_day_01()")
   localpath = YAML_DOC['local_path']
   filename = "aoc_input_day_01.txt"
   aoc_file = open(f"{localpath}/{filename}", 'r')
   lines = aoc_file.readlines()
   aoc_file.close()

   # Read the data into a list
   elvish_food_packs = []
   elf_pack = []
   for line in lines:
      item = line.strip()
      if item:
         elf_pack.append(int(item))
      else:
         elvish_food_packs.append(elf_pack)
         elf_pack = []
 
   # Summarize and sort
   elvish_pack_summaries = []
   for food_pack in elvish_food_packs:
      elvish_pack_summaries.append(sum(food_pack))
   elvish_pack_summaries.sort(reverse=True)

   # Get the top values
   print(elvish_pack_summaries)

   top_3_calorie_sum = \
      elvish_pack_summaries[0] + \
      elvish_pack_summaries[1] + \
      elvish_pack_summaries[2]  
   log.info(f"~~~ top_3_calorie_sum: {top_3_calorie_sum}")
   return
