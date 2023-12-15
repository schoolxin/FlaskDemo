import os

from flask import Flask, render_template, request, redirect, url_for, session, make_response
from controller import demo
app = Flask(__name__, template_folder='template', static_url_path='/', static_folder='resource')
app.config['SECRET_KEY'] = os.urandom(24)  # 24位 生成随机数种子  用于产生sessionID

print(__name__)
# 定义接口地址
@app.route('/')
def index():
    return render_template('index.html')


@app.route('/article')
def read():
    return render_template('article-user.html')


# 定义用户注册
@app.route('/user/reg', methods=['POST'])
def register():
    return render_template('article-user.html')


# 查询参数
@app.route('/test')
def test():
    username = request.args.get('username')
    password = request.args.get('password')
    return '用户名%s,密码为%s' % (username, password)


# 路由参数 int 表示对路由参数的类型限制
@app.route('/article/<int:articleid>')
def article(articleid):
    return '文件ID%s' % (articleid)


# 直接读取post请求中的参数
@app.route('/user/login', methods=['POST'])
def login():
    username = request.form.get('username')
    password = request.form.get('password')
    return '用户名%s,密码为%s' % (username, password)


# 重定向：是http协议本身的功能，重定向302状态码，在响应头里面通过指定location字段来告诉浏览器跳转
@app.route('/red')
def red():
    return redirect(url_for('test'))


# 直接在响应中进行重定向
@app.route('/redjs')
def redjs():
    html = "<script>location.href='/'</script>"
    return html


# session 和 cookie
# 要处理session 则必须为app实例设置SECRET_KEY 配置参数随机生成器(Session ID) 再使用session函数
# 处理Cookie 需要使用response对象往HTTP的响应中写入满足http协议的Cookie

@app.route("/sess")
def sess():
    session['name'] = 'woniuxy'
    session['nickname'] = 'dengqiang'
    return 'done'


@app.route("/sc/read")
def scread():
    # return '你当前的昵称为:%s'%session.get('nickname')
    return '你当前的昵称为:%s' % request.cookies.get('name')


# 利用自定义响应的方式来向浏览器设置cookie
@app.route("/cookie")
def cookie():
    resp = make_response("这是设置cookie的操作")
    resp.set_cookie('name', 'flask', max_age=30)
    resp.set_cookie('passwd', '1234', max_age=30)
    # 无法在同一个接口中既设置cookie 又获取cookie
    return resp



if __name__ == '__main__':
    app.run(debug=True, port=8888)
