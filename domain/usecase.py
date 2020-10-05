from domain.types import Dictionary
import random

GlobalDictionary = Dictionary("./French-Dictionary")
GlobalDictionary.loadFile()

def getRandomWord(minLen: int=1, maxLen: int=1000):
  """
  docstring
  """
  filtered = list(filter(lambda w: (w.length()>=minLen and w.length()<=maxLen), GlobalDictionary.allWords))
  count = len(filtered)
  if count==0:
    return ""
  index = random.randint(0, count-1)
  word = filtered[index]
  length = word.length()
  #print(index, length)
  return word.value