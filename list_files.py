#Mind where you run this !
#Too much files may overload
import os

#get currenr work directory
start_point = os.getcwd()

def list_files(_dir):
    #list directories under current
    dirs = os.listdir(_dir)
    for dir in dirs:
        #get path of next directory
        next_dir = os.path.join(_dir,dir)
        #if current one is not direcotry - print the file name
        if not os.path.isdir(next_dir):
            print(dir + ' is file not dir !!! ')
        else:
            #if current one is directory call myself
            #print(next_dir)
            list_files(next_dir)
