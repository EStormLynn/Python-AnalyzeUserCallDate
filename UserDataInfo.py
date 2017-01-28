#coding=utf-8
# 用户通话信息类记录
class UserDataInfo(object):
    def __init__(self):
        self.calling_long = 0   #主叫时长
        self.called_long = 0    #被叫时长
        self.call_long = 0      #总时长

        self.calling_times = 0  #主叫次数
        self.called_times = 0   #被叫次数
        self.call_times = 0     #总次数

        self.time_intervel=[]   #通话时段
        for i in range(0,12):
            self.time_intervel.append(0)

        self.day_intervel=[]    #每日通话次数
        for i in range(0,31):
            self.day_intervel.append(0)

        self.call_freq= None       #通话最频繁

