from cgi import test
from pickle import TRUE
import tests.test as tester
import os
#       "id": "7c7dc8c4bf0ed066f4c8ac6571b176fa5604d477",


def DJ_Mode():
   isSeeked = False
   isSaved = False

   

   

   while TRUE:
      if isSaved == False:
           with open('musics.txt', 'w', encoding='utf-8') as f:
               f.write(tester.p1.getCurrentPlayingSong())
               isSaved = True
               isSeeked = False

      with open('musics.txt', encoding='utf-8') as f:
        lines = f.read()
        if lines.find(tester.p1.getCurrentPlayingSong()) == -1:
           ##print(lines)
           ##print(tester.p1.getCurrentPlayingSong())
           # seek to segment
           if isSeeked == False:
              tester.p1.seekMusic()
              with open('musics.txt', 'w', encoding='utf-8') as f:
                   f.write("")
              isSeeked = True
              isSaved = False




           # rewrite

       
       

if __name__ == "__main__":
   # tester.runTests()
   print("POWERED BY SCRIPT")
   DJ_Mode()




