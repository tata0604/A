word=input("Enter the string : ")


# AND operation
print("AND operation :")
for x in word:
    AND_string=ord(x)&127
    print(chr(AND_string),end="")
    
print("\n-----------------------")


# XOR operation
print("XOR operation :")
for x in word:
    XOR_string=ord(x)^127
    print(chr(XOR_string),end="")

print("\n-----------------------")


#---------------------------------------------------------------------------------------------------------
#code in C

#include<stdio.h>
#include <string.h>
  

#using namespace std;

# int main(){

#     char str[]="Hello World";
#     int i,len;
#     len=strlen(str);
#     for(i=0;i<len;i++)
#     {
#     printf("%c",str[i]&127);
#     }
#     printf("\n");
#     for(i=0;i<len;i++)
#     {
#     printf("%c",str[i]^127);
#     }
#     printf("\n");
    
#     return 0;
# }
