def get_birthdate(pesel):
    year = int(pesel[:2])
    month = int(pesel[2:4])
    if 20 < month < 33:
        month = month-20
        year = '20' + year
    elif 80 < month < 93:
        month = month-80
        year = '18' + year
    else:
        year = '19' + year
    month = str(month)
    if len(month) < 2:
        month = '0' + month
    day = pesel[4:6]
    return str(year), str(month), day

def get_sex(pesel):
    return int(pesel[9])%2

def validate(pesel):
    peselArray = []
    for i in range(0, 10):
        peselArray.append(int(pesel[i]))
    peselArray[0] = (peselArray[0]*1) % 10
    peselArray[4] = (peselArray[4]*1) % 10
    peselArray[8] = (peselArray[8]*1) % 10
    peselArray[1] = (peselArray[1]*3) % 10
    peselArray[5] = (peselArray[5]*3) % 10
    peselArray[9] = (peselArray[9]*3) % 10
    peselArray[2] = (peselArray[2]*7) % 10
    peselArray[6] = (peselArray[6]*7) % 10
    peselArray[3] = (peselArray[3]*9) % 10
    peselArray[7] = (peselArray[7]*9) % 10
    pesel_sum = 0
    for i in range(0, 10):
        pesel_sum = pesel_sum + peselArray[i]
    last = 10 - pesel_sum % 10
    print(f"last: {last}")
    if int(pesel[10]) == last:
        return True
    else:
        return False
