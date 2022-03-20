def dateDifference(dateStart):
    print(dateStart)
    year=int(dateStart.split("-")[0])
    month=int(dateStart.split("-")[1])
    day=int(dateStart.split("-")[2])
    date_list=[year,month,day]

    return date_list

def dateText(delta,tenderPeriod,periodSemster=0,periodOther=0):
    actualPeriod=delta.days
    delays=actualPeriod-int(tenderPeriod)-int(periodSemster)-int(periodOther)
    if delays>=1 and delays<=10:
        yum="ايام"
    else:
        yum="يوماً"
    import num2words
    from num2words import num2words
    if delays<=0:
        explanation="لا يوجد ايام تاخير"
        delays_2=''
        value={1:explanation,2:delays_2}
    else:
        line1="مدة التفيذ الفعلية للمشروع ({one})".format(one=actualPeriod)
        line2="-" + '\n' + "مدة العطاء ({two})".format(two=tenderPeriod)
        line3="-" + '\n'+"(تمديدات اخرى ({three}) + تمديد الصيف والشتاء ({four}) )".format(three=periodOther,four=periodSemster)
        #line4=" =   ({five})".format(five=delays)
        explanation=line1+line2+line3
        delays_2=num2words( delays, lang='ar') + ' ' +yum +" "  + "( "+ str(delays)+ " )"
        value={1:explanation,2:delays_2}




    return value
