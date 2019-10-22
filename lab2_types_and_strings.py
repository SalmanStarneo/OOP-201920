#course: Object-oriented programming, year 2, semester 1
#academic year: 201920
#author: B. Schoen-Phelan
#date: 29-09-2019
#purpose: Lab 2

class Types_and_Strings:
    def __init__(self):
        pass

    def play_with_strings(self):
        # working with strings
        message = input("Enter your name: ")
        print("\nOriginally entered: "+ message)
        print('\nfirst letter:'+message[:1])
        print('\nlast letter:'+message[-1:])
        # # print only first and last of the sentence
        # first = message[:1]
        print("\n\t1-He said \n \"that's fantastic \"")
        # last =  message[-1:1]

       # print("The last character is:",last)
        # use slice notation
        print('\nthe amount of a in your name = ',message.count('a'))

        letter=input('\n now Enter the letter you want to look for within your name:')
        Value=message.find(letter)

        if(Value!=-1):
            print('\n The letter ',letter,' is found in position',(Value+1))
        else:
            print('\n The letter ',letter,' does not exist in the name')
        # escaping a character
        
            print("\n The letters in your name adds up to:",len(message)," letters")
        Xletter=input('\n Enter a letter you want to replace a in your name:')
        nameExtra=message.replace('a',Xletter)
        print(nameExtra)

        # find all a's in the input word and count how many there are

        print('//////////////////////////////')
        
        for i in range(0,len(message),2):
            print(message[i])

        print('////////////////////////////')
        # replace all occurences of the character a with the - sign
        # try this first by assignment of a location in a string and
        # observe what happens, then use replace()


        # printing only characters at even index positions


    def play_with_lists(self):
        message = input("Please enter a whole sentence: ")
        print("Originally entered: "+ message)

        # hand the input string to a list and print it out
        XList=message.split(' ')

        print("\n",XList)

        # append a new element to the list and print
        newitem=input("\n Please enter an item to the list:")
        XList.append(newitem)

        print('\n',XList)
        # remove from the list in 3 ways
        print('\nnow the item that just been added will be removed\n')

        print(XList.pop(),'\n',XList)

        # check if the word cake is in your input list
        #lent=len(XList)
        

        for i in XList:
            if any("cake" for i in XList):
                print('\n you seems to have found the stash of cake\n')
                break
            else:
                print('\nNo sweets for you \n')

        print(XList*3)
        
        X2List=XList

        X2List.reverse()
        
        print('\n',X2List)        

                
        # reverse the items in the list and print


        # reverse the list with the slicing trick


        # print the list 3 times by using multiplication



tas = Types_and_Strings()
#tas.play_with_strings()
tas.play_with_lists()