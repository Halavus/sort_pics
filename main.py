#!/usr/bin/python
# -*- coding: utf-8 -*-
'''
This script has to be encoded in utf-8. (:set fileencoding=utf-8)
Because of the special FR-Chars é, û
'''

import os
import sys
from subprocess import Popen as Popen
from subprocess import PIPE as PIPE

import numbers

try:
    source_dir = sys.argv[1]
    files = os.listdir(source_dir)
except IndexError:
    source_dir = ""
    files = 'No source directory given.'

print files


class File:
    def __init__(self, filename):
        self.filename = filename
        self.path = os.path.join(source_dir, self.filename)
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
                try:
                    isinstance(int(filename[:4]), numbers.Number)

                    year = filename[:4]
                    month = ' '.join([months[filename[4:6]], year[2:4]])
                    day = filename[6:8]

                except ValueError:

                    year = filename[4:8]
                    month = ' '.join([months[filename[8:10]], year[2:4]])
                    day = filename[10:12]

            except KeyError:
                raise ValueError("No valid month found.")

            if int(year) in range(1990, 2100):
                return {'year': year, 'month': month, 'day': day}
            else:
                raise ValueError("No valid year found.")

        self.date = splitname()
        
        def caller(lst): 
            '''bash command if more than 1 word have to be in a list'''
            proc = Popen(lst, stdout=PIPE)
            output = proc.stdout.read()
            return output

        if caller(["which", "md5deep"]):
            '''returns True if md5deep is installed'''
            if os.path.isfile(self.path):
                md5check = caller(["md5deep", self.path, "-k"])
                '''
                md5deep -k outputs: "md5sum */path/of/file"
                -k adds * before the path
                '''
                self.md5sum = md5check[:md5check.find("*") - 1]
            else:
                raise ValueError(
                    ' '.join([self.path, "Is maybe a directory?"]))
        else:
            raise OSError("md5deep not installed")
        

sorted_root_dir = sys.argv[2]
out = sorted_root_dir

classed_filenames = []

# TODO At this point files should be diffed with already sorted ones
# best using md5sum
for i in files:
    try:
        classed_filenames.append(File(i))

    except ValueError:
        '''
        if the file don't follow the pattern, ignore it.
        '''
        pass


if not os.path.isdir(out):
    # checks if the dir exists otherwise create it

    if classed_filenames:
        user_input = raw_input("The output root directory doesn't exists."
                               "Continue (Y/n): "
                               )
    else:
        sys.exit("No file to sort found.")
    if user_input == 'Y':
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


def debug():
    for i in classed_filenames:
        print ' '.join([i.filename, i.md5sum])
