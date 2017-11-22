# jira-issues
Get jira issue data via jira-python

## Setup
#### Using Docker
```
docker run -it -v $PWD:/work python:2.7.14 bash
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
python ./main.py -u username -a https://mydomain.comjira -j assignee=admin
```

## Caveats
* Some characters, like `@` must be escaped in JQL queries.
