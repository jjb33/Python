'''
Some ideas:
-start with small words first
-ask for max length of word and create a list to select from
-ask for how many words (get random words from list creating a new list of this length)
-ask for a login which will store previous lists (by entered name). Present user with a list of previous word lists to go back to
-find a way to collect the words consistently wrong to another list for focused practice later
-create own list by selecting from available
-try to use only words in the list for instructions
-have user pick a color for page/words. Maybe a picture too
-you need rewards, but how do you get feedback on how the user answered? Self submitted? (Maybe can steel M-W pronunciations lol)
'''

import random
import time

fry100test = ['the', 'of', 'and', 'a', 'to', 'you', 'that']
fry100all = ['the', 'of', 'and', 'a', 'to', 'in', 'is', 'you', 'that', 'it', 'he', 'was', 'for', 'on', 'are', 'as', 'with', 'his', 'they', 'I', 'at', 'be', 'this', 'have', 'from', 'or', 'one', 'had', 'by', 'words', 'but', 'not', 'what', 'all', 'were', 'we', 'when', 'your', 'can', 'said', 'there', 'use', 'an', 'each', 'which', 'she', 'do', 'how', 'their', 'if', 'will', 'up', 'other', 'about', 'out', 'many', 'then', 'them', 'these', 'so', 'some', 'her', 'would', 'make', 'like', 'him', 'into', 'time', 'has', 'look', 'two', 'more', 'write', 'go', 'see', 'number', 'no', 'way', 'could', 'people', 'my', 'than', 'first', 'water', 'been', 'called', 'who', 'oil', 'sit', 'now', 'find', 'long', 'down', 'day', 'did', 'get', 'come', 'made', 'may', 'part']
fry100all.sort(key = len)
ongoing = ['the', 'of', 'a', 'I', 'in', 'on', 'for', 'is']
# print('Let me show you all the words in the Fry 100')
# t=0
# while t != 19:

#     for x in fry100all:
#         print x[t]
        

def getmaxlenlist (maxlen):
    maxlenlist = []
    for word in fry100all:
        if len(word) <= maxlen:
            maxlenlist.append(word)
        else:
            continue
    return maxlenlist

def getnumwordslist (numwords, maxlenlist):
    numwordslist = random.sample(maxlenlist, numwords)
    return(numwordslist)

def getalist ():
    while True:
        inpmaxlen = input('how many letters can be in the word? (Pick a number 1-6)?\n')
        try:
            int(inpmaxlen)
            break
        except:
            print('That is not a number. Try again')
            continue
    maxlen = (int(inpmaxlen))
    maxlenlist = getmaxlenlist(maxlen)
    print('There are', len(maxlenlist), 'words with that many letters.\n')
    while True:
        inpnumwords = input(('How many words do you want to practice with? (Pick a number between 1 and', str(len(maxlenlist)) + ')'))
        try:
            int(inpnumwords)
        except:
            print('That is not a number. Try again.')
            continue
        numwords = (int(inpnumwords))
        if numwords < 1:
            print('Please pick at least one or we can\'t play!')
            continue
        if numwords > len(maxlenlist):
            if int(inpnumwords) == 1:
                print('There is only 1 matching word.')
                continue
            else:
                print('There are only', len(maxlenlist), 'words with', maxlen, 'letters or less')
                continue
        else:
            break
    return getnumwordslist(numwords, getmaxlenlist(maxlen))

def play():
    choice = input('What list do you want to use? Type random or ongoing.\n')
    if choice == 'random':
        playlist = getalist()
    if choice == 'ongoing':
        playlist = ongoing
    # print('\n\nHere\'s your list of words:\n\n')
    # for word in playlist:
    #     print(word)    
    print('\nHere we go!\n', '~~~~~~~~~~~~~~~~\n\n\n')
    inp = None
    while inp != 'q':
        print('What is this word?\n\n\n')
        word1 = random.sample(playlist,1) #poplation, sample size
        print(f'**********\n {word1[0]}\n**********\n\n\n')
        inp = input('ENTER for a new word, Q to quit, or N for a new game)')
        if inp == 'n'or inp == 'N':
            play()

         
#    Would you like to play again with new words?

play()
print('See you soon!')
time.sleep(2)
p =[]
for x in reversed(range(100)):
    p.append(x)
for x in p:
    print('.' * x)
# for x in random.sample(p, 70):
#     print('>' * x)
print('Finished')
exit()





# #Create 20 lists of 5 and add to dictionary
# n = 1
# d= {}
# workinglist = []
# for i in randindex:
#     if len(workinglist) == 5:
#         d[str('fry5' + str(n))] = workinglist
#         n += 1
#         workinglist = []
#     else:
#         workinglist.append(fry100all[i])

# print(d)


    
    
    

