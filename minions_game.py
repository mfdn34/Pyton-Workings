"""
Kevin and Stuart want to play the 'The Minion Game'.

Game Rules

Both players are given the same string, .
Both players have to make substrings using the letters of the string .
Stuart has to make words starting with consonants.
Kevin has to make words starting with vowels.
The game ends when both players have made all possible substrings.

Scoring
A player gets +1 point for each occurrence of the substring in the string .

For Example:
String  = BANANA
Kevin's vowel beginning word = ANA
Here, ANA occurs twice in BANANA. Hence, Kevin will get 2 Points.
"""
vowels = ["A", "E", "I", "İ", "O", "Ö", "U", "Ü"]
consonants = ["Q", "Z", "W", "S", "X", "D", "C", "R", "F", "V",
              "T", "G", "B", "Y", "H", "N", "J", "M", "K", "L", "P", "Ç", "Ğ", "Ş"]

S = input("Please a word or a sentence: ").upper()

while True:
    if len(S) < 10**6:
        break
    else:
        S = input("Please enter fewer characters: ").upper()

stuart = []
kevin = []

wordlist = []  # Wordlist keeps all possibilities

"""
for loop generates all possibilities of
subset of word and assigns these values to wordlist.
"""
for i in range(len(S)+1):  
    for j in range(i):
        wordlist.append(S[j:i])

for i in range(len(wordlist)): 
    if wordlist[i][0] in vowels:
        kevin.append(wordlist[i][0])
    if wordlist[i][0] in consonants:
        stuart.append(wordlist[i][0])

#print("Stuart :", len(stuart))
#print("Kevin :", len(kevin))

if len(stuart)>len(kevin) : print("Stuart ", len(stuart))  
elif len(stuart)<len(kevin) : print("Kevin ", len(kevin))
else : print("Draw")
