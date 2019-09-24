*** Settings ***
Library           requests
Library           RequestsLibrary

*** Test Cases ***
ngwlan
    Create Session    api    http://10.10.143.211:20010
    ${dicttype}    Create Dictionary    Content-Type=application/json    X-Channel-Id=ngwlan    X-Trans-Id=ngwlan123456    Accept-Charset=UTF-8
    ${d}    Set Variable    { \ \ "params": { \ \ \ \ \ \ \ \ "cooperationModelId": "", \ \ \ \ \ \ \ \ "bandwidth": "50", \ \ \ \ \ \ \ \ "areaId": "", \ \ \ \ \ \ \ \ "billId": "15026611016", \ \ \ \ \ \ \ \ "phoneNo": "", \ \ \ \ \ \ \ \ "communityName": "", \ \ \ \ \ \ \ \ "isGigabit":"", \ \ \ \ \ \ \ \ "changeType": "0", \ \ \ "crmpfPubInfo": { \ \ \ \ \ \ \ \ \ \ \ \ "staffId": "K2886", \ \ \ \ \ \ \ \ \ \ \ \ "orgId": "1000001", \ \ \ \ \ \ \ \ \ \ \ \ "cityCode": "0871", \ \ \ \ \ \ \ \ \ \ \ \ "countryCode": "1001", \ \ \ \ \ \ \ \ \ \ \ \ "paging": "***", \ \ \ \ \ \ \ \ \ \ \ \ "rowsPerPage": "***", \ \ \ \ \ \ \ \ \ \ \ \ "pageNum": "***" \ \ \ \ \ \ \ \ } \ \ \ } }
    ${addr}    Post Request    api    ngcrmpfcore_sh/csf/toAbility/queryPackagesInfo    data=${d}    headers=${dicttype}
    log    ${addr.text}
    Delete All Sessions
