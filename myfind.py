#!/usr/bin/env python3
import os
import sys
import re

USAGE = "Usage: myfind [--regex=pattern | --name=filename] directory [command]"

def replacebrackets(li, path):
    result = []

    i = 0
    while i < len(li):
        if '{}' in li[i]:
            result.append(li[i].replace('{}',path))
        else:
            result.append(li[i])
        i += 1
    
    return result

def find(directory, regex=None, name=None, command=None):
    # Saving the walking data
    walk = {} # key = root, value = (dirs(tuple), files(tuple))
    for tup in os.walk(directory):
        walk[tup[0]] = (tuple(tup[1]), tuple(tup[2]))
    # print(walk)
    
    # The directory doesn't exist. 
    # Treat it as an invalid command line argument, and print out the usage string
    if walk == {}:
        sys.exit(USAGE)
        
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
    should_exit = False
    
    for path in output:
        args = replacebrackets(command_spl, path)
        # print(command_spl)
        
        pid = os.fork() 
    
        if pid == 0: # Child
            try:
                os.execlp(args[0], *args)
            except OSError:
                # String formatting
                args_str = ''
                for a in args:
                    args_str += a
                    args_str += ' '

                args_str = args_str[:-1]
                sys.exit("Error: Unable to start process '{}'".format(args_str))
        elif pid == -1: # Process cannot start
            sys.exit("Error: Unable to start process '{}'".format(''.join(args)))
        else: # Parent
            status = os.wait()
            exitcode = status[1] >> 8 # Get the high byte
            # If the child ends with non-zero exitcode, the parent exits as well
            if exitcode != 0:
                should_exit = True

    # Exit with a non-zero exitcode
    if should_exit:
        sys.exit(1)
        
    
    

if __name__ == "__main__":
    # No command line arguments given
    if len(sys.argv) == 0:
        sys.exit(USAGE)

    # print(sys.argv)
    
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
            args[0] = line.replace('~', '/home') # Replace ~ to /home
            first_no_flag = False
        # Command
        else:
            args[3] = line.strip("\"") # Strip the quotes
        # print(args)
    
    # If more than one flags are received
    if flag_counter > 1:
        sys.exit(USAGE)

    find(*args)