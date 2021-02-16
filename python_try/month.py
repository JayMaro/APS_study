T = int(input())

for test_case in range(1, T + 1):
    
    month_31 = [1,3,5,7,8,10,12]
    month_30 = [4,6,9,11]

    input_str = input()
    year = input_str[:4]
    month = int(input_str[4:6])
    day = int(input_str[6:])
    
    if not 1<=month<=12:
        print("#{} -1".format(test_case))

        continue
    
    if month in month_31:
        if not 1<=day<=31:
            print("#{} -1".format(test_case))
            continue
    elif month in month_30:
        if not 1<=day<=30:
            print("#{} -1".format(test_case))
            continue
    elif month == 2:
        if not 1<=day<=28:
            print("#{} -1".format(test_case))
            continue


    print("#{}".format(test_case), end = ' ')
    print("{}/{:02}/{:02}".format(year,month,day))