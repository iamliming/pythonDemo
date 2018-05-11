import urllib2
import re

for idx in range(1,100):
    response = urllib2.urlopen("http://wap.cmread.com/rbc/l/n.jsp?ln=26771_425652_82576498_7_GD1&nid=408992008&cm=M8030001&t1=17301&vt=3&nodeName=%E5%A5%B3%E7%94%9F%E7%8B%AC%E5%AE%B6&ftl_linkDesc=%E6%9B%B4%E5%A4%9A%E5%A5%B3%E7%94%9F%E7%8B%AC%E5%AE%B6&dataSrcId=83984219&sqId=GD1&page="+str(idx))
    rspStr = response.read()
    pattern = re.compile('/rbc/(\d*)/index.htm',re.S);
    items = re.findall(pattern,rspStr)
    for item in items:
        print item
