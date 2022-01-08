import random


print('''\n          ---------------------------------------------------------
          |                RANDOM USERNAME GENERATOR              |
          ---------------------------------------------------------''')

# get user input
num = int(input("\nNumber of random usernames to generate: "))
print("")


#read censor list
with open('banned.txt','r') as inline:
    censored = inline.read().strip(' \n').split('\n')


# read word lists from two files
with open('nouns.txt', 'r') as infile:
    nouns = infile.read().strip(' \n').split('\n')
with open('adjectives.txt', 'r') as infile:
    adjectives = infile.read().strip(' \n').split('\n')



x = 1

# generate usernames random from nuons.txt and adj.txt
for i in range(num):

    # construct username
    word1 = random.choice(adjectives)
    word2 = random.choice(nouns)

    #check if word2 is censored
    if word2 in censored:
        i -= 1
        continue
    #else make and print the username

    #captilaize first letter
    word1 = word1.title()
    word2 = word2.title()

    username = '{}{}{}'.format(word1, word2, random.randint(1, 99))

    # success
    print("%d) %s\n " % (x, username))
    x += 1