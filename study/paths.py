#!/usr/bin/python3

import sys, os
import datetime
import os.path

#Path source: https://stackoverflow.com/questions/595305/how-do-i-get-the-path-of-the-python-script-i-am-running-in
#Source of above source: http://www.faqs.org/docs/diveintopython/regression_path.html


print('sys.argv[0] =', sys.argv[0])
pathname = os.path.dirname(sys.argv[0])
fullpath = os.path.abspath(pathname)
print('path =', pathname)
print('full path =', os.path.abspath(pathname))

filename = fullpath + "/path.out"
f = open(filename, "w+")
f.write(str(datetime.datetime.now()))
f.write('\nsys.argv[0] =' + sys.argv[0])
f.write('\npath =' + pathname)
f.write('\nfull path =' + fullpath)
f.write("\n")



print();print()

#Check if file exist source: https://linuxize.com/post/python-check-if-file-exists/

dir_to_check = fullpath + "/test_dir"
file_to_check = dir_to_check + "/test_file"

if os.path.exists(dir_to_check):
    print("dir exists"); f.write("\ndir exists")
else:
    print("dir not exists"); f.write("\ndir not exists")


if os.path.isfile(file_to_check):
    print ("File exist"); f.write("\nFile exist")
else:
    print ("File not exist"); f.write("\nFile not exist")

f.close()
