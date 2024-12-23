# Easy-Blog v1.1
超简单博客方案 ｜ 使用 Flask、SQLite 和 (Jinja2)Bootstrap

## 这是什么
这是一个由Flask(后端和Jinja2模板引擎)+SQLite实现的超简单博客方案，只算代码，估计甚至没有200kb。

事实上，我正在使用Express+React等现代组合编写一些内容，没想到我的第一个博客引擎发布会是Flask+Jinja2，因为作业。(可能不会有更新)

我曾经写过PHP，我不否认PHP实在好，但是它的函数实在多得糟糕，并且安装极其繁琐，在我入门Linux时，PHP简直是我的噩梦。

而这次带来的**Flask(Jinja2)+SQLite数据库(使用ORM模型操作)博客程序**是为了完成我的Python大作业。(我不是这个专业的，别喷TvT)

## 可以学到什么
虽然我几乎没有花什么时间就完成了这个作业(因为是作业，**我写了很多笔记，包括HTML的易错点**(我经常记混，因为我学了很多乱七八糟的东西), **如果你打算学习Flask和网页开发，我认为这个项目应该可以帮到你**)，但是令我感到痛苦的就是，Jinja2的写法，大量使用{{}}，并且我的编辑器没有Jinja2的语法联想，我写了很多繁琐的，易错的HTML。于是我一直在完善，写笔记。

在作业要求下，我使用了Bootstrap5 CSS框架(离线引入)。Bootstrap5的官网我认为很糟糕，起码对我而言是，我查询了海量的文档，想知道这个类到底对应了什么，最终还是妥协，把大部分布局留给了Ai做。

---

### 还没有写完编辑文章的图片删除和更改路由，以及管理员改密码路由，账号密码具体看项目指引【4】

---

## 项目指引

1.第一次运行：`pip3 install -r requirements.txt` 安装所需的库

2.关于数据库：instance文件夹存放了一个SQLite数据库，这个数据库由 `model.py` 这个文件创建，你完全可以删掉这个测试用的数据库，只要代码重新运行 `python3 app.py` ，就会自动创建新的SQLite数据库(如果instance文件夹没有数据库)

3.关于app.py：你可以在 `app.py` 这个文件中找到一些定义，比如说 *第七行-登陆信息加密key*， *第八行，后台管理地址*， *第十行，数据库的名字(无则自动在instance文件夹创建)*

4.关于数据库：`model.py` 文件后面写明白了，**默认会插入一个管理员账户，账号为admin，密码为123456**。可惜的是，代码目前(v1.1)没有修改密码的功能，所以得手动编辑SQLite文件。

5.杂项：图片将会上传到 `static/upload` 文件夹下。一些页面信息通过在 `templates` 文件夹下的HTML文件修改，如页脚 `footer.html` (Jinja2的锅)。**`static/upload`下有测试内容，你可以全部删掉，包括instance文件夹的数据库文件，再运行代码。`github_images`只是在本文中展示，与代码无关**

---

## 页面展示

**主页面**
![主页面](/github_images/index.PNG)

**文章页面**
![文章页面](/github_images/article.PNG)

**文章编辑 未完成(v1.1)**
![文章编辑](/github_images/edit.PNG)

**后台登陆**
![后台登陆](/github_images/login.PNG)

**后台页面**
![后台页面](/github_images/admin.PNG)

**发表文章**
![发表文章](/github_images/post.PNG)

**搜索功能**
![搜索功能](/github_images/search.PNG)


