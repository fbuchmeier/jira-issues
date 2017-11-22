# jira-issues
Get jira issue data via jira-python

## Setup
#### Using Docker
```
docker run -it -v $PWD:/work python:2.7.14 bash
pip install -r requirements.txt
cd /work
```

#### On your local machine
* Install python 2.7
* Install PIP
* Install requirements
```
pip install -r requirements.txt
```

#### Usage
```
python ./main.py -u username -a https://mydomain.com/jira -j assignee=admin
```

#### Sample output
```
----------TECH-4505------------
<JIRA Issue: key=u'TECH-4505', id=u'193407'>
u'No Logging available for all environments'
----------EKW-11420------------
<JIRA Issue: key=u'EKW-11420', id=u'245100'>
u'URL redirection for Stash REST API calls fail unauthorized'
```

## Caveats
* Some characters, like `@` must be escaped in JQL queries -> `\\u0040`
