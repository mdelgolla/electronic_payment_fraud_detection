import mysql.connector
import sys

originalcol = 'payeeId'
updatecolname = 'col2'
tablename = 'transaction'
database = 'orelpay'
# start index
id = 1

print('------------------------------------------------------')
for i, arg in enumerate(sys.argv):
    if i == 1:
        originalcol = arg
        print("Setting original coloumn name: ", originalcol)
    if i == 2:
        updatecolname = arg
        print("Setting update column name: ", updatecolname)
    if i == 3:
        tablename = arg
        print("Setting tablename: ", tablename)
    if i == 4:
        database = arg
        print("Setting database: ", database)
    if i == 5:
        id = int(arg)
        print("Setting start index: ", id)

print('------------------------------------------------------')

#TODO: change db details
mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="root",
  port="8889",
  database=database
)

mycursor = mydb.cursor()

def updatecol(original, value):
    if not original:
        sql = "UPDATE "+tablename+" SET "+updatecolname+" = '"+str(value)+"' WHERE "+originalcol+" IS NULL"
    else:
        sql = "UPDATE "+tablename+" SET "+updatecolname+" = '"+str(value)+"' WHERE "+originalcol+" = '"+original+"'"
    mycursor.execute(sql)
    mydb.commit()
    return mycursor.rowcount

mycursor.execute("SELECT DISTINCT("+originalcol+") FROM "+tablename+" t WHERE "+updatecolname+" IS NULL")
myresult = mycursor.fetchall()

for x in myresult:
    original = x[0]
    print("[Updating]")
    rows = updatecol(original, id)
    print(f'{originalcol}: {original} - {updatecolname}: {id}\t\t {rows} rows affected.\n')
    id += 1

print(f'\n\n--------------------SUMMARY-------------------------')
print(f'DATABASE NAME:\t\t\t {database}')
print(f'TABLENAME:\t\t\t {tablename}')
print(f'ORIGINAL COLOUMN:\t\t {originalcol}')
print(f'PROCESSED COLOUMN:\t\t {updatecolname}')
print(f'----------------------------------------------------')
