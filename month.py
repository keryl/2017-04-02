def is_month(month):

    # first check given month is string
    if type(month) != str:
        return "argument should be of type string"

    months = ['jan', 'feb', 'mar', 'apr', 'may', 'jun', 'jul', 'aug', 'sep', 'oct', 'nov', 'dec']

    # return True if given month is in months list
    if month in months:
        return True

    # else return false
    else:
        return False

if __name__=="__main__":
    jan_is_month = is_month("jan")
    print ("jan is a month: " + jan_is_month)