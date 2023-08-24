from english_words import english_words_set as ews

def initWords(words):
  ans = set()
  for w in words:
    if len(w) == 5 and w[0].upper() != w[0]: ans.add(w)
  return ans

def initScore():
  a = dict()
  b = dict()
  c = dict()
  d = dict()
  e = dict()
  score = [a, b, c, d, e]
  return score

def chooseWord(words):
  for w in words:
    return w

def getHint():
  ans = list(input())
  ans = [int(i) for i in ans]
  return ans

def missingScore(word, hint, score):
  for i, h in enumerate(hint):
    if h != 0: continue
    for s in score:
        s[word[i]] = -1
      
def misplacedScore(word, hint, score, count):
  #print(len(score))
  for i, h in enumerate(hint):
    if h != 1: continue
    if word[i] in count: count[word[i]] += 1
    else: count[word[i]] = 1
    for j, s in enumerate(score):
      #print(word, i, j)
      if word[j] == word[i]: continue
      s[word[i]] = 0
      #print(i, j)
    #print(score)
    score[i][word[i]] = -1

def correctScore(word, hint, score):
  for i, h in enumerate(hint):
    if h != 2: continue
    score[i] = word[i]

def updateScore(word, hint, score, count):
  missingScore(word, hint, score)
  #print(score)
  misplacedScore(word, hint, score, count)
  #print("misplaced", score)
  correctScore(word, hint, score)
  #print("correct", score)

def updateValidWords(validWords, word, hint):
  ans = set()
  count = dict()
  score = initScore()
  updateScore(word, hint, score, count)
  #print("updateValid", score)
  #print(count)
  for w in validWords:
    #print(w)
    valid = True
    countCopy = count.copy()
    for i, l in enumerate(w):
      if type(score[i]) == str: #correct
        if l != score[i]: 
          #print(1)
          valid = False
          break
        else: continue
      if l in score[i] and score[i][l] == -1: #missing
        #print("missing: ", l)
        valid = False
        break
      if l in countCopy: #misplaced
        #guaranteed to be in score[i]
        countCopy[l] -= 1
    for c in countCopy:
      if countCopy[c] > 0:
        #if w == "knoll":
          #print("misplaced: ", c)
          #print(countCopy)
          #print(score)
        valid = False
        break
    if valid: 
      #print(w, valid)
      ans.add(w)
  return ans

def wordle(words):
  validWords = initWords(words)
  
  while True:
    #print(len(validWords))
    word = chooseWord(validWords)
    #word = "skunk"
    print(word)
    hint = getHint()
    validWords = updateValidWords(validWords, word, hint)
    #print(validWords)

wordle(ews)



  


