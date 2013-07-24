#!/usr/bin/env python

# Caches Google Spreadsheets on-demand in Python
# POST it a payload of the Spreadsheet key
# Expects to read a configuration file, conf.yaml

import sys
import urllib2
import re
import json

from boto.s3.connection import S3Connection
from boto.s3.key import Key

import cgi

import cgitb
cgitb.enable()

import yaml

f = open('conf.yaml')
conf = yaml.safe_load(f)
f.close()

aws_access_key = conf['aws_access_key']
aws_secret_key = conf['aws_secret_key']
bucket_name = conf['bucket_name']
prefix = conf['prefix']

form = cgi.FieldStorage()
key = form.getvalue("key")

# Save the sheets to S3
def write(filename,content):
	conn = S3Connection(aws_access_key, aws_secret_key)
	pb = conn.get_bucket(bucket_name)
	k = Key(pb)
	k.name = prefix+filename
	k.content_type = 'text/javascript'
	k.set_contents_from_string(content,headers={'Cache-Control': 'max-age=0'})
	k.set_acl('public-read')

base_json_url = "https://spreadsheets.google.com/feeds/worksheets/"+key+"/public/basic?alt=json-in-script&callback=Tabletop.singleton.loadSheets"

base_json_content = urllib2.urlopen(base_json_url).read()

sheet_ids = set(re.findall(r"/public/basic/(\w*)",base_json_content, flags=0))

for sheet_id in sheet_ids:
  sheet_url = "https://spreadsheets.google.com//feeds/list/"+key+"/"+sheet_id+"/public/values?alt=json-in-script&sq=&callback=Tabletop.singleton.loadSheet"
  content = urllib2.urlopen(sheet_url).read()
  filename = key+"-"+sheet_id
  write(filename,content)

write(key,base_json_content)

print "Content-type:text/html\r\n\r\n"
print '<html>'
print '<head>'
print '<title>Success</title>'
print '</head>'
print '<body>'
print '<h2>Execution successful</h2>'
print '</body>'
print '</html>'
