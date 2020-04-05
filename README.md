# Get started

## Create project with virtual environment
Create a project folder, and change work directory to the folder.
Python3 has virtualenv installed by default, and the virtual environment can be created by below command

**create virtual environment**
```bash
$ python3 -m venv
```
**active virtual environment:**
```bash
$ . venv/bin/activate
```
## Install dependencies

```bash
$ pip3 install flask
$ pip3 install boto3
$ pip3 install python-dotenv
$ pip3 install pylast
$ pip3 install lyricwikia
```
Boto is the Amazon Web Services (AWS) SDK for Python. It enables Python developers to create, configure, and manage AWS services, such as EC2 and S3. 
Before you can begin using Boto 3, we should set up authentication credentials.

## AWS setup

**Step1.** Install AWS command line interface
Download and install the package from AWS [webpage](https://aws.amazon.com/cli/)

**Step2.** configure  confidentials
```bash
$ aws configure
# prompt input
AWS Access Key ID [****************RJ3Q]:<your access key>
AWS Secret Access Key [****************KxLa]:<your secret access key>
Default region name [us-east-2]:<your region>
Default output format [text]:
```
Access Key ID and Secret Access Key can be generated at AWS management console -> account -> my secret credentials 

## boto3 API
