from domain.types import Dictionnary
import domain.usecase as uc

if __name__ == "__main__":

  #dict = Dictionnary("./French-Dictionary")
  #print(dict.listFiles())
  #f = "dictionary.txt"
  #ret = Dictionnary("./French-Dictionary").loadFile()
  #print(ret)
  print(uc.getRandomWord(9 , 15))