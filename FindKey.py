import hashlib
import os
filename="C:\\Users\\Kang\\Desktop\\aa.dcf"

enc_file=open(filename,"rb")
filesize = os.path.getsize(filename)
data=enc_file.read(filesize)
enc_file.close()
encrypt_data=data.split(";Size=\"")[1].split("\"\x0d\x0a")[1]



sig="49443303000000".decode('hex')
#번호등록된 폰이 아이폰이라면 900000000 ~ 9999999999
#번호등록된 폰이 안드로이드폰이라면 10[전화번호8자리] ex)1012341234

for i in range(1000000000,1100000000):
    
    st=str(i)
    data_hash=data[0x0e:0x53]
    data_hash+="min"
    data_hash+=st
    data_hash+=( chr(ord(st[0])^0xFF) + chr(ord(st[1])^0xFF) + chr(ord(st[2])^0xFF) + chr(ord(st[3])^0xFF) +chr(ord(st[4])^0xFF) + chr(ord(st[5])^0xFF) + chr(ord(st[6])^0xFF) + chr(ord(st[7])^0xFF) +chr(ord(st[8])^0xFF) + chr(ord(st[9])^0xFF))
    data_hash+="SSE Primary-Level Base Key Generation"
    
    m = hashlib.sha1()
    m.update(data_hash)
    data_hash=m.digest()
  
    if (ord(encrypt_data[0])^ord(data_hash[0]))==ord(sig[0]):

        if (ord(encrypt_data[1])^ord(data_hash[1]))==ord(sig[1]):
            if (ord(encrypt_data[2])^ord(data_hash[2]))==ord(sig[2]):
                if (ord(encrypt_data[3])^ord(data_hash[3]))==ord(sig[3]):
                    if (ord(encrypt_data[4])^ord(data_hash[4]))==ord(sig[4]):
                        if (ord(encrypt_data[5])^ord(data_hash[5]))==ord(sig[5]):
                            if (ord(encrypt_data[6])^ord(data_hash[6]))==ord(sig[6]):
                                print("KEY="+str(i))
                        
                
print("End")
