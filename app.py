import email

from flask import Flask,render_template
from datetime import datetime
app = Flask(__name__)

class User:
    def __init__(self,username,email):
        self.username = username
        self.email = email

def datetime_formate(value,formate='%Y年 %m月 %d日 %H:%M:%S'):
    return value.strftime(formate)
app.add_template_filter(datetime_formate,'format')

@app.route('/')
def hello_world():# put application's code here
    user= User(username='知了',email='@gmail.com')
    person = {
        'username':'张三',
        'email':'zhangsan@gmail.com'
    }
    return render_template('index.html',user=user,person=person)

@app.route('/blog/<blog_id>')
def blog(blog_id):
    return render_template('blog_detail.html',blog_id=blog_id,username="知了")

@app.route('/filter')
def filter_demo():
    user = User(username='知了', email='@gmail.com')
    time=datetime.now()
    return render_template('filter.html',user=user,time=time)

@app.route('/control')
def control_statement():
    age = 18
    books=[{
        'name':'《三国演义》',
        'author':'罗贯中'
    },{
        'name':'《西游记》',
        'author':'吴承恩'
    },{
        'name':'《红楼梦》',
        'author':'曹雪芹'
    },{
        'name':'《水浒传》',
        'author':'施耐庵'
    }]
    return render_template('control.html',age=age,books=books)

if __name__ == '__main__':
    app.run()
