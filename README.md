# BandwidthStability

Bandwidth prediction using machine learning alogrithm.

## Getting Started

First we need to collect network bandwidth data, then apply linear regression - gradient descent alogrithm to predict.

We simple need to run get_data.py every hour for required period of time. We can automate this process using cron job.

### Prerequisites

tinydb
speedtest-cli

### Installing pre-requisites 

```
pip install -r requirements.txt
```

### Setting cronjob

```
crontab -e
Append this line "*/10 * * * * /usr/bin/python /path/to/file/get_data.py"
```


