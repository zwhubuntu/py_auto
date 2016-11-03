import xlrd, MySQLdb, time
book = xlrd.open_workbook('test.xlsx')
sheet = book.sheet_by_name('Sheet1')

ISOTIMEFORMAT="%Y-%m-%d %X"


database = MySQLdb.Connect(host = "localhost", user = "root", passwd = "root", db = "pythontest")

cursor = database.cursor()

try:
    delete = "delete from test"
    cursor.execute(delete)
    database.commit()
except:
    print "delete something error!"
query = "insert into test (id, name, importdate) values (%s, %s, %s)"

for r in range(1, sheet.nrows):
    try:
        id = sheet.cell(r, 0).value
        name = sheet.cell(r, 1).value
        importdate = str(time.strftime(ISOTIMEFORMAT, time.localtime()))
        #print importdate
        values = (id, name, importdate)
        cursor.execute(query, values)
    except:
        print "something error!"
cursor.close()
database.commit()
database.close()


print "insert successfully, done!"