#Mind where you run this !
#Too much files may overload
import os

start_point = os.getcwd()

def list_files(_dir):
    dirs = os.listdir(_dir)
    for dir in dirs:
        next_dir = os.path.join(_dir,dir)
        if not os.path.isdir(next_dir):
            print(dir + ' is file not dir !!! ')
        else:
            list_files(next_dir)
