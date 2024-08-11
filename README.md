# taiko-music-recruitment-ws
automatically download songs from Taiko No Tatsujin music recruitment website using python

# Usage
1. Install Python and add into system variables
2. Clone this repository
3. Download [ChromeDriver](https://googlechromelabs.github.io/chrome-for-testing/) based on your platform
4. Extract `chromedriver.exe` from the zip and put into the repository
5. (Optional) If you have bad specs with your PC, revise the driver timeout and sleep time with a longer value (at line 21, 38 and 69)
6. Either do:
    - Run command prompt through the repository folder, type `python taiko2020/taiko2020.py` and hit Enter
    - Right click the `.py` file, select `Open with` then choose `python.exe`
7. The .py file will print "下載完成，共耗時: xxx.yy秒" once all files are downloaded
