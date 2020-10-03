from domain.types import Dictionary
import domain.usecase as uc

if __name__ == "__main__":

  #dict = Dictionary("./French-Dictionary")
  #print(dict.listFiles())
  #f = "dictionary.txt"
  #ret = Dictionary("./French-Dictionary").loadFile()
  #print(ret)
  print(uc.getRandomWord(9 , 15))