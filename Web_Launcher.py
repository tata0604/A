from sys import*
import webbrowser
import re
import urllib

def is_connected():
    try:
        urllib.urlopen('https://www.google.com/',timeout = 1)
        return True
    except Exception as E:
        return False
    
def Find(string):
    url = re.findall('http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+',string)
    return url

def WebLauncher(path):
    with open(path) as fp:
        for line in fp:
            print(line)
            url = Find(line)
            print(url)
            for str in url:
                webbrowser.open(str,new = 2)
    



def main():
    print("-----By Prajwal Patil-----")
    
    print("Application name : "+argv[0])
    
    if(len(argv) != 2):
        print("Error : Invalid number of arguments")
        exit()
        
    if(argv[1] == "-h") or (argv[1] == "-H"):
        print("This script is used to open URL which is written in one file")
        exit()
        
    if(argv[1] == "-u") or (argv[1] == "-U"):
        print("Usage : ApplicationName Name_Of_File")
        exit()
        
    try:
        WebLauncher(argv[1])

        
    except ValueError:
        print("Error : Invalid datatype of input")
    except Exception as E:
        print("Error : Invalid input",E)    
    
        
if __name__ ==  "__main__":
    main()