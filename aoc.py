## ************************************************************************** ##
## **************                   FUNCTION                   ************** ##
## ************************************.************************************* ##
def aoc_day_05():
   """
   There are about 7,000 different ways to get an "off-by-one" error in this code ...
   ... and I think I hit them all before arriving at a working solution
   """
   # ---------------------------------------------------------------------------
   log.info(">>> aoc_day_05()")
   localpath = YAML_DOC['local_path']
   filename = "aoc_input_day_05.txt"
   aoc_file = open(f"{localpath}/{filename}", 'r')
   lines = aoc_file.readlines()
   aoc_file.close()

   stacks = []
   procedures = []
   for line in lines:
      if 0 <= line.find('['):
         stacks.append(line)
      if 0 <= line.find('move'):
         procedures.append(line)

   # stacks = [ # For testing
   #    "    [D]    ",    # 2
   #    "[N] [C]    ",    # 1
   #    "[Z] [M] [P]"     # 0
   # ]

   # procedures = [ # For testing
   #    "move 1 from 2 to 1",
   #    "move 3 from 1 to 3",
   #    "move 2 from 2 to 1",
   #    "move 1 from 1 to 2"  
   # ]

   new_procs = [] # count, src, tgt
   for proc in procedures:
      proc = proc.strip()
      proc = proc.split()
      new_procs.append((proc[1], proc[3], proc[5]))
   procedures = new_procs

   MAX_ROWS = 5
   def top_crate(col): 
      # Find the top crate in a given stack
      for row in range(MAX_ROWS, -1, -1):
         if crates_arr[row-1][col] != '_':
            break
      return max(0, row-1)

   # ----------------------------------------------------------------------
   # Part 1 
   # ----------------------------------------------------------------------
   max_stacks = 0
   for stack in stacks:
      crate_level = stack.strip()
      stack_count = len(crate_level.split())
      if max_stacks < stack_count:
         max_stacks = stack_count
   cols = max_stacks
   crates_arr = [['_' for i in range(cols)] for j in range(MAX_ROWS)]

   # Fill the array from the bottom to the top
   stacks.reverse() 
   row = -1
   for crate_level in stacks:
      row += 1
      for col in range(0, (cols*4)-1):
         if crate_level[col].isalpha():
            crates_arr[row][int((col-1)/4)] = crate_level[col]

   for proc in procedures:
      count = int(proc[0])
      src = int(proc[1])-1
      tgt = int(proc[2])-1
      for i in range(count):
         src_top = top_crate(src)
         tgt_top = top_crate(tgt)
         crates_arr[tgt_top+1][tgt] = crates_arr[src_top][src]
         crates_arr[src_top][src] = '_'
      # print("\n")
      # for row in range(MAX_ROWS):
      #    print(f"{crates_arr[row]}")

   top_crates = ""
   for j in range(cols):
      top_crates += crates_arr[top_crate(j)][j]
   print(f"Top Crates: {top_crates}")

   return


## ************************************************************************** ##
## **************                   FUNCTION                   ************** ##
## ************************************.************************************* ##
def aoc_day_04():
   """
   Cleanup Assignments
   """
   # ---------------------------------------------------------------------------
   log.info(">>> aoc_day_04()")
   localpath = YAML_DOC['local_path']
   filename = "aoc_input_day_04.txt"
   aoc_file = open(f"{localpath}/{filename}", 'r')
   lines = aoc_file.readlines()
   aoc_file.close()

   # lines = [ # For testing
   #    "2-4,6-8",
   #    "2-3,4-5",
   #    "5-7,7-9",
   #    "2-8,3-7",
   #    "6-6,4-6",
   #    "2-6,4-8"
   # ]

   # ----------------------------------------------------------------------
   # Part 1 & Part 2
   # ----------------------------------------------------------------------
   fullycontained_count = 0
   overlap_count = 0
   for line in lines:
      assignments = line.strip().split(sep=",")
      elf_1_assgn = assignments[0].split(sep="-")
      elf_2_assgn = assignments[1].split(sep="-")
      if int(elf_1_assgn[1]) < int(elf_2_assgn[0]):
         pass # Disjoint assignments
      elif int(elf_2_assgn[1]) < int(elf_1_assgn[0]):
         pass # Disjoint assignments
      elif int(elf_1_assgn[0]) >= int(elf_2_assgn[0]) and int(elf_1_assgn[1]) <= int(elf_2_assgn[1]):
         fullycontained_count += 1
      elif int(elf_2_assgn[0]) >= int(elf_1_assgn[0]) and int(elf_2_assgn[1]) <= int(elf_1_assgn[1]):
         fullycontained_count += 1
      else:
         overlap_count += 1 
   print(f"overlap_count:        {overlap_count}")
   print(f"fullycontained_count: {fullycontained_count}")
   print(f"total:                {fullycontained_count+overlap_count}")
   return


## ************************************************************************** ##
## **************                   FUNCTION                   ************** ##
## ************************************.************************************* ##
def aoc_day_03():
   """
   Rucksack Reorg
   """
   # ---------------------------------------------------------------------------
   log.info(">>> aoc_day_03()")
   localpath = YAML_DOC['local_path']
   filename = "aoc_input_day_03.txt"
   aoc_file = open(f"{localpath}/{filename}", 'r')
   lines = aoc_file.readlines()
   aoc_file.close()

   # lines = [ # For testing
   #    "vJrwpWtwJgWrhcsFMMfFFhFp",
   #    "jqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL",
   #    "PmmdzqPrVvPwwTWBwg",
   #    "wMqvLMZHhHMvwLHjbvcjnnSBnvTQFn",
   #    "ttgJtRGJQctTZtZT",
   #    "CrZsJsPPZsGzwwsLwLmpwMDw"
   # ]

   priority_values = {
      "a":1, "b":2,   "c":3,  "d":4,  "e":5, 
      "f":6, "g":7,   "h":8,  "i":9,  "j":10, 
      "k":11, "l":12, "m":13, "n":14, "o":15, 
      "p":16, "q":17, "r":18, "s":19, "t":20, 
      "u":21, "v":22, "w":23, "x":24, "y":25, "z":26, 
      "A":27, "B":28, "C":29, "D":30, "E":31, 
      "F":32, "G":33, "H":34, "I":35, "J":36, 
      "K":37, "L":38, "M":39, "N":40, "O":41, 
      "P":42, "Q":43, "R":44, "S":45, "T":46, 
      "U":47, "V":48, "W":49, "X":50, "Y":51, "Z":52
   }

   # ----------------------------------------------------------------------
   # Part 1
   # ----------------------------------------------------------------------
   total_score = 0
   for rucksack_contents in lines:
      rucksack_contents = rucksack_contents.strip()
      compartment_1 = [0] * 52
      compartment_2 = [0] * 52
      for i in range (0, int(len(rucksack_contents)/2)):
         compartment_1[priority_values[rucksack_contents[i]]-1] += 1
      for i in range (int(len(rucksack_contents)/2), len(rucksack_contents)):
         compartment_2[priority_values[rucksack_contents[i]]-1] += 1
      for i in range (52):
         if compartment_1[i] != 0 and compartment_2[i] != 0:
            total_score += i+1
   print(f"(Part 1) Total Score: {total_score}")

   # ----------------------------------------------------------------------
   # Part 2
   # ----------------------------------------------------------------------
   total_score = 0
   i = 0
   for i in range(0, len(lines), 3):
      rucksack_contents = lines[i+0].strip()
      rucksack_1 = [0] * 52
      for j in range (0, len(rucksack_contents)):
         rucksack_1[priority_values[rucksack_contents[j]]-1] += 1

      rucksack_contents = lines[i+1].strip()
      rucksack_2 = [0] * 52
      for j in range (0, len(rucksack_contents)):
         rucksack_2[priority_values[rucksack_contents[j]]-1] += 1

      rucksack_contents = lines[i+2].strip()
      rucksack_3 = [0] * 52
      for j in range (0, len(rucksack_contents)):
         rucksack_3[priority_values[rucksack_contents[j]]-1] += 1

      for j in range (52):
         if rucksack_1[j] != 0 and rucksack_2[j] != 0 and rucksack_3[j] != 0:
            total_score += j+1
   print(f"(Part 2) Total Score: {total_score}")
   return


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
