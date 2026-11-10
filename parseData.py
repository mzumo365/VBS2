import win32api
import time
import math

with open("test.txt", "r", encoding="utf-8") as file:
    content = file.read()

data = []

while True:
    x = int(content[1:content.index(",")])
    content = content[content.index(",")+2:]
    y = int(content[0:content.index(")")])
    content = content[content.index(")")+3:]
    if not data:
        time1 = float(0)
    else:
        time1 = float(content[0:content.index(",")])
    if "(" in content:
        content = content[content.index("("):]
    else:
        item = [x, y, time1]
        data.append(item)
        break
    item = [x, y, time1]
    data.append(item)


def tracePath(path):
    startTime = time.perf_counter()
    for item in path:
        while True:
            endTime = time.perf_counter()
            if (endTime-startTime >= item[2]):
                win32api.SetCursorPos((item[0], item[1]))
                break

def getAngle(path):
    x1, y1 = data[0][0],data[0][1]
    x2, y2 = (data[len(data)-1][0] - x1), (y1 - data[len(data)-1][1])

    angle = math.degrees(math.atan2(y2,x2))
    if (angle < 0):
        angle+=360
    return angle

print(getAngle(data))
tracePath(data)