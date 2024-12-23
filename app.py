from flask import Flask, render_template, request, redirect, url_for, session, flash
from werkzeug.security import check_password_hash
from model import User, Content, init_db, or_
from admin import admin_bp                  # 引入admin.py这个蓝图Python文件

app = Flask(__name__)
app.secret_key = 'ASD9980'
admin = 'admin'

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# 注册蓝图
app.register_blueprint(admin_bp, url_prefix=f'/{admin}')

# 初始化数据库
init_db(app)

# 首页路由
# jinja2标签内用{{}}, 嵌入Python代码用{%%}
@app.route('/')
def index():
    items = Content.query.all()
    return render_template('index.html', items=items)

@app.route('/article/<int:content_id>')
def articles(content_id):
    article = Content.query.filter_by(id=content_id).first()
    posttime = str(article.posttime).split('.')[0].split(' ')
    # posttime [0]为年月日，[1]为具体时间
    if not article:
        return "请求的文章为空!!"
    else:
        return render_template('articles.html', article=article, posttime=posttime)
    
# HTML 内Form的name属性将提交到后端去。id仅只作该页标识符。

# # 搜索路由  POST
# # 如若不添加GET和POST双支持, 则默认支持GET. 导致的直接问题就是405, 拒绝你对此路由的POST访问, 则无法通过Form表单提交内容查询数据
# @app.route('/search', methods=['GET', 'POST'])
# def search():
#     if request.method == 'POST':
#         search_data = request.form['search']
#         # %search_data%: 表示包含 search_data 的所有记录, 如若不带, 则为精准匹配, %相当于正则表达式的* 。
#         search_fetch = Content.query.filter(
#         or_(
#             Content.title.like(f'%{search_data}%'),
#             Content.content.like(f'%{search_data}%')
#             )
#         ).all()
#         if not search_fetch:
#             return "搜的什么玩意这是!(红温)"
#         else:
#             return render_template('search.html', results=search_fetch)
        
#     return render_template('search.html')

# 搜索路由  GET
@app.route('/search')
def search():
    keyword = request.args.get('q', '')
    # %keyword%: 表示包含 keyword 的所有记录, 如若不带, 则为精准匹配, %相当于正则表达式的* 。
    search_fetch = Content.query.filter(
        or_(
            Content.title.like(f'%{keyword}%'),
            Content.content.like(f'%{keyword}%')
        )
    ).all()
    if not search_fetch :
        return "搜的什么玩意这是!(红温)"
    else:
        return render_template('search.html', results=search_fetch)

# 登录路由
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        user = User.query.filter_by(username=username).first()
        if user and check_password_hash(user.password, password):
            session['logged_in'] = True
            session['username'] = username
            flash('登录成功！', 'success')
            return redirect(url_for('admin.admin'))
        else:
            flash('用户名或密码错误！', 'danger')

    return render_template('login.html')

# 退出登录路由
@app.route('/logout')
def logout():
    session.clear()
    flash('您已退出登录！', 'info')
    return redirect(url_for('login'))

# 程序入口
if __name__ == '__main__':
    app.run(debug=True)