import requests, json
dev_count=0
other_count=0
for job in requests.get("https://jobs.github.com/positions.json?utf8=%E2%9C%93&description=&location=New+York").json():
    print("Type: {0}, Description: {1}".format(job['type'], job['title']))
    if ("Developer" or "Engineer") in job['title']:
        dev_count+=1
    else:
        other_count+=1
print("Developerjobs: {0}, Other jobs: {1}".format(dev_count, other_count))
print("Developer-Ratio: {0:.2%}".format(dev_count/(dev_count + other_count)))
