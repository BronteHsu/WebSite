from flask import Flask, render_template
from datetime import datetime

webObj=Flask(__name__) # main.py

# 建立route

@webObj.route('/') # 首頁
def frontPage():
    name='bronte'
    time=today()
    return render_template('index.html',**locals())

@webObj.route('/today')
def today():
    return datetime.now().strftime('%Y-%m-%d %H:%M:%S')

webObj.run(debug=True)



