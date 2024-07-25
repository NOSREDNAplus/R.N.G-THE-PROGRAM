import platform, os, json
from time import sleep
from random import randint

min_num = 1
max_num = 100
rate0 = 0.001
rate1 = 0.1
offset = [5,10]
roll0 = 125
roll1 = 25

n = None

if os.path.exists("./config.json"):
    try:
        with open("./config.json", "r") as f:
            d = json.load(f)
            b = d.get("use_custom")
            if b:
                for i in d.get("settings").keys():
                    if i == "min_num":
                        v = d.get("settings").get("min_num")
                        if type(v) == int:
                            min_num = d.get("settings").get("min_num")
                    elif i == "max_num":
                        v = d.get("settings").get("max_num")
                        if type(v) == int:
                            max_num = d.get("settings").get("max_num")
                    elif i == "rate0":
                        v = d.get("settings").get("rate0")
                        if type(v) == float or type(v) == int:
                            rate0 = d.get("settings").get("rate0")
                    elif i == "rate1":
                        v = d.get("settings").get("rate1")
                        if type(v) == float or type(v) == int:
                            rate1 = d.get("settings").get("rate1")
                    elif i == "offset":
                        v = d.get("settings").get("offset")
                        offset.clear()
                        if type(v.get("0")) == int:
                            offset.append(v.get("0"))
                        if type(v.get("1")) == int:
                            offset.append(v.get("1"))
                    elif i == "roll0":
                        v = d.get("settings").get("roll0")
                        if type(v) == int:
                            rate1 = d.get("settings").get("roll0")
                    elif i == "roll1":
                        v = d.get("settings").get("roll1")
                        if type(v) == int:
                            rate1 = d.get("settings").get("roll1")
                print("SYSTEM: Succesfully loaded settings")
    except Exception as e:
        print(f"Failed to load settings from config.json: {e}")
else:
    with open("config.json", "w") as f:
        f.write("""{
    "use_custom":true,
    "settings":
    {
        "max_num":100,
        "min_num":1,
        "rate0":0.001,
        "rate1":0.5,
        "offset":{
            "0":5,
            "1":10
        },
        "roll0":125,
        "roll1":25                
    }
}""")
def sysClr():
    if platform.platform().startswith("Linux"):
        os.system("clear")
    else:
        os.system("cls")
def roll(interval: float, times: int, number: int) -> None:
    i = 0
    while i != times:
        sysClr()
        s = randint(min_num, max_num)
        while s == number:
            s = randint(min_num, max_num)
        print(s)
        sleep(interval)
        i = i+1
input("> SURPRISE <")
while True:
    n = randint(min_num, max_num)
    roll(rate0, roll0, n)
    roll(rate1, roll1, n)
    temp = randint(0,1)
    ofs = randint(offset[0], offset[1])
    temp2 = None
    if temp == 0:
        temp2 = n - ofs
    else:
        temp2 = n + ofs
    sysClr()
    print(temp2)
    sleep(rate1)
    sysClr()
    print(n)
    sleep(rate1)
    input("> SURPRISE <")