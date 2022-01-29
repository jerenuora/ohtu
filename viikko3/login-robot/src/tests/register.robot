*** Settings ***
Resource  resource.robot
Test Setup  Input New Command And Create User


*** Test Cases ***
Register With Valid Username And Password
    Input Credentials  teppo  teppo123
    Output Should Contain  New user registered

Register With Already Taken Username And Valid Password
    Input Credentials  kalle  teppo123
    Output Should Contain  User with username kalle already exists

Register With Too Short Username And Valid Password
    Input Credentials  k  teppo123
    Output Should Contain  Invalid username

Register With Valid Username And Too Short Password
    Input Credentials  teppo  t1
    Output Should Contain  Password is required to be atleast 8 characters long

Register With Valid Username And Long Enough Password Containing Only Letters
    Input Credentials  teppo  teppotee
    Output Should Contain  Password has to contain atleast one number
*** Keywords ***
Input New Command And Create User
    Create User  kalle  kalle123
    Input New Command