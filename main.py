from getData import GetData
from config import sites
from wp import WP

getdata = GetData()
datas = getdata.getNewsUrl()
wordpresses = []
for site in sites:
    wp = WP(site['url'], site['admin']['username'], site['admin']['password'], site['SEO']['keywords'],
            site['SEO']['description'], site['SEO']['title'])
    wordpresses.append(wp)

for wordpress in wordpresses:
    for data in datas:
        wordpress.publish(data['title'], data['content'])
        print('已为{}发布{}'.format(wordpress.url, data['title']))