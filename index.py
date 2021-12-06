def epostalcode(codeposti):
    if (len(codeposti) != 10):
        return "tool code posti dorost nis"
    if (codeposti[4]== 5):
        return "raqam 5 nemytavanad adad 5 bashad"
    if (codeposti[:4]==(codeposti[0]+codeposti[0]+codeposti[0]+codeposti[0])):
        return "code posti eshtebah ast"
    if( codeposti == (codeposti[0]+codeposti[0]+codeposti[0]+codeposti[0]+codeposti[0]+codeposti[0]+codeposti[0]+codeposti[0]+codeposti[0]+codeposti[0])):
        return "code posti eshtebah ast"
    for i in range(len(codeposti)):
        if(codeposti[i] == "2" or codeposti[i]== "0"):
            return "adad 0 ya 2 mojaz nis"

    return "code posti sahih ast"

codeposti = input ("enter postal code:")
print ( epostalcode(codeposti))
    


# https://t.me/DeAref
