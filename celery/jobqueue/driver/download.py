import requests
import re
import io
import platform
import zipfile
import glob

home = "https://chromedriver.chromium.org/home"

def check_exists():
    files = [f for f in glob.glob("./chromedriver*")]
    return len(files) != 0

def download_driver():
    if check_exists():
        # print("chromedriver was downloaded")
        return
    response = requests.get(home)

    if response.status_code != 200:
        print("Can not fetch data...")
        return

    version = re.search(r'Latest stable.*?http.*?=(.*?)/"', response.text).group(1)

    download_link = ""
    platform_ = platform.system().lower()
    if(platform_ ==  "windows"):
        download_link = f"https://chromedriver.storage.googleapis.com/{version}/chromedriver_win32.zip"
    elif platform_ ==  "linux":
        download_link = f"https://chromedriver.storage.googleapis.com/{version}/chromedriver_linux64.zip"
    else:
        download_link = f"https://chromedriver.storage.googleapis.com/{version}/chromedriver_mac64.zip"

    r = requests.get(download_link, stream=True)
    z = zipfile.ZipFile(io.BytesIO(r.content))
    z.extractall()
    import os
    executable_path = os.path.join(os.getcwd(), 'chromedriver')
    os.chmod(executable_path, 755)