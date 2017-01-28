#coding=utf-8
import xlrd
import matplotlib.pyplot as plt
import UserDataInfo

def readData(url):
    data=xlrd.open_workbook(url)
    table=data.sheets()[0]  #多张sheet的情况读取第一张
    nrows=table.nrows
    ncols=table.ncols
    list=[]
    for rownum in range(0,nrows):
        row=table.row_values(rownum)
        for i in range(0,ncols):        #转码unicode转utf-8
            row[i]=row[i].encode('utf-8')
        if row:
            list.append(row)
    return list

#行为分析
def behavior_analysis(datalist):
    t=1
    for line in datalist:
        if(t==1):
            t=3
            continue
        dh=dateDecode(line[2])
        day=int(dh[0])
        hour=int(dh[-1])

        user.day_intervel[day]+=1
        user.time_intervel[hour/2]+=1


        timeStr=line[3]
        timelong = timeDecode(timeStr)

        if line[4]=='主叫':
            user.calling_times+=1
            user.calling_long+=timelong
        if line[4]=='被叫':
            user.called_times+=1
            user.called_long+=timelong


    user.call_times=user.calling_times+user.called_times    #总次数
    user.call_long=user.calling_long+user.called_long       #总时长

#解码时间
def timeDecode(timeStr):
    hour = min = sec = 0
    if timeStr.find('小时') != -1:
        hour = timeStr.split('小时')[0]
        timeStr = timeStr.split('小时')[1]
    if timeStr.find('分') != -1:
        min = timeStr.split('分')[0]
        timeStr = timeStr.split('分')[1]
    if timeStr.find('秒') != -1:
        sec = timeStr.split('秒')[0]

    timelong = int(sec) + int(min) * 60 + int(hour) * 60 * 60
    return timelong

#编码时间
def timeEncode(time):
    strtime=str(time%60)+"秒"
    time/=60
    if(time!=0):
        strtime=str(time%60)+"分"+strtime
        time/=60
        if (time != 0):
            strtime = str(time % 60) + "小时"+strtime
    return strtime

#解码日期
def dateDecode(dateStr):
    dateStrlist=dateStr.split(' ')
    dayStr=dateStrlist[0]
    dayStrlist=dayStr.split('-')
    day=dayStrlist[-1]

    timeStr=dateStrlist[-1]
    timeStrlist=timeStr.split(':')
    timeHour=timeStrlist[0]

    dayAndHour=[]
    dayAndHour.append(day)
    dayAndHour.append(timeHour)
    return dayAndHour


def printout():
    print "被叫次数：", user.called_times
    print "被叫时长：", timeEncode(user.called_long)

    print "主叫次数：", user.calling_times
    print "主叫时长：", timeEncode(user.calling_long)

    print "总次数：",user.call_times
    print "总时长：",timeEncode(user.call_long)

    print "日期",user.day_intervel
    print "时段",user.time_intervel

#数据可视化
def dataVisualization(userinfo):
    plt.plot(userinfo.day_intervel, 'k')
    plt.plot(userinfo.day_intervel, 'bo')
    plt.xlabel(u'日          期')
    plt.ylabel(u'通话次数')
    plt.title(u'每日通话分析')
    plt.grid(color='#95a5a6', linestyle='--', linewidth=1, axis='y', alpha=0.4)
    plt.show()

url="/Users/SeeKHit/Downloads/2017年01月语音通信.xls"
datalist=readData(url)

user=UserDataInfo.UserDataInfo()
behavior_analysis(datalist)

printout()
dataVisualization(user)





