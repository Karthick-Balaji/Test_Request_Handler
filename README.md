# Test_Request_Handler
This is a Python project using Django for handling REST API requests and Robot Framework for keyword-driven acceptance testing.

## How to run
This project starts a web server that listens for a POST API call to the end point: http://127.0.0.1:8000/testai/tests/v1/execute
The request body should be as follows:
```
{
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
```
The response would be of xml format stating the test statistics.
Sample output for the above request is as follows
```
<?xml version="1.0" encoding="UTF-8"?>
<robot generator="Robot 7.0 (Python 3.12.2 on win32)" generated="2024-04-13T17:07:04.647188" rpa="false" schemaversion="5">
    <suite id="s1" name="Request" source="C:\Karthick_Balaji\code\Test_Request_Handler\test_request_handler\request.robot">
        <test id="s1-t1" name="Open google.com" line="7">
            <kw name="Open Browser" owner="SeleniumLibrary">
                <msg time="2024-04-13T17:07:05.570152" level="FAIL">ValueError: 'chrome' is not a supported browser.</msg>
                <arg>browser='chrome'</arg>
                <doc>Opens a new browser instance to the optional ``url``.</doc>
                <status status="FAIL" start="2024-04-13T17:07:05.567153" elapsed="0.013000">ValueError: 'chrome' is not a supported browser.</status>
            </kw>
            <kw name="Go To" owner="SeleniumLibrary">
                <arg>url='https://google.com'</arg>
                <doc>Navigates the current browser window to the provided ``url``.</doc>
                <status status="NOT RUN" start="2024-04-13T17:07:05.583156" elapsed="0.000000"/>
            </kw>
            <status status="FAIL" start="2024-04-13T17:07:05.561154" elapsed="0.025005">ValueError: 'chrome' is not a supported browser.</status>
        </test>
        <test id="s1-t2" name="Open google.com 2" line="11">
            <kw name="Open Browser" owner="SeleniumLibrary">
                <arg>https://google.com</arg>
                <arg>chrome</arg>
                <doc>Opens a new browser instance to the optional ``url``.</doc>
                <status status="PASS" start="2024-04-13T17:07:05.592162" elapsed="3.619400"/>
            </kw>
            <kw name="Close Browser" owner="SeleniumLibrary">
                <doc>Closes the current browser.</doc>
                <status status="PASS" start="2024-04-13T17:07:09.212558" elapsed="2.162155"/>
            </kw>
            <status status="PASS" start="2024-04-13T17:07:05.590158" elapsed="5.786584"/>
        </test>
        <doc>Test File that's used for the Robot Framework Requests.</doc>
        <status status="FAIL" start="2024-04-13T17:07:04.654192" elapsed="6.724534"/>
    </suite>
    <statistics>
        <total>
            <stat pass="1" fail="1" skip="0">All Tests</stat>
        </total>
        <tag></tag>
        <suite>
            <stat pass="1" fail="1" skip="0" id="s1" name="Request">Request</stat>
        </suite>
    </statistics>
    <errors></errors>
</robot>
```
## Required Dependencies:
- Python
- pip
- robot framework
- selenium
