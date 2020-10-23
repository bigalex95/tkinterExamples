import time
thislist = ["apple", "banana", "cherry"]
thislist.pop(0)
print(thislist)
thislist.pop(0)
print(thislist)
thislist.pop(0)
print(thislist)
thislist.append('apple')
print(thislist)
element = [2, 3, time.time()]
thislist.append(element)
print(thislist)
print(thislist[1][1])
t = time.time()
print(t)
time.sleep(5)
print(time.time() - t)
