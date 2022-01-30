*** Settings ***
Resource  resource.robot
Suite Setup  Open And Configure Browser
Suite Teardown  Close Browser
Test Setup  Go To Register Page




*** Test Cases ***

Register With Valid Username And Password
    Set Username  heikki
    Set Password  heikki123
    Set PasswordConfimation  heikki123
    Submit Credentials
    Register Should Succeed

Register With Too Short Username And Valid Password
    Set Username  h
    Set Password  heikki123
    Set PasswordConfimation  heikki123
    Submit Credentials
    Register Should Not Succeed
    Register Should Throw Error Invalid Password

Register With Valid Username And Too Short Password
    Set Username  heikki
    Set Password  h1
    Set PasswordConfimation  h1
    Submit Credentials
    Register Should Not Succeed
    Register Should Throw Error Too Short Password

Register With Nonmatching Password And Password Confirmation
    Set Username  heikki
    Set Password  heikki123
    Set PasswordConfimation  teppo123
    Submit Credentials
    Register Should Not Succeed
    Register Should Throw Error Passwords Dont Match


*** Keywords ***
Register Should Succeed
    Welcome Page Should Be Open

Register Should Not Succeed
    Register Page Should Be Open

Register Should Throw Error Too Short Password
    Register Page Should Contain Too Short Password

Register Should Throw Error Invalid Password
    Register Page Should Contain Invalid Username

Register Should Throw Error Passwords Dont Match
    Register Page Should Contain Passwords Dont Match


Submit Credentials
    Click Button  Register

Set Username
    [Arguments]  ${username}
    Input Text  username  ${username}

Set Password
    [Arguments]  ${password}
    Input Password  password  ${password}

Set PasswordConfimation
    [Arguments]  ${password_confirmation}
    Input Password  password_confirmation  ${password_confirmation}
