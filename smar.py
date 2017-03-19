# smar.py - String MAss Replace
#
# This code is in the Public Domain (or CC0 licensed, at your option.)
# Unless required by applicable law or agreed to in writing, this
# software is distributed on an "AS IS" BASIS, WITHOUT WARRANTIES OR
# CONDITIONS OF ANY KIND, either express or implied.
#

#!/usr/bin/env python


## Fid all occurences of a string in a file
#
# @param file_path path to the file
# @param string_to_find string to find (search for)
#
# @return number of string occurence found
#
def find_string(file_path, string_to_find):

    count_found = 0
    with open(file_path) as file_to_search:
        for line in file_to_search:
            if string_to_find in line:
                count_found += 1

    return count_found


## Replace all occurences of a string in a file
#
# @param file_path path to the file
# @param string_to_find string to find (search for)
# @param new_string new string replace the found string
#
# @return number of string occurence found and replaced
#
def replace_string(file_path, string_to_find, new_string):
  
    # check if file contains any doxygen member comments to update
    count_found = find_string(file_path, string_to_find)
  
    if count_found > 0:
        # we have something to replace - go ahead
        from tempfile import mkstemp
        from shutil import move
        from os import remove, close
        import re
        # Create temp file
        fh, abs_path = mkstemp()
        with open(abs_path,'w') as new_file:
            with open(file_path) as old_file:
                for line in old_file:
                     new_file.write(line.replace(string_to_find, new_string))

	    close(fh)
        # Remove original file
        remove(file_path)
        # Move new file
        move(abs_path, file_path)

    return count_found # and replaced

  
## Replace all occurences of a string in a directory and pront report
#
# @param dir_to_process directory with files to process
# @param string_to_find string to find (search for)
# @param new_string new string replace the found string
# @param do_replace replacement will be made if set to 1, otherwise reach only
#
# @return number of string occurence found and replaced
#
def process_files(dir_to_process, string_to_find, new_string, do_replace):

    import os
    
    # Confirm our understanding what we are supposed to do
    if do_replace == 1:
        print "REPLACING string \"" + string_to_find + "\"" + "with \"" + new_string + "\""
    else:
        print "Searching for string \"" + string_to_find + "\""

    # Now do the job
    for root, dirs, files in os.walk(dir_to_process):
        for file in files:
            #if file.endswith(".rst"):
                file_path = os.path.join(root, file)
                if do_replace == 1:
                    count_found = replace_string(file_path, string_to_find, new_string)
                else:
                    count_found = find_string(file_path, string_to_find)
                if count_found > 0:
                    print str(count_found) + "\t" + file_path

    return
  

# -------------------
# Main script follows  
# -------------------
#
import sys
import re

# Functionality:
#
# This script will process all folders in path below:
dir_to_process = 'C:/Users/Krzysztof/Documents'
# Update this variable to match your configuration
#
# Note for Windows users: 
#
# Use forward-slashes instead of backslashes for this path, i.e. 'C:/msys32/esp-idf/components'.
# 
# Usage:
#
# Search for string only and print out report
# $ pyton smar.py
# Search, replace and print out report
# $ pyton smar.py -u
#
# Process input parameters to find out what we are supposed to do
do_replace = 0
if len(sys.argv) > 1:
    if sys.argv[1] == "-u":
        do_replace = 1

print "Path traversed: " + dir_to_process

# Input file:
#
# The file opened below contains list of replacements to made
# Each line of list contains string to find and a new string separated with a tab
with open("replacements.txt") as list_to_replace:
    line_count = 0
    for line in list_to_replace:
        line_count += 1
        string_to_find, string_to_replace = re.split(r'\t+', line.rstrip())
        process_files(dir_to_process, string_to_find, string_to_replace, do_replace)
