import math
from cryptography.fernet import Fernet

def GCD(a,b):
    if (b==0):
        return a
    else:
        return(b,a%b)
    
p=int(input(" p :"))
q=int(input(" q :"))

n=p*q

e=2
k=2

phi=(p-1)*(q-1)

while(e<phi):
    if(GCD(e,phi)==1):
        break
    else:
        e+=1
    
d=int(((k*phi)+1)/e)


print(f"Public Key (e,n) : ({e},{n})")
print(f"Private Key (d,n) : ({d},{n})")

msg = input("Enter you Message : ")


key = Fernet.generate_key()

fernet = Fernet(key)

encryptedMSG = fernet.encrypt(msg.encode())
decryptedMSG = fernet.decrypt(encryptedMSG).decode()

print("original string : ", msg)
print("Encrypted String : ", encryptedMSG)
print("decrypted string : ", decryptedMSG)
