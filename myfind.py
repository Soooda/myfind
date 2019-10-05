#!/usr/bin/env python3
import os
import sys
import re

USAGE = "Usage: myfind [--regex=pattern | --name=filename] directory [command]"

def subprocess(command, path): 
    pid = os.fork() 
    
    if pid > 0: 
        os.wait()
    else: 
        os.execl('bash', command, path)

def find(directory, regex=None, name=None, command=None):
    # Saving the walking data
    walk = {} # key = root, value = (dirs(tuple), files(tuple))
    for tup in os.walk(directory):
        walk[tup[0]] = (tuple(tup[1]), tuple(tup[2]))
    # print(walk)
    
    output = [] # Output lines collection
    
    # directory
    if (regex is None) and (name is None):
        for i in walk.items():
            output.append(i[0])
            for f in i[1][1]:
                output.append(i[0] + '/' + f) # adds sub-file
    # Name flag
    elif name is not None:
        for i in walk.items():
            # Check the directory name
            if i[0].split('/')[-1] == name:
                output.append(i[0])
            # Check the file name
            elif name in i[1][1]:
                output.append(i[0] + '/' + name) # adds the path found
    # Regex flag
    elif regex is not None:
        for i in walk.items():
            # Check the directory name
            if re.search(regex, i[0].split('/')[-1]) is not None:
                output.append(i[0])
            # Check the file name
            for filename in i[1][1]:
                if re.search(regex, filename) is not None:
                    output.append(i[0] + '/' + filename) # adds the path found
                
    # If there is not command input, print
    if command is None:
        for line in output:
            print(line)
        return
    
    # String process "command flags {}"
    command_spl = command.split()
    
    for path in output:
        command_spl[-1] = path
        # print(command_spl)
        pid = os.fork() 
    
        if pid > 0: 
            os.wait()
        else: 
            os.execlp(command_spl[0], *command_spl)

        
    
    

if __name__ == "__main__":
    # No command line arguments given
    if len(sys.argv) == 0:
        sys.exit(USAGE)
    
    args = [None, None, None, None]
    first_no_flag = True
    
    flag_counter = 0 # Record how many flags
    for line in sys.argv[1:]: # Exclude the filename
        # RegEx flag
        if line.startswith('--regex='):
            args[1] = line[8:] # Get rid of the '--regex='
            args[1] = args[1].strip("\"") # Get rid of the quotes
            flag_counter += 1
        # Name flag
        elif line.startswith('--name='):
            args[2] = line[7:] # Get rid of the '--name='
            flag_counter += 1
        # Directory
        elif first_no_flag:
            # Add the directory from command line arguments
            args[0] = sys.argv[1].replace('~', '/home') # Replace ~ to /home
            first_no_flag = False
        # Command
        else:
            args[3] = line.strip("\"") # Strip the quotes
    
    # If more than one flags are received
    if flag_counter > 1:
        sys.exit(USAGE)
        
    find(*args)