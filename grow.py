import mysql.connector
import requests
import json

response = requests.get('http://glsindia-dev.cisco.com:3838/data/output.json')
print(type(response))
mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="sachin123",
  database="casesdb"
)
mycursor = mydb.cursor()
data = response.json()
cases = data['cases']
sql = "TRUNCATE TABLE casestbl;"
mycursor.execute(sql)

def funcCreatedb():
    sql = "create table IF NOT EXISTS casestbl (id INT PRIMARY KEY,  created_at VARCHAR(50),  action_id INT,  building_id VARCHAR(50), related_kase VARCHAR(50));"
    mycursor.execute(sql)
    myresult = mycursor.fetchall()
    # print(len(myresult))
    # for x in myresult:
    #     print(x)
    # mycursor.execute("select * from casestbl")
    # print(mycursor.fetchall())

funcCreatedb()

for row in cases:
    values = " "
    count = 0
    # for key, value in row.items():
    for idx, value in enumerate(row.items()):
        if count > 4:
            values = values[:-1]
            break
        # print(type(idx))
        # print(key)
        # print(value[1])
        if idx == 1 or idx == 3 or idx == 4:
            count += 1
            values += '"'+str(value[1]) + '"' + ","
            continue
        values += str(value[1]) + ","
        count += 1
    # values = str(values)
    sql = "INSERT INTO casestbl(id,created_at,action_id,building_id,related_kase) "
    sql = sql + "VALUES (" + values +" )"
    #print(sql)
    mycursor.execute(sql)
    mydb.commit()

sql = "select * from casestbl"
mycursor.execute(sql)
myres = mycursor.fetchall()
for x in myres:
    print(x)
