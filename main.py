#!/usr/bin/python
# -*- coding: utf-8 -*-
'''
This script has to be encoded in utf-8. (:set fileencoding=utf-8)
Because of the special FR-Chars é, û
'''

import os
import sys
import numbers

try:
    source_dir = sys.argv[1]
    files = os.listdir(source_dir)
except IndexError:
    source_dir = ""
    files = 'No source folder given.'

print sys.argv[0]
print files


class File:
    def __init__(self, filename):
        self.filename = filename
        self.path = os.path.join(os.path.abspath(source_dir), self.filename)
        months = {'01': u'Janvier',
                  '02': u'Février',
                  '03': u'Mars',
                  '04': u'Avril',
                  '05': u'Mai',
                  '06': u'Juin',
                  '07': u'Juillet',
                  '08': u'Août',
                  '09': u'Septembre',
                  '10': u'Octobre',
                  '11': u'Novembre',
                  '12': u'Décembre',
                  }

        def splitname(filename=self.filename):

            try:
                isinstance(int(filename[:4]), numbers.Number)

                year = filename[:4]
                month = ' '.join([months[filename[4:6]], year[2:4]])
                day = filename[6:8]

            except ValueError:

                year = filename[4:8]
                month = ' '.join([months[filename[8:10]], year[2:4]])
                day = filename[10:12]

            return {'year': year, 'month': month, 'day': day}

        self.date = splitname()



sorted_root_dir = sys.argv[2]
out = sorted_root_dir

classed_filenames = []
for i in files:
    try:
        classed_filenames.append(File(i))

    except KeyError:
        '''
        if the file don't follow the pattern, ignore it.
        '''
        pass


if not os.path.isdir(out):
    # checks if the dir exists otherwise create it
    # NOTE REMOVE ON PROD
    
    user_input = raw_input("The output root directory doesn't exists."
                            "Continue (Y/n): "
                            )
    if user_input == 'Y':
    #user_input = raw_input("The output root directory doesn\'t exists. Create it? (Y/n): ")
        os.mkdir(out)
    else:
        sys.exit("Aborded")

for i in classed_filenames:
    # first we create the needed dirs
    path_year = os.path.join(out, i.date['year'])
    path_month = os.path.join(path_year, i.date['month'])
    path_file = os.path.join(path_month, i.filename)
    if not os.path.isdir(path_month) and not os.path.isdir(path_year):
        os.makedirs(path_month)
    else:
        if not os.path.isdir(path_month):
            os.mkdir(path_month)
    # then we hardlink the files
    # pass if file already exists 
    # NOTE this should be prevented before !!
    try:
        os.link(i.path, path_file)
    except OSError:
        pass


# print 'Debug'
# print classed_filenames[1].date['month']
