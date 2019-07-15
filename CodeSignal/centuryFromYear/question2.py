def centuryFromYear(year):
    if(year>=1 and year<=2005):
        if str(year)[2:4] == "00":
            century = int(str(year)[:2])
        else:
            century = int(str(year)[:2]) +1
        return century
print(centuryFromYear(2001))