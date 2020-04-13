# COMP 2523 Project - iTunes Clone

## What it can do

Allow user to post song to AWS s3 bucket and enable user to play music in the browser

## What we user
* Python flask
* SQLite
* S3 bucket

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

And change line 254 "your clounFront Domain name"

![code change](https://i.ibb.co/gmPYwP6/code-change.png)


## Create lastFM api info
[Go to here](https://www.last.fm/api/)
1. Create api account
2. Get an api key
3. modify the ".env" file, if there is no ".env" create one

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

## Things to be Implemented
<ul>
  <li>Upgrade schema to use natural primary keys ie. International Standard Recording Code (ISRC)</li>
  <li>Switch to full 13 table SQL database</li>
  <ul>
    <li>Updated Schema includes all many-many relationships</li>
    <li>ie. playlist_songs, artist_songs</li>
  </ul>
  <li>Integrate authentication from Gurmeet's code to Master</li>
  <li>Implement Authorisation status levels such that:</li>
  <ul>
    <li>Only database admins can upload songs/create albums etc. to the database</li>
    <li>Users have read-only privileges, plus ability to create playlists</li>
    <li>Free user restrictions / paid user access</li>
  </ul>
  <li>Upload full test environment with 100 songs to test</li>
  <li>Create automated test suite with pytest and implement github actions for continuous integration</li>
  <li>Centralized error handling</li>
  <li>Write documentation</li>
</ul>
