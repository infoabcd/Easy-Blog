# Easy-Blog v1.1
Uses flask, SQLite and bootstrap, with total mentions under 500kb

## 这是什么
这是一个由Flask(后端和Jinja2模板引擎)+SQLite实现的超简单博客方案，只算代码，估计甚至没有200kb。

事实上，我使用Express+React等现代组合。我曾经写过PHP，我不否认PHP实在好，但是它的函数实在多得糟糕，并且安装极其繁琐，在我入门Linux时，PHP简直是我的噩梦。

而这次带来的**Flask(Jinja2)+SQLite数据库(使用ORM模型操作)博客程序**是为了完成我的Python大作业。

## 可以学到什么
虽然我几乎没有花什么时间就完成了这个作业(因为是作业，**我写了很多笔记，包括HTML的易错点**(我经常记混，因为我学了很多乱七八糟的东西), **如果你打算学习Flask和网页开发，我认为这个项目应该可以帮到你**)，但是令我感到痛苦的就是，Jinja2的写法，大量使用{{}}，并且我的编辑器没有Jinja2的语法联想，我写了很多繁琐的，易错的HTML。于是我一直在完善，写笔记。

在作业要求下，我使用了Bootstrap5 CSS框架(离线引入)。Bootstrap5的官网我认为很糟糕，起码对我而言是，我查询了海量的文档，想知道这个类到底对应了什么，最终还是妥协，把大部分布局留给了Ai做。

---

### 还没有写完编辑文章的图片删除和更改路由

---

## 项目指引

第一次运行：`pip3 install -r requirements.txt` 安装所需的库

关于数据库：instance文件夹存放了一个SQLite数据库，这个数据库由model.py这个文件创建，你完全可以删掉这个测试用的数据库，只要代码重新运行`python3 app.py`，就会自动创建新的SQLite数据库(如果instance文件夹没有数据库)

关于app.py：
