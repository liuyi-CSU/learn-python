#！/usr/bin/env python
#-*-coding:utf-8-*-

#字典浅复制
x = {'user': 'admin', 'machines': ['foo', 'bar', 'baz']}
y = x.copy()
y['user'] = 'mlh'
y['machines'].remove('bar')
print('keys方法：', x.keys())
#print('iterkeys:', x.iterkeys) #iterkeys不能直接print
for i in iter(x.keys()):
    print('%s:%s', (i, x[i]))
#print(y)
#print(x)    #改变y时，x也会改变

#字典深复制
from copy import deepcopy
d = {}
d['name'] = ['Alfred', 'Bertrand']
c = d.copy()
dc = deepcopy(d)
d['name'].append('Clive')
print('c:', c, 'dc:', dc)

