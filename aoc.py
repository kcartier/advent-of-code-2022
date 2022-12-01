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
