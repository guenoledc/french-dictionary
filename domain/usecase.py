from domain.types import Dictionnary
import random

GlobalDictionary = Dictionnary("./French-Dictionary")
GlobalDictionary.loadFile()

def getRandomWord(minLen: int=1, maxLen: int=1000):
  """
  docstring
  """
  count = GlobalDictionary.wordCount()
  len = 0
  word = None
  while len < minLen or len > maxLen:
    index = random.randint(0, count-1)
    word = GlobalDictionary.allWords[index]
    len = word.length()
  return word.value