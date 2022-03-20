import math
class tender:
    def __init__(self,cost,period):
        self.cost=int(cost)
        self.period=int(period)
    def ald5ol(self):
        x=0.01
        ald5ol_values=[]
        for i in range(5):
            ald5ol_values.append(int(self.cost*x))
            x+=.005
        return  ald5ol_values
    def alta5ier(self):
        return math.ceil((self.cost*0.10)/(self.period*30) )
    def minumumPayment(self):
        return math.ceil((self.cost*0.60)/self.period)
#-------------------------------------------------------------------------

def merge_two_dicts(x, y):
    z = x.copy()   # start with keys and values of x
    z.update(y)    # modifies z with keys and values of y
    return z

class tamem:
    def __init__(self,year,month):
        self.year=int(year)
        self.month=int(month)
    def diesel(self):
        diesel_2019={2019:{1:560,2:560,3:600,4:610,5:610,6:{"1/6/2019-10/6/2019":610,"11/6/2019-30/6/2019":620},7:590,8:605,9:590,10:605,11:595,12:595}}
        diesel_2020={2020:{1:615,2:605,3:555,4:465,5:395,6:410,7:465,8:465,9:480,10:460,11:460,12:470}}
        diesel_2021={2021:{1:500,2:525,3:555,4:555,5:555,6:580,7:605,8:615,9:605,10:615}}
        z = merge_two_dicts(diesel_2019, diesel_2020)
        z=merge_two_dicts(z, diesel_2021)
        try:
            value=z[self.year][self.month]
            value=[value,'سعر السولار']
        except:
            value=['','القيمة غير موجودة داخل قاعدة البيانات']
        return value
    def bitumen(self):
        butumen_2019={2019:{1:377.40,2:382.53,3:408.53,4:420.6,5:421.46,6:409.15,7:388.17,8:420.86,9:367.18,10:403.47,11:331.8,12:296.37}}
        butumen_2020={2020:{1:308,2:347.44,3:223.36,4:257.59,5:220.15,6:230.76,7:276.02,8:294.11,9:303.72,10:293.77,11:296.18,12:313.21}}
        butumen_2021={2021:{1:329.53,2:349.95,3:373.97,4:390.81,5:381.28,6:384.29,7:406.47,8:411.99,9:405.99}}
        z = merge_two_dicts(butumen_2019, butumen_2020)
        z=  merge_two_dicts(z, butumen_2021)
        try:
            value=z[self.year][self.month]
            value=[value,'سعر الاسفلت السائل']
        except:
            value=['','القيمة غير موجودة داخل قاعدة البيانات']
        return value
    def fuel(self):
        fuel_2019={2019:{1:351.00,2:355.83,3:380.36,4:391.74,5:392.61,6:379.14,7:358.16,8:390.85,9:377.17,10:373.46,11:301.78,12:266.35}}
        fuel_2020={2020:{1:277.99,2:317.43,3:293.35,4:277.57,5:190.49,6:200.74,7:246,8:264.09,9:273.7,10:263.75,11:266.17,12:283.2}}
        fuel_2021={2021:{1:299.51,2:319.93,3:346.96,4:360.79,5:351.26,6:354.28,7:376.45,8:381.98,9:375.96}}
        z = merge_two_dicts(fuel_2019, fuel_2020)
        z=  merge_two_dicts(z, fuel_2021)
        try:
            value=z[self.year][self.month]
            value=[value,'سعر زيت الوقود']
        except:
            value=['','القيمة غير موجودة داخل قاعدة البيانات']
        return value
