data = "From h1234567@ncku.edu.tw Tue Sep 27 10:14:16 2016"
# answer:Tue Sep 27 10:14:16 2016 From h7654321@ncku.edu.tw
pos1= data.find("h")
print(pos1)#5
pos2= data.find("@")
print(pos2)#13
data=data[0:pos1+1]+"7654321"+data[pos2:]
print(data)#0to6 +7654321+@...... 
pos3=data.find("Tue")
print(pos3)
modifieddata=data[pos3:]+ " "+data[:pos3]
print(modifieddata)