import smtplib, ssl
import random
from BitVector import *
import time, socket, sys,os

if not sys.warnoptions:
    import warnings
    warnings.simplefilter("ignore")
    
ip=[57, 49, 41, 33, 25, 17,  9,  1, 59, 51, 43, 35, 27, 19, 11,  3, 61,53, 45, 37, 29, 21, 13,  5, 63, 55, 47, 39, 31, 23, 15,  7, 56, 48,40, 32, 24, 16,  8,  0, 58, 50, 42, 34, 26, 18, 10,  2, 60, 52, 44,36, 28, 20, 12,  4, 62, 54, 46, 38, 30, 22, 14,  6]	
e=[31,  0,  1,  2,  3,  4,  3,  4,  5,  6,  7,  8,  7,  8,  9, 10, 11, 12, 11, 12, 13, 14, 15, 16, 15, 16, 17, 18, 19, 20, 19, 20, 21, 22, 23, 24, 23, 24, 25, 26, 27, 28, 27, 28, 29, 30, 31,  0]
p=[15,  6, 19, 20, 28, 11, 27, 16,  0, 14, 22, 25,  4, 17, 30,  9,  1,7, 23, 13, 31, 26,  2,  8, 18, 12, 29,  5, 21, 10,  3, 24]
s_box= []
s_box.append([[14,4,13,1,2,15,11,8,3,10,6,12,5,9,0,7],[0,15,7,4,14,2,13,1,10,6,12,11,9,5,3,8],[4,1,14,8,13,6,2,11,15,12,9,7,3,10,5,0],[15,12,8,2,4,9,1,7,5,11,3,14,10,0,6,13]])
s_box.append([[15,1,8,14,6,11,3,4,9,7,2,13,12,0,5,10],[3,13,4,7,15,2,8,14,12,0,1,10,6,9,11,5],[0,14,7,11,10,4,13,1,5,8,12,6,9,3,2,15],[13,8,10,1,3,15,4,2,11,6,7,12,0,5,14,9]])
s_box.append([[10,0,9,14,6,3,15,5,1,13,12,7,11,4,2,8],[13,7,0,9,3,4,6,10,2,8,5,14,12,11,15,1],[13,6,4,9,8,15,3,0,11,1,2,12,5,10,14,7],[1,10,13,0,6,9,8,7,4,15,14,3,11,5,2,12]])
s_box.append([[7,13,14,3,0,6,9,10,1,2,8,5,11,12,4,15],[13,8,11,5,6,15,0,3,4,7,2,12,1,10,14,9],[10,6,9,0,12,11,7,13,15,1,3,14,5,2,8,4],[3,15,0,6,10,1,13,8,9,4,5,11,12,7,2,14]])
s_box.append([[2,12,4,1,7,10,11,6,8,5,3,15,13,0,14,9],[14,11,2,12,4,7,13,1,5,0,15,10,3,9,8,6],[4,2,1,11,10,13,7,8,15,9,12,5,6,3,0,14],[11,8,12,7,1,14,2,13,6,15,0,9,10,4,5,3]])
s_box.append([[12,1,10,15,9,2,6,8,0,13,3,4,14,7,5,11],[10,15,4,2,7,12,9,5,6,1,13,14,0,11,3,8],[9,14,15,5,2,8,12,3,7,0,4,10,1,13,11,6],[4,3,2,12,9,5,15,10,11,14,1,7,6,0,8,13]])
s_box.append([[4,11,2,14,15,0,8,13,3,12,9,7,5,10,6,1],[13,0,11,7,4,9,1,10,14,3,5,12,2,15,8,6],[1,4,11,13,12,3,7,14,10,15,6,8,0,5,9,2],[6,11,13,8,1,4,10,7,9,5,0,15,14,2,3,12]])
s_box.append([[13,2,8,4,6,15,11,1,10,9,3,14,5,0,12,7],[1,15,13,8,10,3,7,4,12,5,6,11,0,14,9,2],[7,11,4,1,9,12,14,2,0,6,10,13,15,3,5,8],[2,1,14,7,4,10,8,13,15,12,9,0,3,5,6,11]])
inv_ip=[39,  7, 47, 15, 55, 23, 63, 31, 38,  6, 46, 14, 54, 22, 62, 30, 37,5, 45, 13, 53, 21, 61, 29, 36,  4, 44, 12, 52, 20, 60, 28, 35,  3, 43, 11, 51, 19, 59, 27,34,  2, 42, 10, 50, 18, 58, 26, 33,  1, 41,9, 49, 17, 57, 25, 32,  0, 40,  8, 48, 16, 56, 24]
pc_2=[13, 16, 10, 23,  0,  4,  2, 27, 14,  5, 20,  9, 22, 18, 11,  3, 25,7, 15,  6, 26, 19, 12,  1, 40, 51, 30, 36, 46, 54, 29, 39, 50, 44,32, 47, 43, 48, 38, 55, 33, 52, 45, 41, 49, 35, 28, 31]
pc_1=[56, 48, 40, 32, 24, 16,  8,  0, 57, 49, 41, 33, 25, 17,  9,  1, 58,50, 42, 34, 26, 18, 10,  2, 59, 51, 43, 35, 62, 54, 46, 38, 30, 22,14,  6, 61, 53, 45, 37, 29, 21, 13,  5, 60, 52, 44, 36, 28, 20, 12,4, 27, 19, 11,  3]

def encrypt(messages):
    rno=0 
    #message = BitVector(hexstring = messages)
    #print('in encr 1 ', type(messages))
    message = BitVector(textstring = messages)
    #print('in encr 2', type(message))
    message=message.permute(ip) 
    [l0,r0]=message.divide_into_two()
    
    while(rno<16):
        j=0
        l1=r0
        rf=r0.permute(e)  
        rf=rf ^ k[rno]
        output=''
        bitno=0
        while(j<8):
            i=0
            s=[]
            while (i < 6):
                s.append(str(rf[bitno]))
                bitno+=1
                i += 1
            index1=int((s[0]+s[-1]),2)
            index2=int(''.join(s[1:5]),2)
            s=hex(s_box[j][index1][index2])
            output+=s[2:]
            j+=1
        
        rf=BitVector(hexstring=output)
        output=rf.permute(p)
        output=output^l0 
        r1=output
        l0=l1
        r0=r1
        rno+=1
    output=r1+l1
    output=output.permute(inv_ip)
    myhexstring = output.get_hex_string_from_bitvector()
    return myhexstring

def decrypt(messages):
    k.reverse()
    rno=0
    message = BitVector(hexstring = messages)
    message=message.permute(ip)
    [l0,r0]=message.divide_into_two()
    while(rno<16):
        j=0
        l1=r0
        rf=r0.permute(e)
        rf=rf ^ k[rno]
        output=''
        bitno=0
        while(j<8):
            i=0
            s=[]
            while ( i < 6):
                s.append( str(rf[bitno]) )
                bitno+=1
                i += 1
            index1=int((s[0]+s[-1]),2)
            index2=int(''.join(s[1:5]),2)
            s=hex(s_box[j][index1][index2])
            output+=s[2:]
            j+=1
        
        rf=BitVector(hexstring=output)
        output=rf.permute(p)
        output=output^l0
        r1=output
        l0=l1
        r0=r1
        rno+=1
    output=r1+l1
    output=output.permute(inv_ip)
    #myhexstring = output.get_hex_string_from_bitvector()
    myhexstring = output.get_text_from_bitvector()
    return myhexstring 

def generate_key(key):
    key64 = BitVector(hexstring = key)
    key56=key64.permute(pc_1)
    global k 
    k=[]
    rno=1
    [c,d]=key56.divide_into_two()
    while(rno<=16):
        if(rno==1 or rno==2 or rno==9 or rno==16):
            c<<1
            d<<1
        else:
            c<<2
            d<<2
        key56=c + d
        key48=key56.permute(pc_2)
        k.append(key48)
        rno+=1 


print("\nWelcome....\n")
print("Initialising....\n")
time.sleep(1)

s = socket.socket()
host = socket.gethostname()
ia = socket.gethostbyname(host)
port = 1234
s.bind((host, port))
print(host, "(", ia, ")\n")
name = input(str("Enter your name: "))
           
s.listen(1)
print("\nWaiting for incoming connections...\n")
conn, addr = s.accept()
print("Received connection from ", addr[0], "(", addr[1], ")\n")

s_name = conn.recv(1024)
s_name = s_name.decode()
print(s_name, "has connected \nEnter [e] to exit \n")
conn.send(name.encode())

port = 465
smtp_server = "smtp.gmail.com"
sender_email = "abc707038@gmail.com"
password = "@abc7038"
mail_id = conn.recv(1024)
receiver_email = mail_id.decode()
print(receiver_email)
ran = random.randrange(10**80)
myhex = "%016x" % ran

#limit string to 64 characters
myhex = myhex[:16]

key = str(myhex)
context = ssl.create_default_context()

with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
    server.login(sender_email, password)
    server.sendmail(sender_email, receiver_email, key)

while True:
    '''print('1.Chat')
    print('2.File Transfer')
    print('3.Exit')
    print('Enter your choice:')'''
    message = input("Me : ")
    #print(type(message))
    if message == "[e]":
        message = "Left chat room!"
        conn.send(message.encode())
        print("\n")
        break
    i = 0
    j = 0
    msg_chunk = []
    enc_chunk = []
    while (i < len(message)):
        l = i+8
        #print('l',l)
        if l < len(message):
            #print('in if',i+8)
            msg_chunk.append(message[i:l])
            j = j+1
            
        else:
            msg_chunk.append(message[i:len(message)])
            j = j+1
            #print('j',j)
            #print(l-len(message))
            s1 = ' '*(l-len(message))
            msg_chunk[j-1] += s1 
        i += 8
    
    i = 0
    j = 0
    #print(msg_chunk)		
    for i in msg_chunk:
        generate_key(key)
        m = encrypt(msg_chunk[j])
        j = j+1
        enc_chunk.append(m)
    enc_msg = ''.join(map(str,enc_chunk))
    #print('Encrypted message='+enc_msg)
    conn.send(enc_msg.encode())
    ###################
    message = conn.recv(1024)
    print(s_name, "encrypted:", message)
    message = message.decode()
    if message == 'Left !' :
        break
    i1 = 0
    j1 = 0
    msg1_chunk = []
    enc1_chunk = []
    while (i1 < len(message)):
        l1 = i1+16
        #print('l',l)
        if l1 < len(message):
            #print('in if',i+8)
            msg1_chunk.append(message[i1:l1])
            j1 = j1+1
            
        else:
            msg1_chunk.append(message[i1:len(message)])
            j1 = j1+1
            #print('j',j)
            #print(l-len(message))
            s2 = ' '*(l1-len(message))
            msg1_chunk[j1-1] += s2 
        i1 += 16
    
    i1 = 0
    j1 = 0
    #print(msg_chunk)		
    for i1 in msg1_chunk:
        generate_key(key)
        m1 = decrypt(msg1_chunk[j1])
        j1 = j1+1
        enc1_chunk.append(m1)
    enc1_msg = ''.join(map(str,enc1_chunk))

    #m = m.decode()
    print(s_name, "decrypted:", enc1_msg)