
# coding: utf-8

# In[25]:


#!/usr/bin/env python3

"""wcount.py: count words from an Internet file.

__author__ = "迟家明"
__pkuid__  = "1700012459"
__email__  = "chijiaming@pku.edu.cn"
"""

import sys
from urllib.request import urlopen


def wcount(lines, topn=10):
    """count words from lines of text string, then sort by their counts
    in reverse order, output the topn (word count), each in one line. 
    """
    sys.argv[1:]=urlopen(sys.argv[1])
    wl=sys.argv[1:]
    wlst0=[]
    for aline in wl:
        wlst0+=aline.split()
    wlst=list(set(wlst0))
    tlst=[]
    mlst=[]
    nlst=[]
    mydic={}
    for word in wlst:
        mlst+=[word]
        js=0
        for aword in wlst0:
            if word==aword:
                js+=1
        tlst.append(js)
        nlst+=[js]
        mydic[js]=word
    klst=sorted(mydic,reverse=True)      
    t=0
    for i in klst:
        mstr=str(mydic[i]).replace('b',"").replace("'",'')
        print(mstr,'    ',i)
        t+=1
        if t>=topn:
            break

if __name__ == '__main__':

    if  len(sys.argv) == 1:
        print('Usage: {} url [topn]'.format(sys.argv[0]))
        print('  url: URL of the txt file to analyze ')
        print('  topn: how many (words count) to output. If not given, will output top 10 words')
        sys.exit(1)

    try:
        topn = 10
        if len(sys.argv) == 3:
            topn = int(sys.argv[2])
    except ValueError:
        print('{} is not a valid topn int number'.format(sys.argv[2]))
        sys.exit(1)

    try:
        with urlopen(sys.argv[1]) as f:
            contents = f.read()
            lines   = contents.decode()
            wcount(lines, topn)
    except Exception as err:
        print(err)
        sys.exit(1)


# In[31]:


pass


# In[30]:


pass


# In[32]:


pass

