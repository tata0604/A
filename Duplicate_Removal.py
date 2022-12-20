from sys import*
import os
import hashlib
import time

def DeleteFiles(dict1):
    result = list(filter(lambda x: len(x) > 1,dict1.values()))
    
    print()
    
    ans = input("Are you sure to delete this files...?  Y/N : ")
    
    if(ans == 'y' or ans == "Y"):
    
        icnt = 0
        
        if len(result) > 0:
            for result in result:
                for subresult in result:
                    icnt += 1
                    
                    if icnt >= 2:
                        os.remove(subresult)                  
                icnt = 0
        else:
            print("No duplicate files found.")
            
        print("--> Files deleted successfully...")
            
    elif(ans == 'n' or ans == "N"):
        print("Files not deleted")  
    

def hashfile(path,blocksize = 1024):
    fd = open(path,'rb')
    hasher = hashlib.md5()
    buf = fd.read(blocksize)
    
    while len(buf) > 0:
        hasher.update(buf)
        buf = fd.read(blocksize)
    
    fd.close()
    
    return hasher.hexdigest()

def FindDuplicate(path):
    flag = os.path.isabs(path)
    
    if flag == False:
        path = os.path.abspath(path)
        
    exist = os.path.isdir(path)
    
    dups = {}
    
    if exist:
        for dirName,subdirs,fileList in os.walk(path):
            print("Current Folder is : "+dirName)
            
            for filen in fileList:
                path = os.path.join(dirName,filen)
                file_hash = hashfile(path)
                
                if file_hash in dups:
                    dups[file_hash].append(path)
                else:
                    dups[file_hash] = [path]
    
        return dups
    else:
        print("Invalid path")
        
def PrintDuplicate(dict1):
    results= list(filter(lambda x : len(x) > 1, dict1.values()))
    
    if len(results) > 0:
        print()
        print("Duplicates Found : ")
        
        print("The following files are identical.")
        
        icnt = 0
        for result in results:
            for subresult in result:
                icnt = icnt + 1
                if icnt >= 2:
                    print("\t\t%s"%subresult)
                    
        
    else:
        print("--> No duplicate files found...")
        exit()
        

def main():
    print("-------Duplicate_Removal by Prajwal Patil-------")
    
    print("Application name : "+argv[0])
    
    if(len(argv) != 2):
        print("Error : Invalid number of arguments")
        exit()
        
    if(argv[1] == "-h") or (argv[1] == "-H"):
        print("This script is used to traverse specific directory and display sizes of files")
        exit()
        
    if(argv[1] == "-u") or (argv[1] == "-U"):
        print("Usage : ApplicationName AbsolutePath_of_Directory Extention")
        exit()
        
    try:
        arr = {}
        startTime = time.time()
        
        arr = FindDuplicate(argv[1])
        
        PrintDuplicate(arr)
        
        DeleteFiles(arr)
        
        endTime = time.time()
        print('Took %s seconds to evaluate.'%(endTime - startTime))
        
    except ValueError:
        print("Error : Invalid datatype of input")
        
    except Exception as E:
        print("Error : Invalid input",E)
        
if __name__ ==  "__main__":
    main()
