#!/usr/bin/env python
"""
====
Task
====
Initialize your list (L = []) and follow the N commands given over N lines.
Each command will be 1 of the 8 commands given above. The extend(L) method
will not be used. Each command will have its own value(s) separated by a space.

============
Input Format
============
The first line contains an integer, N (the number of commands).
The N subsequent lines each contain one of the 8 commands described above.

============
Sample Input
============
Input::
    12
    insert 0 5
    insert 1 10
    insert 0 6
    print
    remove 6
    append 9
    append 1
    sort
    print
    pop
    reverse
    print

=============
Sample Output
=============
Output::
    [6, 5, 10]
    [1, 5, 9, 10]
    [9, 5, 1]

=========
Editorial
=========
Solution::

    arr = []
    for i in range(int(raw_input())):
        s = raw_input().split()
        for i in range(1,len(s)):
            s[i] = int(s[i])

        if s[0] == "append":
            arr.append(s[1])
        elif s[0] == "extend":
            arr.extend(s[1:])
        elif s[0] == "insert":
            arr.insert(s[1],s[2])
        elif s[0] == "remove":
            arr.remove(s[1])
        elif s[0] == "pop":
            arr.pop()
        elif s[0] == "index":
            print arr.index(s[1])
        elif s[0] == "count":
            print arr.count(s[1])
        elif s[0] == "sort":
            arr.sort()
        elif s[0] == "reverse":
            arr.reverse()
        elif s[0] == "print":
            print arr
"""

from __future__ import print_function, unicode_literals


try:
    input = raw_input
except NameError:
    pass


def main():
    my_list = []
    number_of_command = int(input().strip())
    for _ in range(number_of_command):
        user_input = input().split()
        command = user_input[0]
        if command == 'append':
            my_list.append(int(user_input[-1]))
        elif command == 'insert':
            my_list.insert(int(user_input[1]), int(user_input[-1]))
        elif command == 'remove':
            my_list.remove(int(user_input[-1]))
        elif command == 'pop':
            my_list.pop()
        elif command == 'index':
            my_list.index(int(user_input[-1]))
        elif command == 'count':
            my_list.count(int(user_input[-1]))
        elif command == 'sort':
            my_list.sort()
        elif command == 'reverse':
            my_list.reverse()
        elif command == 'print':
            print(my_list)
        else:
            raise ValueError


if __name__ == '__main__':
    main()
