# taiko-music-recruitment-ws
automatically download songs from Taiko No Tatsujin music recruitment website using python
## Years Available
- 2020
- 2024

# Usage
1. Install Python and add into system variables
2. Install packages
    ```
   pip install requests selenium
    ```
3. Clone this repository
4. Download [ChromeDriver](https://googlechromelabs.github.io/chrome-for-testing/) based on your platform
5. Extract `chromedriver.exe` from the zip and put into the repository
6. (Optional) If you have bad specs with your PC, revise the driver timeout and sleep time with a longer value
7. Run cmd through the repository path and the following command
   ```
    python taiko<year>/taiko<year>.py
   ```
   where `<year>` in [Years Available](https://github.com/MarioUniverseZ/taiko-music-recruitment-ws/tree/main#years-available)
8. The .py file will print "下載完成，共耗時: xxx.yy秒" once all files are downloaded
