import io
import os
import os.path as path

class Word():
  """
  defines a word
  """
  def __init__(self, dictline: str):
    super().__init__()
    split = dictline.split(';')
    self.value = split[0]
    self.options = split[1:]
  def length(self):
    """
    return the length of the word
    """
    return len(self.value)

class Adjective(Word):
  """
  docstring
  """
  def __init__(self, dictline):
    super().__init__(dictline)
    self.female = self.options[0]=='epi' or self.options[0]=='fem'
    self.male = self.options[0]=='epi' or self.options[0]=='mas'
    self.singular = self.options[1]=='sg' 
    self.plural = self.options[1]=='pl' 
    #print(self.value, self.plural)

class Adverb(Word):
  """
  docstring
  """
  def __init__(self, dictline):
    super().__init__(dictline)

dictionaryStructure = {
  "adjectives.txt": {
    "useClass" : Adjective
  },
  "adverbs.txt" : {
    "useClass" : Adverb

  },
  "default" : {
    "useClass" : Word

  }
}

class Dictionary():
  """
  defines a Dictionary with all the words
  """
  def __init__(self, basepath: str):
    super().__init__()
    self.basepath = basepath
    self.allWords = []
    self.dictionarypath = path.join(self.basepath, "dictionary")

  def listFiles(self):
    return list(filter(lambda f: f!="dictionary.txt", os.listdir(self.dictionarypath)))

  def wordCount(self):
    return len(self.allWords)

  def loadFile(self, filepath: str = None):
    """
    load a file from the Dictionary storage
    """
    if filepath == None:
      filepath = "dictionary.txt"
    file = io.open(path.join(self.dictionarypath, filepath), encoding="UTF-8", mode="r")
    struct = dictionaryStructure[filepath] if filepath in dictionaryStructure else dictionaryStructure["default"]
    useClass = struct["useClass"]
    count = 0
    for l in file.readlines():
      self.allWords.append(useClass(l.rstrip()))
      count += 1
    return (count, len(self.allWords))
