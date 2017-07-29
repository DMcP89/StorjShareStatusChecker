#Storjshare Status Checker

Small script package to collect stats from Storjshare and sends them to IFTTT.


### Setup

1. Clone the project to your local machine.
    ```
    git clone https://github.com/DMcP89/StorjShareStatusChecker.git
    ```
2. Install required packages.
    ```
    pip install -R requirements.txt
    ```
3. Add IFTTT details to properties.ini file.
    ```
    [IFTTT]
    KEY={YOUR IFTTT KEY}
    TRIGGER={YOUR ITTT TRIGGER}
    ```
4. Create webhook event on IFTTT.(https://gist.github.com/austinhuang0131/3846a66790ecc240ec470229b4318cdf/)