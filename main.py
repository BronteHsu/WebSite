from flask import Flask
from datetime import datetime

webObj=Flask(__name__) # main.py

# 建立route

# 首頁
@webObj.route('/')
def frontPage():
    return 'Hello!'

@webObj.route('/today')
def today():
    return datetime.now().strftime('%Y-%m-%d %H:%M:%S')

webObj.run(debug=True)
