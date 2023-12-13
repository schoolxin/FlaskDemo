from flask import Flask, render_template, request

app = Flask(__name__, template_folder='template', static_url_path='/', static_folder='resource')


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

if __name__ == '__main__':
    app.run(debug=True, port=8888)
