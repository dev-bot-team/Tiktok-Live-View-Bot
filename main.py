from urllib.parse import urlencode
from pystyle import *
from random import choice
import os, sys, ssl, re, time, random, threading, requests, hashlib, json, base64
from console.utils import set_title
from urllib3.exceptions import InsecureRequestWarning
from http import cookiejar
from concurrent.futures import ThreadPoolExecutor
from bs4 import BeautifulSoup
from html5lib import *


System.Title("[TikTok Ultimate Bot] DBTechLabs.com")
def Banner():
    Banner1 = r"""

████████╗██╗██╗  ██╗████████╗ ██████╗ ██╗  ██╗    ██████╗  ██████╗ ████████╗
╚══██╔══╝██║██║ ██╔╝╚══██╔══╝██╔═══██╗██║ ██╔╝    ██╔══██╗██╔═══██╗╚══██╔══╝
   ██║   ██║█████╔╝    ██║   ██║   ██║█████╔╝     ██████╔╝██║   ██║   ██║   
   ██║   ██║██╔═██╗    ██║   ██║   ██║██╔═██╗     ██╔══██╗██║   ██║   ██║   
   ██║   ██║██║  ██╗   ██║   ╚██████╔╝██║  ██╗    ██████╔╝╚██████╔╝   ██║   
   ╚═╝   ╚═╝╚═╝  ╚═╝   ╚═╝    ╚═════╝ ╚═╝  ╚═╝    ╚═════╝  ╚═════╝    ╚═╝                                                                            
                                                   made by DBTechLabs.com                                                                               
    """
    Banner2 = r"""
    """
    print(Center.XCenter(Colorate.Vertical(Colors.green_to_cyan, Add.Add(Banner2, Banner1, center=True), 2)))


class BlockCookies(cookiejar.CookiePolicy):
    return_ok = set_ok = domain_return_ok = path_return_ok = lambda self, *args, **kwargs: False
    netscape = True
    rfc2965 = hide_cookie2 = False

requests.packages.urllib3.disable_warnings(category=InsecureRequestWarning)
ssl._create_default_https_context = ssl._create_unverified_context

r = requests.Session()
r.cookies.set_policy(BlockCookies())

with open(os.path.join("locale_lang.txt"), "r") as f:
        __localesLanguage = f.read().splitlines()
with open(os.path.join("region_lang.txt"), "r") as f:
        __regions = f.read().splitlines()
with open(os.path.join("region_timezone.txt"), "r") as f:
        __tzname = f.read().splitlines()
with open(os.path.join("video_links.txt"), "r") as f:
        __aweme_id = f.read().splitlines()
with open(os.path.join("room_id.txt"), "r") as f:
        __room_id = f.read().splitlines()
with open(os.path.join("live_channel_id.txt"), "r") as f:
        devices = f.read().splitlines()      
with open(os.path.join("sessions.txt"), "r") as f:
        __session_id = f.read().splitlines()
        
__domains = ["api-h2.tiktokv.com","api22-core-c-useast1a.tiktokv.com", "api19-core-c-useast1a.tiktokv.com","api16-core-c-useast1a.tiktokv.com", "api21-core-c-useast1a.tiktokv.com","api19-core-useast5.us.tiktokv.com"]
__offset = ["-28800", "-21600"]
__devices = ["SM-G9900","SM-A136U1", "SM-M225FV", "SM-E426B", "SM-M526BR", "SM-M326B","SM-A528B","SM-F711B","SM-F926B","SM-A037G","SM-A225F","SM-M325FV","SM-A226B","SM-M426B","SM-A525F","SM-N976N","SM-M526B","SM-G570MSM","SM-A520F","SM-G975F","SM-A215U1","SM-A125F","SM-J730F","SM-A207F","SM-G970F","SM-A236B","SM-J730F","SM-J730F","SM-G970F","SM-J730F","SM-J730F","SM-J327T1","SM-A205U","SM-A136B","SM-G991B","SM-G525F","SM-A528B","SM-A528B","SM-A528B","SM-A136B","SM-G900F","SM-A226B","SM-A528B","SM-A515F","SM-G935T","SM-A505F","SM-P619","SM-N976B","SM-A510M","SM-J530FM","SM-G998B","SM-A500FU", "SM-G935F"]

__versionCode = ["190303", "190205", "190204", "190103", "180904", "180804", "180803", "180802",  "270204"]
__versionUa =  [247, 312, 322, 357, 358, 415, 422, 444, 466]
__resolution = ["900*1600", "720*1280"]
__dpi = ["240", "300"]


class Gorgon:
	"IF you WANT the REST of the CODE please contact me on Telegram."

def sendViewsTest(__device_id, __install_id, cdid, openudid):
    global reqs, _lock, success, fails, rps, rpm
    for x in range(10):
        try:
            session_id = random.choice(__session_id)
            versionCode = random.choice(__versionCode)
            aweme_id = random.choice(__aweme_id)
            offset = random.choice(__offset)
            regions = random.choice(__regions)
            localesLanguage = random.choice(__localesLanguage)
            tzname = random.choice(__tzname)
            devices = random.choice(__devices)
            domains = random.choice(__domains)
            timestamp_ms = round(time.time() * 1000)
            _ts = unix=int(time.time())

            params = urlencode(
                                {
                                "IF you WANT the REST of the CODE please contact me on Telegram."
                                }
        )

            payload = f"item_id={aweme_id}&play_delta=1"
            sig     = Gorgon(params=params, cookies=None, data=None, unix=int(time.time())).get_value()
        
            response = r.post(
                url = ("https://" +  domains  + "/aweme/v1/aweme/stats/?" + params),
                data    = payload,
                headers = {"IF you WANT the REST of the CODE please contact me on Telegram."},
                verify  = False
            )
            reqs += 1
            try:
                if response.json()['status_code'] == 0:
                    _lock.acquire()
                    #print(f"Sent: {success}\nErrors: {fails}\nTotal: {success + fails}")
                    print(Colorate.Horizontal(Colors.yellow_to_green, f'Video ID : {__aweme_id} | Sent success: {success} '))
                    success += 1
                    _lock.release()
            except:
                if _lock.locked():_lock.release()
                fails += 1
                continue

        except Exception as e:
            pass

def sendViews(__device_id, __install_id, cdid, openudid):
    global reqs, _lock, success, fails, rps, rpm
    for x in range(10):
        try:
            session_id = random.choice(__session_id)
            versionCode = random.choice(__versionCode)
            aweme_id = random.choice(__aweme_id)
            offset = random.choice(__offset)
            regions = random.choice(__regions)
            localesLanguage = random.choice(__localesLanguage)
            tzname = random.choice(__tzname)
            devices = random.choice(__devices)
            domains = random.choice(__domains)

            params = urlencode(
                                {
                                   "IF you WANT the REST of the CODE please contact me on Telegram."
                                }
        )

            payload = f"item_id={aweme_id}&play_delta=1"
            sig     = Gorgon(params=params, cookies=None, data=None, unix=int(time.time())).get_value()
        
            response = r.post(
                url = (
                    "https://"
                    +  domains  +
                    "/aweme/v1/aweme/stats/?" + params
                ),
                data    = payload,
                headers = {"IF you WANT the REST of the CODE please contact me on Telegram."},
                verify  = False
            )
            reqs += 1
            try:
                if response.json()['status_code'] == 0:
                    _lock.acquire()
                    #print(f"Sent: {success}\nErrors: {fails}\nTotal: {success + fails}")
                    print(Colorate.Horizontal(Colors.yellow_to_green, f'Video ID : {__aweme_id} | Sent success: {success} '))
                    success += 1
                    _lock.release()
            except:
                if _lock.locked():_lock.release()
                fails += 1
                continue

        except Exception as e:
            pass

def getRoomID():
    try:
        "IF you WANT the REST of the CODE please contact me on Telegram."
    except Exception as e:
            pass   

def sendLiveViews(__device_id, __install_id, cdid, openudid):
    global reqs, _lock, success, fails, rps, rpm
    for x in range(10):
        try:
            session_id = random.choice(__session_id)
            versionCode = random.choice(__versionCode)
            aweme_id = random.choice(__aweme_id)
            offset = random.choice(__offset)
            regions = random.choice(__regions)
            localesLanguage = random.choice(__localesLanguage)
            tzname = random.choice(__tzname)
            devices = random.choice(__devices)
            domains = random.choice(__domains)
            timestamp_ms = round(time.time() * 1000)
            ts = unix=int(time.time())
            room_id = random.choice(__room_id)

            params = urlencode(
                                {
                                "IF you WANT the REST of the CODE please contact me on Telegram."
                                }
        )
            payload = f"room_id={room_id}&hold_living_room=1&is_login=1&enter_source=general_search-general_search&request_id=xxxxxxxxx"
            sig     = Gorgon(params=params, cookies=None, data=None, unix=int(time.time())).get_value()
        
            response = r.post(
                url = (
                    "https://"
                    +  domains  +
                    "/webcast/room/enter/?" + params
                ),
                data    = payload,
                headers = {"IF you WANT the REST of the CODE please contact me on Telegram."},
                verify  = False
            )
            reqs += 1
            try:
                if response.json()['status_code'] == 0:
                    _lock.acquire()
                    #print(f"Sent: {success}\nErrors: {fails}\nTotal: {success + fails}")
                    print(Colorate.Horizontal(Colors.yellow_to_green, f'Video ID : {__aweme_id} | Sent success: {success} '))
                    success += 1
                    _lock.release()
            except:
                if _lock.locked():_lock.release()
                fails += 1
                continue

        except Exception as e:
            pass

def sendShares(__device_id, __install_id, cdid, openudid):
    global reqs, _lock, success, fails, rps, rpm
    for x in range(10):
        try:
            session_id = random.choice(__session_id)
            versionCode = random.choice(__versionCode)
            aweme_id = random.choice(__aweme_id)
            offset = random.choice(__offset)
            regions = random.choice(__regions)
            localesLanguage = random.choice(__localesLanguage)
            tzname = random.choice(__tzname)
            devices = random.choice(__devices)
            domains = random.choice(__domains)
            versionUa = random.choice(__versionUa)

            params = urlencode(
                                {
                                   "IF you WANT the REST of the CODE please contact me on Telegram."
                                }
            )
            payload = f"share_delta=1&item_id={aweme_id}"
            sig     = Gorgon(params=params, cookies=None, data=None, unix=int(time.time())).get_value()
        
            response = r.post(
                url = (
                    "https://"
                    +  domains  +
                    "/aweme/v1/aweme/stats/?" + params
                ),
                data    = payload,
                headers = {"IF you WANT the REST of the CODE please contact me on Telegram."},
                verify  = False
            )
            reqs += 1
            try:
                if response.json()['status_code'] == 0:
                    _lock.acquire()
                    #print(f"Sent: {success}\nErrors: {fails}\nTotal: {success + fails}")
                    print(Colorate.Horizontal(Colors.yellow_to_green, f'Video ID : {__aweme_id} | Sent success: {success} '))
                    success += 1
                    _lock.release()
            except:
                if _lock.locked():_lock.release()
                fails += 1
                continue

        except Exception as e:
            pass

def sendHearts(__device_id, __install_id, cdid, openudid):
    global reqs, _lock, success, fails, rps, rpm
    for x in range(10):
        try:
            session_id = random.choice(__session_id)
            versionCode = random.choice(__versionCode)
            aweme_id = random.choice(__aweme_id)
            offset = random.choice(__offset)
            regions = random.choice(__regions)
            localesLanguage = random.choice(__localesLanguage)
            tzname = random.choice(__tzname)
            devices = random.choice(__devices)
            domains = random.choice(__domains)
            resolution = random.choice(__resolution)
            dpi = random.choice(__dpi)
            timestamp_ms = round(time.time() * 1000)
            ts = unix=int(time.time())
            params = urlencode(
                                {
                                "IF you WANT the REST of the CODE please contact me on Telegram."
                                }
        )
        
            sig     = Gorgon(params=params, cookies=None, data=None, unix=int(time.time())).get_value()
            response = r.post(
                url = ("https://xxxxxxx.com/aweme/v1/commit/item/digg/?" + params),
                headers = {"IF you WANT the REST of the CODE please contact me on Telegram."},
                verify  = False
            )
            reqs += 1
            try:
                if response.json()['status_code'] == 0:
                    _lock.acquire()
                    print(Colorate.Horizontal(Colors.yellow_to_green, f'Video ID : {__aweme_id} | Sent success: {success} '))
                    success += 1
                    _lock.release()
            except:
                if _lock.locked():_lock.release()
                fails += 1
                continue

        except Exception as e:
            pass

def sendFavorites(__device_id, __install_id, cdid, openudid):
    global reqs, _lock, success, fails, rps, rpm
    for x in range(10):
        try:
            session_id = random.choice(__session_id)
            versionCode = random.choice(__versionCode)
            timestamp_ms = round(time.time() * 1000)
            _ts = unix=int(time.time())
            aweme_id = random.choice(__aweme_id)
            domains = random.choice(__domains)
            params = urlencode(
                                {
                                "IF you WANT the REST of the CODE please contact me on Telegram."
                                }
            )
            sig = Gorgon(params=params, cookies=None, data=None, unix=int(time.time())).get_value()
            response = r.post(
                url = ("https://" +  domains  + "/aweme/v1/aweme/collect/?aweme_id=" + aweme_id + params),
                headers = {"IF you WANT the REST of the CODE please contact me on Telegram."},
                verify  = False
            )
            reqs += 1
            try:
                if response.json()['status_code'] == 0:
                    _lock.acquire()
                    print(Colorate.Horizontal(Colors.yellow_to_green, f'Video ID : {__aweme_id} | Sent success: {success} '))
                    success += 1
                    _lock.release()
            except:
                if _lock.locked():_lock.release()
                fails += 1
                continue

        except Exception as e:
            pass

def rpsm_loop():
    global rps, rpm
    while True:
        initial = reqs
        time.sleep(1)
        rps = round((reqs - initial) / 60, 1)
        rpm = round(rps * 60, 1)

def clearConsole():
    if os.name == 'posix':
        os.system('clear')
    elif os.name in ('ce', 'nt', 'dos'):
        os.system('cls')
    else:
        pass
def sendFollowers():
    try:
         print("")

    except Exception as e:
        pass

def checkRegisterUser():
    try:
        response  = requests.get("license code url to check")
        if response.status_code == 200:
            print('Welcome back man, your license is valid!')
            time.sleep(3)
        else:
            print('License is NOT valid.')
            time.sleep(3)
            sys.exit()

    except Exception as e:
        pass

def stats():
    Banner()
    print(f"Sent: {success}\nErrors: {fails}\nTotal: {success + fails}")
    set_title(f"Sent: {success} Errors: {fails} Total:{success + fails}")
     
if __name__ == "__main__":
    clearConsole()
    Banner()
    threading.Thread(target=checkRegisterUser).start()
    time.sleep(3)
    with open(os.path.join("devices.txt"), "r") as f:
        devices = f.read().splitlines()

    sendType = int(Write.Input("[1] - TikTok Video Views\n[2] - TikTok Video Favorite\n[3] - TikTok Video Share\n[4] - TikTok Video Like (heart)\n[5] - TikTok Followers\n[6] - TikTok Live Stream\n\nType option number : ", Colors.green_to_yellow, interval=0.0001))
    threads = int(Write.Input("Number of Threads: ", Colors.green_to_yellow, interval=0.0001))
    amountTosend = int(Write.Input("Number of hits: ", Colors.green_to_yellow, interval=0.0001))
    
    _lock = threading.Lock()
    reqs = 0
    success = 0
    fails = 0
    rpm = 0
    rps = 0
    
    threading.Thread(target=rpsm_loop).start()
    while True:  
        device = random.choice(devices)
        for i in range(threads):
                if sendType == 1:
                    if success >= amountTosend:
                        print("All views sent!")
                        time.sleep(3)
                        exit()
                    else:    
                        did, iid, cdid, openudid = device.split(':')
                        t = threading.Thread(target=sendViews,args=[did,iid,cdid,openudid])
                        t.start()
                if sendType == 2:
                    if success >= amountTosend:
                        print("All views sent!")
                        time.sleep(1)
                        exit()
                    else:
                        did, iid, cdid, openudid = device.split(':')
                        t = threading.Thread(target=sendFavorites,args=[did,iid,cdid,openudid])
                        t.start()
                if sendType == 3:
                    if success >= amountTosend:
                        print("All views sent!")
                        time.sleep(1)
                        exit()
                    else:
                        did, iid, cdid, openudid = device.split(':')
                        t = threading.Thread(target=sendShares,args=[did,iid,cdid,openudid])
                        t.start() 
                if sendType == 4:
                    if success >= amountTosend:
                        print("All views sent!")
                        time.sleep(1)
                        exit()
                    else:
                        did, iid, cdid, openudid = device.split(':')
                        t = threading.Thread(target=sendHearts,args=[did,iid,cdid,openudid])
                        t.start() 
                if sendType == 5:
                    if success >= amountTosend:
                        print("All views sent!")
                        time.sleep(1)
                        exit()
                    else:
                        did, iid, cdid, openudid = device.split(':')
                        t = threading.Thread(target=sendFollowers,args=[did,iid,cdid,openudid])
                        t.start()  
                if sendType == 6:
                    if success >= amountTosend:
                        print("All views sent!")
                        time.sleep(1)
                        exit()
                    else:
                        did, iid, cdid, openudid = device.split(':')
                        t = threading.Thread(target=sendLiveViews,args=[did,iid,cdid,openudid])
                        t.start()              
