#!/usr/bin/env python

import sys
import re


print('#!/usr/bin/env python')
print('# coding=utf-8')
print('from format import entry,volume,section,count,fourteen,Copyright')
print('')


for line in sys.stdin:
    line = line[:-1]
    if '*' in line:
        l = line.replace('*', "', '")
        print("entry('" + l + "')")
        
    elif line.startswith('類篇卷第'):
        print("volume('%s')" % line)

    elif re.match('^[0-9]', line) is not None:
        print("section('%s')" % line)

    elif re.match('^文', line) is not None:
        print("count('%s')" % line)

    elif re.match('^十四部', line) is not None:
        print("fourteen('%s')" % line)        

    elif line == '二品頂戴布政使銜四川分巡川東兵備道歸安姚覲元重栞' or line == '朝散大夫右諫議大夫權御史中丞充理檢使上護軍河內郡開國侯食邑一千三百戸賜紫金魚袋臣司馬光等奉敕修纂':
        print("Copyright('%s')" % line)
        
    elif re.match('^$', line) is not None:
        print(line)
        
    else:
        print("unknown('%s')" % line)
        
        
