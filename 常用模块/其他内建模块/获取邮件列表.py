import imaplib,datetime,pymysql
class mail_163:
    def __init__(self,accout):
        self.account = accout


def mailcount(num):
    """获取邮箱的当天的发件数量"""
    with imaplib.IMAP4_SSL('imaphm.qiye.163.com',993) as m:
        mailaccount = ("reg.server-00%s@mexmarkets.com" % num)
        m.login(mailaccount,'19861119Kk' )
        m.select('Sent')
        # 获取当天日期并转换为邮件日期格式
        C_date = datetime.datetime.strftime(datetime.date.today(),'%d-%B-%Y')
        type,data = m.search(None,'(SENTON %s)' % C_date)
        a = data[0].decode('utf-8')
        return len(a.split(" "))
#print(mailcount('1'))
DB_name = 'countmail'
DB_host = '39.105.13.50'
DB_pass = '20140916'
DB_user = 'root'
mail_server = 'smtphm.qiye.163.com'
mail_user = 'reg.server-005@mexmarkets.com'
mail_pass = '19861119Kk'
mail_port = 994
mail_protocol = 'ssl'
def update_mail():
    db = pymysql.connect(DB_host, DB_user, DB_pass, DB_name)
    cursor = db.cursor()
    try:
        cursor.execute("update mails set server='%s',user='%s',pass='%s',port=%d,sec_protocol='%s'" % (mail_server,mail_user,mail_pass,mail_port,mail_protocol))
        db.commit()
    except:
        db.rollback()
    finally:
        db.close()
update_mail()
def get_cu_mail(arg):
    dab = pymysql.connect(DB_host, DB_user, DB_pass, DB_name)
    cur =dab.cursor()
    cur.execute("select %s from mails" % arg)
    result = cur.fetchone()
    dab.close()
    return  result
get_cu_mail('user')
