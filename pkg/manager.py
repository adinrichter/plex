from os.path import dirname, basename, isfile, join
import glob

modules = glob.glob(join(dirname(__file__), "*.py"))

def return_commands():
    commands = [basename(f)[:-3] for f in modules if isfile(f) and f.startswith('cmd_')]
    print(commands)
    
    
if __name__ == "__main__":
    return_commands()