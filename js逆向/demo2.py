# @author lsg
# @date 2022/9/1 0001
# @file demo2.py
import execjs

ctx = execjs.compile('''
  function add(x,y){
  return x + y;
  }
''')

with open('ss1.js',mode='r',encoding='utf-8') as f:
    jsfile = f.read()
print(execjs.compile(jsfile).call('one'))
