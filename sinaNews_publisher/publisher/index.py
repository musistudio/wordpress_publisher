# -*- coding: utf-8 -*-
import logging
from getData import GetData
from config import sites
from wp import WP
import time


# if you open the initializer feature, please implement the initializer function, as below:
# def initializer(context):
#   logger = logging.getLogger()
#   logger.info('initializing')

def handler(event, context):
  logger = logging.getLogger()
  getdata = GetData()
  datas = getdata.getNewsUrl()
  wordpresses = []
  for site in sites:
      wp = WP(site['url'], site['admin']['username'], site['admin']['password'], site['SEO']['keywords'], site['SEO']['description'], site['SEO']['title'])
      wordpresses.append(wp)
  for wordpress in wordpresses:
      for data in datas:
          wordpress.publish(data['title'], data['content'])
          logger.info('{}--已为{}发布{}'.format(time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time())), wordpress.url, data['title']))
  return 'completed!'