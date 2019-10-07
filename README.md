# MyFind
A python program to mimic the behaviour of bash command find.

### The Find Command
All Unix-like systems (Linux, etc) have a command called "find". This command allows you to search the file system name-space for a file that satisfies some criteria.
For example, you might search for a file with a particular name (exact match), or you might search for a file with a name that matches a regular expression pattern. You might search for a file that has certain characteristics such as created after a particular date or has certain permissions (eg writable).

You can see the detailed specification of this command using the Unix man command, eg:

```bash
man find
```

### Specification
To implement a very simplified version of the Unix find command.

The syntax is:
```
myfind.py [--regex=pattern | --name=filename] directory [command]
```
**myfind.py** is the command name

**directory** is a required argument for the path to the directory to traverse

**filename** is the exact filename to match against when traversing the directory

**pattern** is the regular expression pattern to match against when traversing the
directory

Only one of **--regex=** pattern or **--name=** filename should be provided. If
neither are provided, then list all files found during the traversal. These flags may be
located anywhere in the argument list.

**command** is an optional argument which is a Unix command that has {} in the
command string replaced by the file name that is currently being executed on. If this
argument is not provided, then just list the file paths of the discovered files. This
string should be a simple command with an argument list (e.g. no redirections or
pipes).

### Error Handling and Assumptions
If invalid command line arguments are provided, your program should output the
following to standard error and exit with a non-zero exit code. You should also print
this for pattern is invalid or directory does not exist.

> Usage: myfind.py [--regex=pattern | --name=filename] directory
> [command]


If any of the child processes could not be started, your program should print the
following to standard error and exit with a non-zero exit code. An example is
provided in the last usage example.

> Error: Unable to start process '\<command\>'

### Testcases

For all the testcases:

1. Each argument passed to myfind is in a seperated line.

2. Testcases that will produce **non-deterministic** output will have extension ```.sortin```

3. Testcases that will produce **deterministic** output namely running certain commands will have extension ```.in```

4. Testcases that will produce **nonzero exit code and send messages to Stderr** will have extension ```.errorin```

### Usage Examples
Updating...
