

def splitIt(word):
    return [char for char in word]
     
bag=["A","A","A","A","A","A","A","A","A","B","B","C","C","D","D","D","D","E","E","E","E","E","E","E","E","E","E","E","E","F","F","G","G","G","H","H","I","I","I","I","I","I","I","I","I","J","K","L","M","M","N","N","N","N","N","N","O","O","O","O","O","O","O","O","P","P","Q","R","R","R","R","R","R","T","T","T","T","T","T","U","U","U","U","V","V","W","W","X","Y","Y","Z"]
        
import random
import string
letters=[]
for i in range (0,7):
        letter=random.choice(bag)
        bag.remove(letter)
        letters.append(letter)
        

print(letters)

input('Generate word.')
accept=False
r=1
print('Thinking...')
repeats=50
while accept==False:
        for i in range (0,repeats):
                shuffleList=letters
                random.shuffle(shuffleList)
                result = ''.join(shuffleList)
                result=splitIt(result)
                if r>0:
                        if r<6:
                                for i in range (0,r):
                                        result.pop(len(result)-1)
                result2 = ''.join(result)
                if result2 in open('dic.txt').read():
                        accept=True
                        print(result2)
                        break
        repeats=repeats+10
        if r==5:
                r=1
        else:
                r=r+1
        
        
        

        



