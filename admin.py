from flask import Blueprint, render_template, request, redirect, url_for, flash, session
from werkzeug.utils import secure_filename
from model import db, Content
import os

# 声明 Flask的蓝图 给app.py引入使用, 设置路由前缀为 '/admin'
admin_bp = Blueprint('admin', __name__, url_prefix='/admin')

UPLOAD_FOLDER = 'static/uploads'
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif'}

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

# 管理路由
@admin_bp.route('/')
def admin():
    if not session.get('logged_in'):
        flash('请先登录！', 'warning')
        return redirect(url_for('login'))

    items = Content.query.all()
    return render_template('admin.html', items=items)

# http://127.0.0.1:5000/admin/post 和 http://127.0.0.1:5000/admin/post/ 是两个东西. 后者报NotFound

# 发布文章路由
@admin_bp.route('/post', methods=['GET', 'POST'])
def post():
    if not session.get('logged_in'):
        flash('请先登录！', 'warning')
        return redirect(url_for('index'))

    if request.method == 'POST':
        title = request.form['title']
        content = request.form['content']
        # image = request.files['image']
        images = request.files.getlist('images')

        # 处理上传图片
        # image_path = None
        image_paths = []
        for image in images:
            if image and allowed_file(image.filename):
                filename = secure_filename(image.filename)
                image_path = os.path.join(UPLOAD_FOLDER, filename)
                image_paths.append(image_path)
                image.save(image_path)

        images_string = ','.join(image_paths)

        # 保存文章到数据库(必须和数据库字段名保持一致, 否则报错: 'TypeError: 'image_path' is an invalid keyword argument for Content')
        new_content = Content(title=title, content=content, images=images_string)
        db.session.add(new_content)
        db.session.commit()

        flash('文章发布成功！', 'success')
        return redirect(url_for('admin.admin'))

    return render_template('post.html')

# 编辑文章路由
@admin_bp.route('/edit', methods=['GET', 'POST'])
def edit():
    if not session.get('logged_in'):
        flash('请先登录！', 'warning')
        return redirect(url_for('index'))
    
    content_id = request.args.get('e', '')
    article = Content.query.filter_by(id=content_id).first()

    if article is None:
        return "请求的文章不存在", 404
    if request.method == 'POST':
        article.title = request.form['title']
        article.content = request.form['content']
        db.session.commit()
        flash('文章已成功更新！', 'success')
        return redirect(url_for('articles', content_id=content_id))  # 重定向到查看文章的页面
    return render_template('edit.html', article=article)

# 删除文章路由
@admin_bp.route('/delete/<int:content_id>')
def delete(content_id):
    if not session.get('logged_in'):
        flash('请先登录！', 'warning')
        return redirect(url_for('index'))

    content = Content.query.get(content_id)
    if content:
        db.session.delete(content)
        db.session.commit()
        flash('文章已删除！', 'success')
    else:
        flash('文章不存在！', 'danger')

    return redirect(url_for('admin.admin'))