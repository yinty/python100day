*** Settings ***
Library           RequestsLibrary

*** Test Cases ***
TestCase01
    Open Browser    https://www.jianshu.com/p/9dcb4242b8f2    chrome

TestCase02
    Create Session    testerhome    https://testerhome.com
    ${resp}    Get Request    testerhome    /topics/8746
    Should Be Equal As Integers    ${resp.status_code}    200    【error】接口请求失败，status_
    log    ${resp.content}
