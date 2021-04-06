# @Time    : 2020/10/28 19:42
# @Author  : Nadine
# @Software: PyCharm
from tkinter import *
from tkinter import messagebox
from tkinter.messagebox import *
import cx_Oracle as cx
from PIL import ImageTk, Image
import requests
from bs4 import BeautifulSoup
import re
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib


class LoginPage(Frame):
    def __init__(self):
        super().__init__()
        self.username = StringVar()
        self.password = StringVar()
        self.pack()
        self.createForm()

    def createForm(self):
        Label(self).grid(row=0, stick=W, pady=10)
        Label(self, text='账户: ').grid(row=1, stick=W, pady=10)
        Entry(self, textvariable=self.username).grid(row=1, column=1, stick=E)
        Label(self, text='密码: ').grid(row=2, stick=W, pady=10)
        Entry(self, textvariable=self.password, show='*').grid(row=2, column=1, stick=E)
        Button(self, text='登陆', command=self.loginCheck).grid(row=3, stick=W, pady=10)
        Button(self, text='退出', command=self.quit).grid(row=3, column=1, stick=E)

    def loginCheck(self):
        name = self.username.get()
        secret = self.password.get()
        if name == 'zjf' and secret == '123':
            self.destroy()
            self.quit()
            # MainPage()
        else:
            showinfo(title='错误', message='账号或密码错误！')
            # print('账号或密码错误！')


def image():
    IMAGE_PATH = '123.jpg'
    WIDTH, HEIGTH = 500, 500
    root.geometry('{}x{}'.format(WIDTH, HEIGTH))
    canvas = Canvas(root)
    canvas.pack(fill=BOTH)
    img = ImageTk.PhotoImage(Image.open(IMAGE_PATH), Image.ANTIALIAS)
    canvas.background = img  # Keep a reference in case this code is put in a function.
    bg = canvas.create_image(0, 0, anchor=NW, image=img)


root = Tk()
root.title('银行个人理财系统')
width = 500
height = 500
screenwidth = root.winfo_screenwidth()
screenheight = root.winfo_screenheight()
alignstr = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
root.geometry(alignstr)  # 居中对齐
image()
page1 = LoginPage()
root.mainloop()

window = Tk()
window.configure()


def leftQuery():
    global queryEntry
    queryLable = Label(text="数据库表", justify="center")
    queryLable.pack()
    queryEntry = Entry(justify="center")
    queryEntry.pack()
    queryButton = Button(text="查询", justify="center", command=sqlQuery)
    queryButton.pack()


def sqlQuery():
    global queryEntry
    global queryText
    queryText.delete('1.0', END)
    print(queryEntry.get())
    conn = cx.connect('zjf/zjf@127.0.0.1:49161/XE')
    cursor = conn.cursor()
    sql = "select * from " + queryEntry.get()
    print(sql)
    cursor.execute(sql)
    alldata = cursor.fetchall()
    for i in alldata:
        print(i)
        queryText.insert(INSERT, i)
        queryText.insert(INSERT, '\n')
    # messagebox.showerror(title='error', message='数据库查询出错')
    cursor.close()
    conn.close()


def textQuery():
    global queryText
    queryText = Text(height=10)
    queryText.tag_configure("center", justify='center')
    queryText.pack()


def saveMenu():
    menubar = Menu(root)
    filemanu = Menu(menubar, tearoff=0)
    filemanu.add_command(label='New')
    menubar.add_cascade(label='File', menu=filemanu)


def saveButton():
    Button(window, text='存钱', command=saveMoney).pack(side=BOTTOM)


def takeButton():
    Button(window, text='取钱', command=takeMoney).pack(side=BOTTOM)


def productButton():
    Button(window, text='理财产品', command=showProduct).pack(side=BOTTOM)


def stockButton():
    Button(window, text='股票列表', command=showStock).pack(side=BOTTOM)


def fundButton():
    Button(window, text='基金列表', command=showFund).pack(side=BOTTOM)


def bondButton():
    Button(window, text='债券列表', command=showBond).pack(side=BOTTOM)


def personButton():
    Button(window, text='个人信息', command=showPerson).pack(side=BOTTOM)


def weatherButton():
    Button(window, text='武汉天气', command=showWeather).pack(side=BOTTOM)


def fundGraphButton():
    Button(window, text='基金历史走势图', command=inputFund).pack(side=BOTTOM)


def addCusButton():
    Button(window, text='添加客户', command=addCustomer).pack(side=BOTTOM)


def saveMoney():
    save = Tk()
    text = StringVar()
    Label(save, text="账户号").pack()
    Entry(save, textvariable=text).pack()
    Label(save, text="存款数额").pack()
    Entry(save, textvariable=text).pack()
    Label(save, text="产品类型").pack()
    Entry(save, textvariable=text).pack()
    Button(save, text="确认").pack()
    save.mainloop()


def takeMoney():
    global take
    take = Tk()
    Label(take, text="账户号").pack()
    Entry(take).pack()
    Label(take, text="取款数额").pack()
    Entry(take).pack()
    Button(take, text="确认", command=takeMoneyQuery).pack()
    take.mainloop()


def takeMoneyQuery():
    global take
    pass
    '''
    conn = cx.connect('zjf/zjf@127.0.0.1:49161/XE')
    cursor = conn.cursor()
    sql = "select currentbalance from  account where accountnumber=1000"
    cursor.execute(sql)
    money = cursor.fetchall()
    print(money)
    Label(take, text="当前余额:").pack()
    Label(take, text=money).pack()
    '''


def showProduct():
    show = Tk()
    Label(show, text="代销季添利平衡一号 代码：107331A(代销) 产品到期日：2030-11-11（期限：3652天）").pack()
    Label(show, text="点金系列进取型三个月 产品代码：PS0006 产品到期日：2021-02-08（期限：94天）").pack()
    Label(show, text="点金系列进取型一个月 产品代码：PS0005 产品到期日：2020-12-07（期限：31天）").pack()
    Label(show, text="中证500指数看涨 产品代码：PE0047 产品到期日：2021-04-06（期限：151天）").pack()
    Label(show, text="沪深300指数看跌 产品代码：PA0051 产品到期日：2021-11-05（期限：364天）").pack()
    Label(show, text="中证500指数看涨 产品代码：PA0050 产品到期日：2021-11-05（期限：364天）").pack()
    Label(show, text="代销量化十五月一号 代码：100710 产品到期日：2030-11-06（期限：3652天）").pack()
    show.mainloop()


def showStock():
    show = Tk()
    Label(show, justify="center", text="股票代码	股票简称	公司名称	股票简称拼音").pack()
    Label(show, justify="center", text="000001	平安银行	平安银行股份有限公司	PAYH").pack()
    Label(show, justify="center", text="000002	万科A	万科企业股份有限公司	WKA").pack()
    Label(show, justify="center", text="000004	国农科技	深圳中国农大科技股份有限公司 GNKJ").pack()
    Label(show, justify="center", text="000005	世纪星源	深圳世纪星源股份有限公司	SJXY").pack()
    Label(show, justify="center", text="000006	深振业Ａ	深圳市振业(集团)股份有限公司	SZYA").pack()
    Label(show, justify="center", text="000007	全新好	深圳市全新好股份有限公司	QXH").pack()
    show.mainloop()


def showFund():
    show = Tk()
    Label(show, justify="center",
          text="序号	基金 代码	基金简称	日期	单位净值	累计净值	日增长率	近1周	近1月	近3月	近6月	近1年	近2年	近3年	今年来	成立来	自定义 手续费").pack()
    Label(show, justify="center",
          text="1	009321	中信保诚中债	10-30	1.1329	1.1329	0.03%	9.69%	13.31%	13.32%	---	---	---	---	---	13.29%	13.29%	0.00%	").pack()
    Label(show, justify="center",
          text="2	009320	中信保诚中债	10-30	1.1346	1.1346	0.03%	9.62%	13.24%	13.47%	---	---	---	---	---	13.46%	13.46%	0.06%").pack()
    Label(show, justify="center",
          text="3	001245	工银生态环境	10-30	1.4080	1.4080	1.15%	8.56%	8.14%	12.19%	61.84%	87.48%	157.40%	65.65%	75.12%	40.80%	85.26%	0.15%").pack()
    Label(show, justify="center",
          text="4	001156	申万菱信新能	10-30	1.9070	1.9070	0.95%	8.48%	11.13%	12.57%	61.34%	109.33%	161.95%	77.40%	66.84%	90.70%	110.02%	0.15%").pack()
    Label(show, justify="center",
          text="5	000496	长安产业精选	10-30	1.2909	1.5309	0.81%	8.35%	7.86%	4.72%	4.16%	3.25%	27.16%	9.65%	-3.14%	61.09%	2.28%	0.15%").pack()
    Label(show, justify="center",
          text="6	002071	长安产业精选	10-30	1.2648	1.3148	0.81%	8.34%	7.82%	4.59%	3.89%	2.75%	25.49%	7.49%	-3.55%	27.92%	1.79%	0.00%").pack()
    show.mainloop()


def showBond():
    show = Tk()
    Label(show, justify="center", text="序号	代码	名称	价格	涨跌幅 今最高	今最低 成交量(手) 成交额(元) 到期日").pack()
    Label(show, justify="center",
          text="1	010512	05国债12	100.69	0.39	0.39%	101.00	100.69	0.16	1.61万	2020-11-15").pack()
    Label(show, justify="center",
          text="2	019633	20附息国债07	94.91	0.25	0.26%	94.91	94.83	2.52	23.91万	2070-05-25").pack()
    Label(show, justify="center",
          text="3	101619	16附息国债19	92.17	0.16	0.17%	92.18	91.91	1.3	1.20万	2046-08-22").pack()
    Label(show, justify="center",
          text="4	019547	16附息国债19	92.09	0.10	0.11%	92.17	91.98	469.28	4319.83万	2046-08-22").pack()
    Label(show, justify="center",
          text="5	019536	16附息国债08	95.83	0.10	0.10%	95.86	95.65	106.03	1015.74万	2046-04-25").pack()
    Label(show, justify="center",
          text="6	019631	20附息国债05	95.53	0.06	0.06%	95.53	95.50	0.13	1.24万	2025-04-09").pack()
    Label(show, justify="center",
          text="7	101613	16附息国债13	99.05	0.05	0.05%	99.10	99.05	3.4	3.37万	2066-05-23").pack()
    show.mainloop()


def showPerson():
    global show
    global person
    show = Tk()
    Label(show, justify="center", text="请输入账户号").pack()
    person = Entry(show)
    person.pack()
    Button(show, text="确认", command=personQuery).pack()


def personQuery():
    global show
    global person
    profile = person.get()
    conn = cx.connect('zjf/zjf@127.0.0.1:49161/XE')
    cursor = conn.cursor()
    sql = "select * from  account where accountnumber=" + profile
    cursor.execute(sql)
    money = cursor.fetchall()
    print(money)
    Label(show, text="账户号 当前余额 开户日期 当前利率 产品编号 当前状态").pack()
    Label(show, text=money).pack()


def showWeather():
    show = Tk()
    r = requests.get('http://www.weather.com.cn/data/sk/101200101.html')
    r.encoding = 'utf-8'
    Label(show, text="城市 风向 温度").pack()
    Label(show, text=r.json()['weatherinfo']['city']).pack(side=LEFT)
    Label(show, text=r.json()['weatherinfo']['WD']).pack(side=LEFT)
    Label(show, text=r.json()['weatherinfo']['temp']).pack(side=LEFT)
    show.mainloop()


def inputFund():
    global code, begin, end
    show = Tk()
    Label(show, text="基金代号").pack()
    code = Entry(show)
    code.pack()
    Label(show, text="开始日期").pack()
    begin = Entry(show)
    begin.pack()
    Label(show, text="结束日期").pack()
    end = Entry(show)
    end.pack()
    Button(show, text="确认", command=showFundGraph).pack()


def showFundGraph():
    global code, begin, end
    # code.get()
    # begin.get()
    # end.get()
    # '050026' '2020-02-01' '2020-06-01'
    fund_df = get_fund(code.get(), start_date=begin.get(), end_date=end.get())
    print(fund_df)
    fig, axes = plt.subplots(nrows=2, ncols=1)
    fund_df[['单位净值', '累计净值']].plot(ax=axes[0])
    fund_df['日增长率'].plot(ax=axes[1])
    plt.show()


matplotlib.rcParams['font.sans-serif'] = ['SimHei']
matplotlib.rcParams['font.family'] = 'sans-serif'
matplotlib.rcParams['axes.unicode_minus'] = False


def get_html(code, start_date, end_date, page=1, per=20):
    url = 'http://fund.eastmoney.com/f10/F10DataApi.aspx?type=lsjz&code={0}&page={1}&sdate={2}&edate={3}&per={4}'.format(
        code, page, start_date, end_date, per)
    rsp = requests.get(url)
    html = rsp.text
    return html


def get_fund(code, start_date, end_date, page=1, per=20):
    # 获取html
    html = get_html(code, start_date, end_date, page, per)
    soup = BeautifulSoup(html, 'html.parser')
    # 获取总页数
    pattern = re.compile('pages:(.*),')
    result = re.search(pattern, html).group(1)
    total_page = int(result)
    # 获取表头信息
    heads = []
    for head in soup.findAll("th"):
        heads.append(head.contents[0])

    # 数据存取列表
    records = []
    # 获取每一页的数据
    current_page = 1
    while current_page <= total_page:
        html = get_html(code, start_date, end_date, current_page, per)
        soup = BeautifulSoup(html, 'html.parser')
        # 获取数据
        for row in soup.findAll("tbody")[0].findAll("tr"):
            row_records = []
            for record in row.findAll('td'):
                val = record.contents
                # 处理空值
                if val == []:
                    row_records.append(np.nan)
                else:
                    row_records.append(val[0])
            # 记录数据
            records.append(row_records)
        # 下一页
        current_page = current_page + 1

    # 将数据转换为Dataframe对象
    np_records = np.array(records)
    fund_df = pd.DataFrame()
    for col, col_name in enumerate(heads):
        fund_df[col_name] = np_records[:, col]

    # 按照日期排序
    fund_df['净值日期'] = pd.to_datetime(fund_df['净值日期'], format='%Y/%m/%d')
    fund_df = fund_df.sort_values(by='净值日期', axis=0, ascending=True).reset_index(drop=True)
    fund_df = fund_df.set_index('净值日期')

    # 数据类型处理
    fund_df['单位净值'] = fund_df['单位净值'].astype(float)
    fund_df['累计净值'] = fund_df['累计净值'].astype(float)
    fund_df['日增长率'] = fund_df['日增长率'].str.strip('%').astype(float)
    return fund_df


def addCustomer():
    global num, pas, bal, proid
    add = Tk()
    Label(add, text="账户号").pack()
    num = Entry(add)
    num.pack()
    Label(add, text="密码").pack()
    pas = Entry(add)
    pas.pack()
    Label(add, text="存款数额").pack()
    bal = Entry(add)
    bal.pack()
    Label(add, text="理财产品编号").pack()
    proid = Entry(add)
    proid.pack()
    Button(add, text="确认", command=addCustomerSql).pack()
    add.mainloop()


def addCustomerSql():
    global num, pas, bal, proid
    conn = cx.connect('zjf/zjf@127.0.0.1:49161/XE')
    cursor = conn.cursor()
    sql = "insert into Account values(" + num.get() + "," + bal.get() + ",sysdate," + "3.22," + proid.get() + ",'active')";
    cursor.execute(sql)
    messagebox.showinfo('提示', '添加成功')

oracleLable = Label(text="银行个人理财系统")
oracleLable.pack()

def oracleInit():
    leftQuery()
    textQuery()
    saveMenu()
    saveButton()
    takeButton()
    productButton()
    stockButton()
    fundButton()
    bondButton()
    personButton()
    weatherButton()
    fundGraphButton()
    addCusButton()

oracleInit()
window.mainloop()
