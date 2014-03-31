#! /usr/bin/python
#
# Data crawler for POJBadge
#
# Author: Bowei Zhang (psyclaudeZ)
#
import requests
import urllib2
import json

from BeautifulSoup import BeautifulSoup as BS

class Crawler:
    ######################
    # constructor
    def __init__(self, user_name = ''):
        self._name = user_name
        self._solved = -1
        self._submission = -1
        self._school = ''
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


    ######################
    # utility methods

    # fetch user info from POJ
    # Return: True if successfully fetched or False, otherwise
    def crawl(self):
        # request HTML
        html = urllib2.urlopen('http://poj.org/userstatus?user_id=' + self._name)

        # parse returned HTML
        soup = BS(html)

        # retrieve relavent fields
        elem = soup.findAll('td', {'width' : '25%'})

        if len(elem) == 0:
            print 'Empty result. Please make sure the user name is correct.'
            return False
        else:
            # elem from index 1 to last but one are designated fields
            fields = elem[1:-1]

            # for each field, do some ad hoc extraction...
            # not actually good coding style...
            vals = []
            for f in fields:
                fs = str(f)
                vals.append(fs[fs.rfind('">') + 2 : fs.find('</')])

            self.set_rank(int(vals[0]))
            self.set_solved(int(vals[1]))
            self.set_submission(int(vals[2]))
            self.set_school(vals[3])

            return True

    # print statistics of the user
    def user_info(self):
        print 'User Name:', self._name
        print 'Rank:', self._rank
        print 'Submission:', self._submission
        print 'Solved:', self._solved
        print 'School:', self._school

    # end of utility methods
    ######################


# c = Crawler('vjudge1')

# c.crawl()
# c.user_info()
