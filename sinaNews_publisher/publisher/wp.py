from wordpress_xmlrpc import Client, WordPressPost
from wordpress_xmlrpc.methods import posts

class WP():
    def __init__(self, url, username, password, keywords, description, title):
        self.wp = Client(url + 'xmlrpc.php', username, password)
        self.keywords = keywords
        self.description = description
        self.title = title
        self.url = url

    def publish(self, title, content):
        post = WordPressPost()
        post.title = title
        post.content = content
        post.post_status = 'publish'  # 文章状态，不写默认是草稿，private表示私密的，draft表示草稿，publish表示发布

        post.terms_names = {
            'post_tag': ['news'],  # 文章所属标签，没有则自动创建
            'category': ['news'],  # 文章所属分类，没有则自动创建
        }

        post.custom_fields = []
        post.custom_fields.append({
            'key': '_aioseop_keywords',
            'value': self.keywords
        })
        post.custom_fields.append({
            'key': '_aioseop_description',
            'value': self.description
        })
        post.custom_fields.append({
            'key': '_aioseop_title',
            'value': self.title
        })
        post.id = self.wp.call(posts.NewPost(post))