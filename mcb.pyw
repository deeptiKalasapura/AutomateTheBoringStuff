#! /usr/bin/python
# Usage: py.exe mcb.pyw save <keyword> - Saves clipboard to keyword.
#        py.exe mcb.pyw <keyword> - Loads keyword to clipboard.
#        py.exe mcb.pyw list - Prints all keywords to terminal.
#        py.exe mcb.pyw delete <keyword> - Deletes <keyword> from mcb.

import sys,pyperclip,shelve,pprint

mcbShelf = shelve.open('mcb')

if len(sys.argv) == 3:
    if sys.argv[1].lower() == 'save':
        mcbShelf[sys.argv[2]] = pyperclip.paste()
    if sys.argv[1].lower() == 'delete':
        del mcbShelf[sys.argv[2]]

elif len(sys.argv) ==2:
    if sys.argv[1].lower() == 'list':
        pprint.pprint(list(mcbShelf.keys()))
    elif sys.argv[1] in mcbShelf:
        pyperclip.copy(mcbShelf[sys.argv[1]])
    elif sys.argv[1].lower() == 'delete':
        mcbShelf.clear()

mcbShelf.close()

