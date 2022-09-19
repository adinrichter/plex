from pkg import *

def main():
    while True:
        entry = input('> ')
        if entry != '':
            entry_command = entry.split()[0]
            entry_args = entry.split()[1:]
        else:
            main()

def get_names():
    raw = info.return_names()
    for str in raw:
        if raw[0:4] == 'cmd_':
            print(raw)

if __name__ == "__main__":
    #main()  # This is the entry point of the program
    get_names()
