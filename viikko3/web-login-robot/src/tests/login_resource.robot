*** Settings ***
Library  SeleniumLibrary
Library  ../AppLibrary.py

*** Variables ***
${SERVER}  localhost:5000
${BROWSER}  headlesschrome
${DELAY}  0 seconds
${HOME URL}  http://${SERVER}
${LOGIN URL}  http://${SERVER}/login
${REGISTER URL}  http://${SERVER}/register

*** Keywords ***

Register Successfully
    Set Username  heikki
    Set Password  heikki123
    Set PasswordConfimation  heikki123
    Submit Credentials

Register Unsuccessfully
    Set Username  h
    Set Password  h1
    Set PasswordConfimation  heikki123
    Submit Credentials

Set Username
    [Arguments]  ${username}
    Input Text  username  ${username}

Set Password
    [Arguments]  ${password}
    Input Password  password  ${password}

Set PasswordConfimation
    [Arguments]  ${password_confirmation}
    Input Password  password_confirmation  ${password_confirmation}
Submit Credentials
    Click Button  Register

Login Should Succeed
    Main Page Should Be Open
Login Should Not Succeed
    Login Page Should Be Open
    Page Should Contain  Invalid username or password
