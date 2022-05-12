from domain.types import Dictionary, Word
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


mapIn  = u"éêëèáàâäúùûüíìîïóòôöýÿÉÊËÈÁÀÂÄÚÙÛÜÍÌÎÏÓÒÔÖÝŸ"
mapOut = u"eeeeaaaauuuuiiiiooooyyEEEEAAAAUUUUIIIIOOOOYY"
translateTable = dict(zip([ord(c) for c in mapIn], mapOut))
def removeUnicode(w:str):
  return w.translate(translateTable)

def findByPattern(pattern: str):
  def filter_func(w:Word):
    if w.length() != len(pattern):
      return False
    word = removeUnicode(w.value).upper()
    patternU = removeUnicode(pattern).upper()
    for i in range(w.length()):
      if patternU[i] != "_" and patternU[i] != word[i]:
        return False
    return True

  return list(map(lambda w:w.value, filter(filter_func, GlobalDictionary.allWords)))