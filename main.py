#!/usr/bin/python
from __future__ import print_function
from jira import JIRA
import re
import getopt
import getpass
import sys
import pprint

# ------ init ---------#
user = ""
password = ""
url = ""
debug = ""

pp = pprint.PrettyPrinter(indent=4)

try:
    options, remainder = getopt.getopt(sys.argv[1:], 'u:p:a:j:d', ['user=',
                                                                     'password=',
                                                                     'application=',
                                                                     'jql=',
                                                                     'debug'
                                                                     ])
except getopt.GetoptError as err:
    print(str(err))

for opt, arg in options:
    if opt in ('-u', '--user'):
        user = arg
    elif opt in ('-p', '--password'):
        password = arg
    elif opt in ('-a', '--application'):
        url = arg
    elif opt in ('-j', '--jql'):
        jql = arg
    elif opt in ('-d', '--debug'):
        debug = True

if not password:
    password = getpass.getpass()

if not user:
    print("User not set. Use '-u username' to correct.")
    sys.exit(2)

if not url:
    print("Application URL not set. Use '-a url' to correct.")
    sys.exit(2)

if not jql:
    print("JQL not set. Use '-j jql-filter' to correct.")
    sys.exit(2)

# ------ main ---------#
options = {
    'server': url,
    }

# Connect to jira
jira = JIRA(options, basic_auth=(user, password))

# Search for issues
issues = jira.search_issues(jql)

# Get field values from issues
for issue in issues:
    print("----------" + issue.key + "------------")
    pp.pprint(issue)
    data = jira.issue(issue.key)
    pp.pprint(data.fields.summary)
