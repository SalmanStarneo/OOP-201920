# course: Object-oriented programming, year 2, semester 1
# academic year: 201920
# author: B. Schoen-Phelan
# date: 10-10-2019
# purpose: Lab 4

class WordCloud:

    # initialises everything
    # everything gets kicked off here
    def __init__(self):
        self.my_dict = self.create_dict()

        if self.my_dict:
            self.create_html(self.my_dict)
        else:
            print("issue with the input file")

    def create_html(self, the_dict):
        fo = open("output.html", "w")
        fo.write('<!DOCTYPE html>\
            <html>\
            <head lang="en">\
            <meta charset="UTF-8">\
            <title>Tag Cloud Generator</title>\
            </head>\
            <body>\
            <div style="text-align: center; vertical-align: middle; font-family: arial; color: white; background-color:black; border:1px solid black">')

        for key in the_dict.keys():
            fo.write('<span style="font-size: ')
            fo.write(str(the_dict[key] * 20))
            fo.write('px"> ')

            fo.write(key)
            fo.write('</span>')

        fo.write('</div>\
                    </body>\
                    </html>')


    def create_dict(self):
        my_dict = {}
        try:
            fo=open("gettisburg.txt","r")
        except Exception as e:
            my_dict=False
            print("Caught this error: %s"% e.__class__.__name__)
        else:
            for line in fo:
                line = line.lower()
                line=line.split()
                for word in line:
                    self.add_to_dict(word, my_dict)
        fo.close()

        return my_dict

    # helper function that is called from
    # create_dict
    # receives a word and a dictionary
    # does the counting of the key we are at and adds 1
    # if this word already exists. Otherwise sets the
    # word occurance counter to 1
    # returns a dictionary
    def add_to_dict(self, word, the_dict):
        for key in the_dict.keys():
            if key == word:
                the_dict[key]=the_dict[key]+1
                return the_dict
        else:
            the_dict[word]= 1
            return the_dict


wc = WordCloud()
