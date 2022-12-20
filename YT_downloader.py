from pytube import YouTube
from sys import*
import re

def Find(string):
    url = re.findall('http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+',string)
    return url

def Video_Downloader(path):
    
    temp = 1
    
    with open(path) as fp:
        
        for line in fp:
            
            url = Find(line)
            
            for str in url:
                    
                video = YouTube(str)
                video_streams = video.streams.filter(file_extension='mp4').get_by_itag(18)

                video_streams.download(filename = "{}.mp4".format(temp),
                output_path = "Youtube_Videos")
                
                print("{}) Video downloaded Successfully in the Youtube_Videos folder...".format(temp))
                
                temp = temp + 1


def main():
    print("----------YouTube downloader By Prajwal Patil------------")
    
    print("Application name : "+argv[0])
    
    if(len(argv) != 2):
        print("Error : Invalid number of arguments")
        exit()
        
    if(argv[1] == "-h") or (argv[1] == "-H"):
        print("This script is used to traverse youtube url file and download this videos")
        exit()
        
    if(argv[1] == "-u") or (argv[1] == "-U"):
        print("Usage : ApplicationName AbsolutePath_of_Directory Extention")
        exit()
        
    try:
        Video_Downloader(argv[1])

    except ValueError:
        print("Error : Invalid datatype of input")
        
if __name__ ==  "__main__":
    main()