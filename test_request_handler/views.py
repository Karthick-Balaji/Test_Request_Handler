
from django.utils.timezone import datetime
from django.http import HttpResponse
from robot import run_cli, rebot_cli
from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from robot.running import TestSuite
import json
from robot.api import ExecutionResult

def home(request):
    payload =   {
                    "tests": [
                        {
                            "title": "Open google.com",
                            "steps": [
                                "Open Browser  browser='chrome'",
                                "Go To  url='https://google.com'"
                            ]
                        },
                        {
                            "title": "Open google.com 2",
                            "steps": [
                                "Open Browser  https://google.com  chrome",
                                "Close Browser"
                            ]
                        }
                    ]
                }
    reqFile = open('./test_request_handler/request.robot','w')
    reqFile.write('''*** Settings ***
Documentation     Test File that's used for the Robot Framework Requests.
Resource  robotResource.resource

*** Test Cases ***''')
    for testCase in payload["tests"]:
        reqFile.write('\n\n' + testCase["title"])
        for steps in testCase["steps"]:
            reqFile.write('\n\t' + steps)

    
    reqFile.close()

    suite = TestSuite.from_file_system('./test_request_handler/request.robot')
    suite.run(output='output.xml')
    response = HttpResponse()
    response.headers["Content-Type"] = "application/xml"
    response.status_code = 200
    outputFile = open('output.xml','r')
    responseBody = outputFile.read()
    outputFile.close()
    response.write(responseBody)
    return response

@api_view(['POST'])
def postData(request):
    testSuite = json.loads(request.body)
    reqFile = open('./test_request_handler/request.robot','w')
    reqFile.write('''*** Settings ***
Documentation     Test File that's used for the Robot Framework Requests.
Resource  robotResource.resource

*** Test Cases ***''')
    for testCase in testSuite["tests"]:
        reqFile.write('\n\n' + testCase["title"])
        for steps in testCase["steps"]:
            reqFile.write('\n\t' + steps)
    
    reqFile.close()
    result = ExecutionResult('output.xml')
    stats = result.statistics

    suite = TestSuite.from_file_system('./test_request_handler/request.robot')
    suite.run(output='output.xml')
    response = HttpResponse()
    response.headers["Content-Type"] = "application/xml"
    response.status_code = 200
    # outputFile = open('output.xml','r')
    # responseBody = outputFile.read()
    # outputFile.close()
    response.write(result)
    return response