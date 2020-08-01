# Tweet-A-Bot :speech_balloon:  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
![Twitter](https://user-images.githubusercontent.com/68439180/88697078-ebfce200-d0b8-11ea-8b18-4f0f6434080f.gif)

## About 
A twitter bot that automates the process of tweeting text messages and/or images. This was performed by using webscraping tools like selenium. <br>
Programming Language: **Python 3.8.5**

## Requirements 

### System Requirements
To install a requirement, you can download from the link mentioned.
- **Python 3 and above.**            &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[Download Python](https://www.python.org/downloads/)
- **Chrome Webdriver**               &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[Chrome Webdriver Installation](https://chromedriver.chromium.org/downloads) 
- **PIP for Python in Windows**      &nbsp;&nbsp;&nbsp;&nbsp;[PIP Installation Guide](https://phoenixnap.com/kb/install-pip-windows) <br> <br>

### Python Module Requirements

- Modules required: **selenium, pillow, tk, getpass**. <br>
- These can be installed by typing the following command in CMD: ```pip3 install -r requirements.txt```
     
         
## Implementation 

- Open CMD, navigate to the working directory. Type in:  ```python Twitter_Bot.py``` 
- If you encounter an error, check if the Python version is 3 and above and the modules are installed correctly.
- On program execution, input necessary details and select the type of tweet (text/image).  
- After selecting image option, minimise all tabs inorder to view the dialog box.
- If the input details are correct, the bot will tweet from your Twitter account successfully.

## Notes 
- **Run this code on terminal (or double click the code file) and NOT ON IDLE because IDLE doesn't provide echo free password input.**
- This bot **only works in _Windows_** (due to directory address configurations which differ in other OS'es.)
- It is important to **_replace the chrome Webdriver address in line number 16_ with the address of your Webdriver's location address.** 
- After changing the address, **if you receive an error**, convert all the single back-slashes into double back-slashes in the address. **Eg: "\\" becomes "\\\\"**. 
- The password **will not echo when being typed.**

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
