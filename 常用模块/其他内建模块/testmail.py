import imaplib,pymysql,datetime

DB_name = 'countmail'
DB_host = '39.105.13.50'
DB_pass = '20140916'
DB_user = 'root'
password = '19861119Kk'
mails = {'reg1':'reg.server-001@mexmarkets.com','reg2':'reg.server-002@mexmarkets.com',
         'reg3':'reg.server-003@mexmarkets.com','reg4':'reg.server-004@mexmarkets.com',
         'reg5':'reg.server-005@mexmarkets.com'}

def getcount(usr,pw):
    with imaplib.IMAP4_SSL('imaphm.qiye.163.com',993) as M:
        M.login(usr,pw)
        res,data=M.select(mailbox='Sent')
        return int(data[0])
def db_insert(table_name,C_date,user,pa_ss):
  db = pymysql.connect(DB_host,DB_user,DB_pass,DB_name)
  cursor = db.cursor()
  cursor.execute("select date from %s  where find_in_set('%s',date)" % (table_name,C_date))
  if cursor.fetchone() is None:
         try:
                cursor.execute('insert into %s values(curdate() , %d)' % (table_name,getcount(user,pa_ss)))
                db.commit()
         except:
                db.rollback()
         finally:
                db.close()
#db_insert('reg1','2018-12-13',,password)
T_date = datetime.date.today()
for i in ['reg1','reg2','reg3','reg4','reg5']:
    db_insert(i,datetime.date.today(),mails[i],password)
