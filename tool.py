import json

#xu ly duong dan feature_files
print("Duong dan feature_files: ")
try:
    urlFeature_files = input()
    fin = open(urlFeature_files)
except FileNotFoundError:
    print("Khong thay file, kiem tra lai duong dan")
    exit()
else:
    data = json.load(fin)

#xu ly duong dan package
print("Duong dan package: VD: BW/ten-package (MW/ten-package)")
urlPackage = input()

#khai bao gia tri ban dau cac bien mostUsed
o = a = s = tempLen1 = 0

#Opcodes
data2 = list(data[urlPackage]['Static_analysis']['Opcodes'].values())
temp1 = data2[0]
for x, y in data[urlPackage]['Static_analysis']['Opcodes'].items():
    temp = int(data[urlPackage]['Static_analysis']['Opcodes'][x])
    if temp >= o:
        o = temp
        mostUsedOpcode = x
    if temp1 >= temp:
        temp1 = temp
        leastUsedOpcode = x

#API Calls
data2 = list(data[urlPackage]['Static_analysis']['API calls'].values())
temp1 = data2[0]
for x, y in data[urlPackage]['Static_analysis']['API calls'].items():
    temp = int(data[urlPackage]['Static_analysis']['API calls'][x])
    if temp >= a:
        a = temp
        mostUsedApi = x
    if temp1 >= temp:
        temp1 = temp
        leastUsedApi = x

#Strings
data2 = list(data[urlPackage]['Static_analysis']['Strings'].keys())
tempLen2 = len(data2[0])
for x, y in data[urlPackage]['Static_analysis']['Strings'].items():
    temp = int(data[urlPackage]['Static_analysis']['Strings'][x])
    if len(x) >= tempLen1:
        tempLen1 = len(x)
        longestString = x
    if len(x) <= tempLen2:
        tempLen2 = len(x)
        shortestString = x
    if temp >= s:
        s = temp
        string = x

#virustotal
virusTotalLink = (data[urlPackage]['VirusTotal']['permalink'])

#Don gian chi la print
print("Opcode duoc su dung nhieu nhat: " + mostUsedOpcode + " - " + str(o))
print("Opcode duoc su dung it nhat: " + leastUsedOpcode)
print("API Call duoc su dung nhieu nhat: " + mostUsedApi + " - " + str(a))
print("API Call duoc su dung it nhat: " + leastUsedApi)
print("String duoc su dung nhieu nhat: " + string + " - " + str(s))
print("String dai nhat: " + longestString)
print("String ngan nhat: " + shortestString)
print("Duong dan Virustotal: " + virusTotalLink )