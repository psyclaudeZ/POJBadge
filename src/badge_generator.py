#! /usr/bin/python
#
# Badge generator for POJBadge
# 
# Author: Bowei Zhang (psyclaudeZ)
#

from PIL import Image

class Badge_Generator: 
    ######################
    # constructor
    def __init__(self, name = 'test'):
        self._name = name
        self._submission =  -1
        self._solved = -1
        self._school = ''
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
        try:
        # by default, using the user name as the image name
            if name == '':
                name = self._name

            # resize and generate the backgound and save it in the output folder
            self._image = Image.open('../resources/poj_background.jpg').\
                    resize((200, 80))

            # self._image.save('../out/' + name + '.png', 'PNG')
            return True
        # handle the exception of unsuccessful generation
        except:
             print 'Failed to generate background.'
             return False

# g = Badge_Generator()
# g.generate_background()
