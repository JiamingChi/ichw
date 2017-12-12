
# coding: utf-8

# In[17]:


#!/usr/bin/env python3
"""currency.py:等价交换货币的换算
__author__ = "迟家明"
__pkuid__  = "1700012459"
__email__  = "chijiaming@pku.edu.cn"
"""
def exchange(currency_from, currency_to, amount_from):
    """Returns: amount of currency received in the given exchange.

    In this exchange, the user is changing amount_from money in 
    currency currency_from to the currency currency_to. The value 
    returned represents the amount in currency currency_to.

    The value returned has type float.

    Parameter currency_from: the currency on hand
    Precondition: currency_from is a string for a valid currency code

    Parameter currency_to: the currency to convert to
    Precondition: currency_to is a string for a valid currency code

    Parameter amount_from: amount of currency to convert
    Precondition: amount_from is a float"""
    
    from urllib.request import urlopen
    str_request='http://cs1110.cs.cornell.edu/2016fa/a1server.php?from='+currency_from+'&to='+currency_to+'&amt='+str(amount_from)    
    doc = urlopen(str_request)
    docstr = doc.read()
    doc.close()
    jstr = docstr.decode('ascii')
    kstr=''
    for i in jstr:
        if(i=='"' or i==',' or i==':' or i=='{' or i=="}"):
            i=''
        kstr+=i
    klist=kstr.split(' ')
    js=0
    judge_error=False
    for j in klist:
        if(klist[js]=='from'):
            if(klist[js+2]==''):
                judge_error=True
                break
            else:
                from_money=float(klist[js+2])   
        if(klist[js]=='to'):
            if(judge_error==False):
                to_money=float(klist[js+2])  
        js=js+1   
    if(judge_error==False):
        if(from_money==0):
            return 0
        else:
            amount_to=amount_from*to_money/from_money
        return amount_to
    else:
        return "Source currency code is invalid."
    
def test1():
    assert(exchange('UUG','AUC',0.1) == "Source currency code is invalid.")
def test2():
    assert(exchange('USD','AFN',8) == 547.148)
def test3():
    assert(exchange('CNY','CCC',12) == "Source currency code is invalid.")
def test4():
    assert(exchange('CNY','USD',0) == 0)
def test5():
    assert(exchange('MVR','MOP',9.0) == 4.7085884869247)
def test6():
    assert(exchange('USD','GBP',55) == 42.146885)
def test7():
    assert(exchange('UUA','GBP',0) == "Source currency code is invalid.")
def test8():
    assert(exchange('STD','USD',21893.55*100) == 106.45754759)
    
def testAll():
    """test all cases"""
    test1()
    test2()
    test3()
    test4()
    test5()
    test6()
    test7()
    test8()
    print("All tests passed") 
    raw_input() 

def main():
    """main module
    """
    testAll()   
    
    
    
if __name__ == '__main__':
    main()
    

    

