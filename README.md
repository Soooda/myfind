# MyFind
A python program to mimic the behaviour of bash command find

**The Find Command**
All Unix-like systems (Linux, etc) have a command called "find". This command allows you to search the file system name-space for a file that satisfies some criteria.
For example, you might search for a file with a particular name (exact match), or you might search for a file with a name that matches a regular expression pattern. You might search for a file that has certain characteristics such as created after a particular date or has certain permissions (eg writable).
You can see the detailed specification of this command using the Unix man command, eg `man find`.

**Specification**
To implement a very simplified version of the Unix find command.
The syntax is:
myfind.py [--regex=pattern | --name=filename] directory [command]
myfind.py is the command name
directory is a required argument for the path to the directory to traverse
filename is the exact filename to match against when traversing the directory
pattern is the regular expression pattern to match against when traversing the
directory
Only one of --regex= pattern or --name= filename should be provided. If
neither are provided, then list all files found during the traversal. These flags may be
located anywhere in the argument list.
command is an optional argument which is a Unix command that has {} in the
command string replaced by the file name that is currently being executed on. If this
argument is not provided, then just list the file paths of the discovered files. This
string should be a simple command with an argument list (e.g. no redirections or
pipes).