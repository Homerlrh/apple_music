# COMP 2523 Project - iTunes Clone

## What it can do

Allow user to post song to AWS s3 bucket and enable user to play music in the browser

# Get started

**Create virtual environment**
on macOS and Linux:
```bash
$ python3 -m venv <envname>
```

on Windows:
```bash
$ py -m venv <envname>
```
**Active virtual environment:**
on macOS and Linux:
```bash
$ source <envname>/bin/activate
```

on windows
```bash
$ . \<envname>\Scripts\activate
```

**Check virtual environment**
on macOS and Linux:
```bash
$ which python
.../<envname>/bin/python
```

on windows
```bash
$ where python
.../<envname>/bin/python.exe
```
**Leaving vitural environment**
```bash
$ deactivate
```

## Install dependencies

**In Terminal or in VsCode Terminal**
```
$ pip install -r requirements.txt
```

## Create a S3 bucket
**Step1.**[Go to here](https://aws.amazon.com/s3/) to create a bucket

You don't need to chang any setting

![Bucket](https://i.ibb.co/McqGcCb/s3.png)

## AWS setup

**Step1.** Install AWS CLI
Download and install the package from AWS [webpage](https://aws.amazon.com/cli/)

**Step2.** configure  confidentials
```bash
$ aws configure
# prompt input
AWS Access Key ID [********************]:<your access key>
AWS Secret Access Key [********************]:<your secret access key>
Default region name [us-east-2]:<your region>
Default output format [text]:
```
>Access Key ID and Secret Access Key can be generated at AWS management console -> account -> my secret credentials 


## Create CloudFront Distribution
**Step1.** Go to [cloudFront page](https://aws.amazon.com/cloudfront/) and create a distribution

![cloudFront](https://i.ibb.co/1v8zGGG/cloud-Front.png)

**Step2.** Go to line 244 in "user_route.py" in module > bluePrints

And change line 254 "<your clounFront Domain name>"
![code change](https://i.ibb.co/gmPYwP6/code-change.png)


## Create lastFM api info
[Go to here](https://www.last.fm/api/)
1. Create api account
2. Get an api key
3. modify the ".env" file

![apiSetting](https://i.ibb.co/r7YJVNY/api-setting.png)

# last - run the app
on macOS and Linux:
```bash
$ python3 main.py
```

on windows
```bash
$ py main.py
```