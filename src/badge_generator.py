#! /usr/bin/python
#
# Badge generator for POJBadge
# 
# Author: Bowei Zhang (psyclaudeZ)
#

from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw
from PIL import ImageOps

class Badge_Generator: 
    ######################
    # constructor
    def __init__(self, name = 'zbw163'):
        self._name = name
        self._submission = 364 
        self._solved = 219 
        self._school = 'New York University'
        self._rank = 2974
        self._image = None
    # end of constructor
    ######################


    ######################
    # access methods below
    def set_user_name(self, name):
        self._name = name

    def get_user_name(self):
        return self._name

    def set_rank(self, rank):
        self._rank = rank

    def get_rank(self):
        return self._rank

    def set_submission(self, submission):
        self._submission = submission

    def get_submission(self):
        return self._submission

    def set_solved(self, solved):
        self._solved = solved

    def get_solved(self):
        return self._solved

    def set_school(self, school):
        self._school = school

    def get_school(self):
        return self._school
    # end of access
    #######################
    

    #######################
    # utility methods

    # generate the "background" of the badge
    # default values: 
    #     + size is normal (200 * 60). Others to be implemented
    #     + name is the image name
    # output:
    #     + True, if successful
    #     + False, if failed
    def generate_background(self, size = 'normal', name = ''):
        #try:
        # by default, using the user name as the image name
        if name == '':
            name = self._name

        # resize and generate the backgound and save it in the output folder
        self._image = Image.open('../resources/poj_background.jpg').\
                resize((200, 60))

        # set canvas for appending text
        draw = ImageDraw.Draw(self._image)

        # set font
        largeFont = ImageFont.truetype("/Library/Fonts/Times New Roman Bold.ttf",\
            12);
        smallFont = ImageFont.truetype("/Library/Fonts/Arial.ttf",\
            10);

        # append text to the canvas
        draw.text((5, 5), 'PKU JudgeOnline', (0, 0, 255), largeFont)

        draw.text((5, 20), self._name, (0, 0, 255), largeFont)

        draw.text((5, 35), 'Rank:', (0, 0, 0), smallFont)
        draw.text((35, 35), str(self._rank), (255, 0, 0), smallFont)

        draw.text((5, 45), 'AC%:', (0, 0, 0), smallFont)
        draw.text((35, 45), str(round(self._solved * 100. / self._submission,\
            2)), (0, 0, 255), smallFont)

        draw.text((80, 35), 'Solved:', (0, 0, 0), smallFont)
        draw.text((140, 35), str(self._solved), (0, 0, 255), smallFont)

        draw.text((80, 45), 'Submission:', (0, 0, 0), smallFont)
        draw.text((140, 45), str(self._submission), (0, 0, 255), smallFont)

        # append border to the original image
        self._image = ImageOps.expand(self._image, border = 2, fill = 'grey')

        # save the image
        self._image.save('../out/' + name + '.png', 'PNG')
        return True
        # handle the exception of unsuccessful generation
        #except:
        #     print 'Failed to generate background.'
        #     return False

    # end of utility methods
    #######################

     
g = Badge_Generator()
g.generate_background()
