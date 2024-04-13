*** Settings ***
Documentation     Test File that's used for the Robot Framework Requests.
Resource  robotResource.resource

*** Test Cases ***

Open google.com
	Open Browser  browser='chrome'
	Go To  url='https://google.com'

Open google.com 2
	Open Browser  https://google.com  chrome
	Close Browser