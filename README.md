## 使用python实现自动向wordpress推送文章
##### 搭配阿里云函数计算可实现每天定时抓取新浪新闻推送到wordpress，并自动设定KDT(需安装All in One SEO插件并启用高级设置里的Unprotect Post Meta Fields选项)


#### 用法：

##### 本地运行
1. 使用```pip3 install -r requements.txt```安装依赖
2. 修改配置文件```config.py```      
在sites列表里添加一个对象，格式如下:
```python
{
    "url": "http://www.test.com/", # 站点地址
    "admin": {
        "username": "username",    # 站点后台用户名
        "password": "password"     # 站点后台密码
    },
    "SEO": {
        "keywords": "keywords",       # 文章页的keywords
        "description": "description", # 文章页的description
        "title": "title"              # 文章页的title
    }
}
```

##### 阿里云函数计算
1. 使用```fun install --runtime python3 --package-type pip requests BeautifulSoup4```安装依赖(阿里云没有wordpress-xmlrpc库，需手动复制)
2. 修改配置(如上)
3. 上传函数(可以使用文件夹上传)并在阿里云控制台配置触发时间