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
# print(len(cases))
# sql = "TRUNCATE TABLE casestbl;"
# mycursor.execute(sql)
def funcCreatedb():
    sql = "create table IF NOT EXISTS casestbl (id INT PRIMARY KEY,  created_at VARCHAR(50),  action_id INT,  building_id VARCHAR(50), related_kase VARCHAR(50),type VARCHAR(50),urgency VARCHAR(50) ,urgency_justification VARCHAR(50),impact VARCHAR(50),impact_justification VARCHAR(50),org_id VARCHAR(50),synopsis VARCHAR(50),opener_id VARCHAR(50),requester_id VARCHAR(50),status VARCHAR(50),closed_at VARCHAR(50),reopened_count VARCHAR(50),assignee_id VARCHAR(50),duplicate_kase_id VARCHAR(50),latest_updater_id VARCHAR(50),resolved_at VARCHAR(50),latest_updated_at VARCHAR(50),location_in_lab VARCHAR(50),lab_space_id VARCHAR(50),related_remedy_kase_ids VARCHAR(50),business_group_id VARCHAR(50),onsite_approval VARCHAR(50),workflow_id VARCHAR(50),opener_userid VARCHAR(50),requester_userid VARCHAR(50),assignee_userid VARCHAR(50),latest_updater_userid VARCHAR(50),action VARCHAR(50),business_group VARCHAR(50),building_name VARCHAR(50),metro_name VARCHAR(50),org_name VARCHAR(50),approval_manager_id VARCHAR(50),kase_participant_ids VARCHAR(50),lab_contact_id VARCHAR(50),lab_manager_contact_id VARCHAR(50),purchase_request_numbers VARCHAR(50));"
    mycursor.execute(sql)
    myresult = mycursor.fetchall()
    # print(len(myresult))
    # for x in myresult:
    #     print(x)
    # mycursor.execute("select * from casestbl")
    # print(mycursor.fetchall())

# funcCreatedb()

for row in cases:
    values = " "
    finalValues = []
    count = 0
    # for key, value in row.items():
    for idx, value in enumerate(row.items()):
        # if count > 4:
        #     values = values[:-1]
        #     break
        # print(type(idx))
        # print(key)
        # print(value[1])
        # if idx == 25 or idx == 38:
        #         #     print(idx,value,type(value[1]))
        #         #     continue
        # if(type(value[1]) is list):
        #     print(idx, value, type(value))
        #     finalValues.insert(idx,value[1])
        #     continue

        #if idx == 1 or idx == 3 or idx == 4:
        count += 1
        values += '"'+str(value[1]) + '"' + ","
        finalValues.insert(idx,value[1])
        #continue
        # values += str(value[1]) + ","
        # finalValues.insert(idx,value[1])
        # count += 1
    # values = str(values)
    print(values)
    #print(finalValues)

    sql = "INSERT INTO casestbl(id,created_at,action_id,building_id,related_kase,type,urgency,urgency_justification,impact,impact_justification,org_id,synopsis,opener_id,requester_id,status,closed_at,reopened_count,assignee_id,duplicate_kase_id,latest_updater_id,resolved_at,latest_updated_at,location_in_lab,lab_space_id,related_remedy_kase_ids, business_group_id,onsite_approval,workflow_id,opener_userid,requester_userid,assignee_userid,latest_updater_userid,action,business_group,building_name,metro_name,org_name,approval_manager_id,kase_participant_ids,lab_contact_id,lab_manager_contact_id,purchase_request_numbers) "
    sql = sql + "VALUES (" + values +" )"
    #print(sql)
    # mycursor.execute(sql)
    # mydb.commit()

# sql = "select * from casestbl"
# mycursor.execute(sql)
# myres = mycursor.fetchall()
# for x in myres:
#     print(x)


