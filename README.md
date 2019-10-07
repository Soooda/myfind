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

Given a directory without flags:
```Bash
$ ./myfind.py ~
/home
/home/run_tests.sh
/home/README
/home/myfind.py
/home/test
/home/test/commandMultiProcess.out
/home/test/findRegex.sortin
/home/test/hello.sh
/home/test/pathNoExist.errorin
/home/test/commandWithFlag.in
/home/test/listHome.out
/home/test/STDERR
/home/test/findRegex.out
/home/test/findName.out
/home/test/commandOnly{}.out
/home/test/listHome.sortin
/home/test/commandOnly{}.in
/home/test/processCannotStart.errorin
/home/test/pathNoExist.out
/home/test/commandWithFlag.out
/home/test/commandMultiProcess.sortin
/home/test/findName.sortin
/home/test/processCannotStart.out
```

Given a directory and a regex pattern:
```Bash
$ ./myfind.py ~ --regex="\.in$"
test/commandWithFlag.in
test/commandOnly{}.in
```

Given a directory and a name:
```Bash
$ ./myfind.py . --name="run_tests.sh"
./run_tests.sh
```

Given a directory, a name and a regex (Error):
```Bash
$ ./myfind.py . --name="run_tests.sh" --regex="\.in$"
STDERR: Usage: myfind [--regex=pattern | --name=filename] directory [command]
```

Given a directory (non exist):
```Bash
$ ./myfind.py tests
STDERR: Usage: myfind [--regex=pattern | --name=filename] directory [command]
```

Cannot start processes:
```Bash
$ ./myfind.py test "fail {}"
STDERR: Error: Unable to start process 'fail test'
STDERR: Error: Unable to start process 'fail test/commandMultiProcess.out'
STDERR: Error: Unable to start process 'fail test/findRegex.sortin'
STDERR: Error: Unable to start process 'fail test/hello.sh'
STDERR: Error: Unable to start process 'fail test/pathNoExist.errorin'
STDERR: Error: Unable to start process 'fail test/commandWithFlag.in'
STDERR: Error: Unable to start process 'fail test/listHome.out'
STDERR: Error: Unable to start process 'fail test/STDERR'
STDERR: Error: Unable to start process 'fail test/findRegex.out'
STDERR: Error: Unable to start process 'fail test/findName.out'
STDERR: Error: Unable to start process 'fail test/commandOnly{}.out'
STDERR: Error: Unable to start process 'fail test/listHome.sortin'
STDERR: Error: Unable to start process 'fail test/commandOnly{}.in'
STDERR: Error: Unable to start process 'fail test/processCannotStart.errorin'
STDERR: Error: Unable to start process 'fail test/pathNoExist.out'
STDERR: Error: Unable to start process 'fail test/commandWithFlag.out'
STDERR: Error: Unable to start process 'fail test/commandMultiProcess.sortin'
STDERR: Error: Unable to start process 'fail test/findName.sortin'
STDERR: Error: Unable to start process 'fail test/processCannotStart.out'
```

Run a command with flag(s):
```Bash
$ ./myfind.py . "ls -l {}"
total 20
-rwxr-xr-x 1 user user 4539 Oct  7 07:00 myfind.py
-rw-r--r-- 1 user user  379 Oct  7 07:00 README
-rwxr-xr-x 1 user user 1858 Oct  7 07:00 run_tests.sh
drwxr-xr-x 2 user user 4096 Oct  7 07:00 test
-rwxr-xr-x 1 user user 1858 Oct  7 07:00 ./run_tests.sh
-rw-r--r-- 1 user user 379 Oct  7 07:00 ./README
-rwxr-xr-x 1 user user 4539 Oct  7 07:00 ./myfind.py
total 76
-rw-r--r-- 1 user user  612 Oct  7 07:00 commandMultiProcess.out
-rw-r--r-- 1 user user   13 Oct  7 07:00 commandMultiProcess.sortin
-rw-r--r-- 1 user user   28 Oct  7 07:00 commandOnly{}.in
-rw-r--r-- 1 user user    6 Oct  7 07:00 commandOnly{}.out
-rw-r--r-- 1 user user   33 Oct  7 07:00 commandWithFlag.in
-rw-r--r-- 1 user user 5589 Oct  7 07:00 commandWithFlag.out
-rw-r--r-- 1 user user   15 Oct  7 07:00 findName.out
-rw-r--r-- 1 user user   24 Oct  7 07:00 findName.sortin
-rw-r--r-- 1 user user   46 Oct  7 07:00 findRegex.out
-rw-r--r-- 1 user user   21 Oct  7 07:00 findRegex.sortin
-rwxr-xr-x 1 user user   11 Oct  7 07:00 hello.sh
-rw-r--r-- 1 user user  579 Oct  7 07:00 listHome.out
-rw-r--r-- 1 user user    2 Oct  7 07:00 listHome.sortin
-rw-r--r-- 1 user user    6 Oct  7 07:00 pathNoExist.errorin
-rw-r--r-- 1 user user   70 Oct  7 07:00 pathNoExist.out
-rw-r--r-- 1 user user   15 Oct  7 07:00 processCannotStart.errorin
-rw-r--r-- 1 user user 1133 Oct  7 07:00 processCannotStart.out
-rw-r--r-- 1 user user 1133 Oct  7 07:00 STDERR
-rw-r--r-- 1 user user 612 Oct  7 07:00 ./test/commandMultiProcess.out
-rw-r--r-- 1 user user 21 Oct  7 07:00 ./test/findRegex.sortin
-rwxr-xr-x 1 user user 11 Oct  7 07:00 ./test/hello.sh
-rw-r--r-- 1 user user 6 Oct  7 07:00 ./test/pathNoExist.errorin
-rw-r--r-- 1 user user 33 Oct  7 07:00 ./test/commandWithFlag.in
-rw-r--r-- 1 user user 579 Oct  7 07:00 ./test/listHome.out
-rw-r--r-- 1 user user 1133 Oct  7 07:00 ./test/STDERR
-rw-r--r-- 1 user user 46 Oct  7 07:00 ./test/findRegex.out
-rw-r--r-- 1 user user 15 Oct  7 07:00 ./test/findName.out
-rw-r--r-- 1 user user 6 Oct  7 07:00 ./test/commandOnly{}.out
-rw-r--r-- 1 user user 2 Oct  7 07:00 ./test/listHome.sortin
-rw-r--r-- 1 user user 28 Oct  7 07:00 ./test/commandOnly{}.in
-rw-r--r-- 1 user user 15 Oct  7 07:00 ./test/processCannotStart.errorin
-rw-r--r-- 1 user user 70 Oct  7 07:00 ./test/pathNoExist.out
-rw-r--r-- 1 user user 5589 Oct  7 07:00 ./test/commandWithFlag.out
-rw-r--r-- 1 user user 13 Oct  7 07:00 ./test/commandMultiProcess.sortin
-rw-r--r-- 1 user user 24 Oct  7 07:00 ./test/findName.sortin
-rw-r--r-- 1 user user 1133 Oct  7 07:00 ./test/processCannotStart.out
```

Run a command with a single pair of curly brackets (treat it as running a executable):
```Bash
$ echo echo hello > hello.sh
$ chmod +x hello.sh
$ ./myfind.py . --name="hello.sh" "{}"
hello
```

Run multi-processes:
```Bash
$ ./myfind.py test "wc {}"
STDERR: wc: test: Is a directory
0       0       0 test
19  76 612 test/commandMultiProcess.out
2  2 21 test/findRegex.sortin
1  2 11 test/hello.sh
1 1 6 test/pathNoExist.errorin
3  5 33 test/commandWithFlag.in
23  23 579 test/listHome.out
19  133 1133 test/STDERR
2  2 46 test/findRegex.out
1  1 15 test/findName.out
1 1 6 test/commandOnly{}.out
1 1 2 test/listHome.sortin
3  3 28 test/commandOnly{}.in
2  3 15 test/processCannotStart.errorin
1  7 70 test/pathNoExist.out
150  676 5589 test/commandWithFlag.out
2  3 13 test/commandMultiProcess.sortin
2  2 24 test/findName.sortin
19  133 1133 test/processCannotStart.out
```
