username = input("Enter your username: ")
numofwords = int(input("How many words do you want to type? "))

def play(username,numofwords):
  import random
  import timeit
  import time
  

  print("Hello",username+"!")
  print("Lets see how fast you can type!")
  
  mode = input("What difficulty typing test do you want to take: \n(e)asy, (m)edium, or (h)ard?  ").strip().lower() 
  if(mode=='e'):
    words = ["the", "and", "for", "are", "but", "not", "you", "all", "any", "can", "had", "her", "was", "one", "our", "out", "day", "get", "has"]
  elif(mode=='m'):
    words=["which","first","their","after","other","years","would","about","where","later","known","three","under","being","there","south"]
   
  else:
    words = ["perfect", "Tuesday", "country", "pumpkin", "special", "America", "freedom", "picture", "husband", "monster", "seventy", "Melissa", "nothing", "jessica", "sixteen", "morning", "journey", "history", "Georgia", "fifteen", "amazing", "rihanna", "January", "dolphin", "teacher", "forever"]
  
  words = random.sample(words,numofwords)
    
  print("Words appear in 3 seconds! Get ready to type!")
  for i in range(3,0,-1):
    print(str(i)+"...")
    time.sleep(1)
  
  print(' '.join(words)+"\n")
  #lines with timeit from this link: https://stackoverflow.com/questions/65498320/how-to-measure-the-time-elapsed-during-user-input-in-python
  start = timeit.default_timer()
  typeover=False
  lstwords = ""
  lstwords = lstwords.join(words)
  while(typeover==False):
    userinput = input("type the words above: ").strip().lower() 
    

    
    userinput = userinput.replace(" ","")#removing spaces between user's input
    if(len(userinput)==len(lstwords)):
      typeover=True
    else:
      print("Enter all of the words! ")
      start = timeit.default_timer()
      
  end = timeit.default_timer()
  
  timer = end - start
  wrongltrs = 0
  timer = round(timer,2)
  
  
  
  #caluculating user's accuracy
  for i in range(len(userinput)):
    if(lstwords[i]!=userinput[i]):
      wrongltrs = wrongltrs + 1
  
  wpm = 0
  
  
  if(mode=='e'):
    wpm = (60*(len(userinput)/3))/timer
  elif(mode=='m'):
    wpm = (60*(len(userinput)/5))/timer
  else:
    wpm = (60*(len(userinput)/7))/timer
  wpm = round(wpm,2)
  
  accuracy = ((len(lstwords) - wrongltrs)/len(lstwords))*100
  accuracy = round(accuracy, 2)
  
  print("Your wpm is:"+str(wpm))
  print("Your typing accuracy was "+str(accuracy)+"%")
  print("You answered in "+str(timer)+"s.")
  
  #https://stackoverflow.com/questions/29223246/how-do-i-save-data-in-a-text-file-python
  print("high scores: ")
  hs=open("typing_game_highscores.txt",'a')
  hs.write(username)
  hs.write(" "+str(wpm))
  hs.write(" "+mode+"\n") 
  hs.close()
  
  #https://stackoverflow.com/questions/17632428/sorting-names-by-their-high-scores
  
  scores = []
  with open("typing_game_highscores.txt") as f:
      for line in f:
        username, wpm, mode = line.split(" " , 2)
        scores.append((username, wpm, mode))
  
  scores.sort(key=lambda s: s[1], reverse = True)
    
  for username,wpm,mode in scores:
    print("username: "+username+" wpm: "+wpm+" mode: "+mode)

play(username,numofwords)
while True:
  
  playagain = input("Do you want to play again? Y or N?").strip().lower()
  if(playagain == 'y'):
    username = input("Enter your username: ")
    numofwords = int(input("How many words do you want to type? "))
    play(username,numofwords)
  else:
    print("thanks for playing!")
    break
