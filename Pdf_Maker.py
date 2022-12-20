import os
from PIL import Image
from sys import*

def PdfMaker():

    files = os.listdir()
    
    image_type = ['jpg','jpeg','png','psd']
    images = []
    
    for x in files:
        for y in image_type:
            if y in str(x):
                temp = Image.open(x)
                temp = temp.convert('RGB')
                images.append(temp)
                break

    name = input('Enter name for the file : ')

    images[0].save('{}.pdf'.format(name),save_all=True, append_images=images[1:])
    
    print("Pdf created successfully...")
    
    print()
    print("Do you want to remove that images..?  Y/N")
    ans  = input()
    
    if(ans == 'y' or ans == 'Y'):
        for x in files:
            for y in image_type:
                if y in str(x):
                    os.remove(x)
        
        print("Images are deleted successfully..")
        
    else:
        print('Ok..Images does not deleted..')
        exit()
    

def main():
    #print("--------------------------------------")
    print()
    print("---------{_by Prajwal Patil_}---------") 

    print("Application name : " +argv[0])
    print()

    if(len(argv) != 1):
        print("Error : Invalid number of arguments")
        exit()
    
    PdfMaker()
    
if __name__ == "__main__":
    main()