# Meetup - API : Python implementation for fosscafe meetup 

### Installation Details are mentioned below.

* Pip to install Meetup Api
    + Use pip to install meetup-api .
    + ```Python
        pip install meetup-api
        ```

* Windows :
    +   Setup Your meetup_api_key as environment variable
    + On powershell run 
        ```Powershell
        $env:MEETUP_API_KEY = "< your meetup api key >"
        ```
    + Then type the following to run script.
    ```Python
    python fetch-meetup-details.py 
    ```
* Linux :
    + Set environment variable as 
    ```Bash
     export MEETUP_API_KEY=<your meetup api key>
     ```
    + Run Python script as following:
    ```Python
    python fetch-meetup-details.py
    ```

# Few important details :
* Runs on Python3
* To run on Python2, change print syntax. Rest should work fine.
* Meetup URL name is hardcoded to "fosscafe".

