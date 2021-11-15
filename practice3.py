import mysql.connector
mydb = mysql.connector.connect(host="localhost",user="root",password="",database="abhayasena")
mycursor = mydb.cursor()
mycursor.execute("select id,sponsor from member")

result = mycursor.fetchall()

for i in result:
    print(i)
    count = 0
    for j in i:
       count+=1
       print(j)
       if (count == 1):

         yt = """ INSERT INTO modal (phonenumber) VALUES (%s); """ %j
         mycursor.execute(yt)
         mydb.commit()
       else:
         yt = """ INSERT INTO modal (userid) VALUES (%s); """ %j
         mycursor.execute(yt)
         mydb.commit()




print("sucess")