from enum import Enum

class Choices(Enum):
  SAVE_A_NEW_ENTRY = 1
  SEARCH_BY_ID = 2
  PRINT_AGES_AVERAGE = 3
  PRINT_ALL_NAMES = 4
  PRINT_ALL_IDS = 5
  PRINT_ALL_ENTRIES = 6
  PRINT_ENTRY_BY_INDEX = 7
  SAVE_ALL_ENTRY = 8
  EXIT = 9


  def printAllOption():
    for choice in Choices:
      print(choice.value , "-" , choice.name)
  