# course: Object-oriented programming, year 2, semester 1
# academic year: 201920
# author: B. Schoen-Phelan
# date: 08-10-2019
# purpose: Lab 3

import string

class WordScramble:
    def __init__(self):
        self.user_input = input("Please give me a sentence: ")

    def scramble(self):
        newWord=''
        # print what was input
        print("The user input was:         ", self.user_input)
        if len(self.user_input)>3:
            newWord = self.user_input[0]+self.user_input[-2]+self.user_input[1]+self.user_input[-1]
            print(newWord+' Line 19')
        elif len(self.user_input)<=3:
            print('This is a short word')
            newWord = self.user_input+'-'+self.user_input[1:]+self.user_input[0]
            print(newWord+' Line 23')
        else:
            print('try again')
            newWord=false

        Sentence=self.user_input.strip().split()
        for word in Sentence:
            Temp_word=list(word)
            if len(Sentence)>3:
                if(',' in Temp_word):
                    Tempo=Temp_word[1]
                    Temp_word[1]=Temp_word[3]
                    Temp_word[3]=Tempo
                    print(Temp_word+' Line 36')
            else:
                    Tempo=Temp_word[1]
                    Temp_word[1]=Temp_word[2]
                    Temp_word[2]=Tempo
                    Swapped=''.join(Temp_word)
                    print(Swapped+' line 41')
        #my_string = 'hello'
        #print(my_string[0])

        # Xstring = list(self.user_input)
        # Moon=Xstring[1]
        # Temp=Xstring[0]
        # Xstring[0] = Xstring[-1]
        # Xstring[1]=Xstring[-2]
        # Xstring[-1]=Temp
        # Xstring[-2]=Moon
        # print(Xstring)
        # print(''.join(Xstring))

        # first scramble is just one word
        # reverse two indices
        # particularly good to use is to switch the first two
        # and the last two
        # this only makes sense if you have a world that is longer than 3


        # now try to scramble one sentence
        # do just words first, then you can move on to work on
        # punctuation

word_scrambler = WordScramble()
word_scrambler.scramble()

