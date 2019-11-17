def minute2time(minute):
    return str((int)((minute-minute%60)/60))+":"+str(minute%60)
# print(minute2time(610)) #testcase 입니담