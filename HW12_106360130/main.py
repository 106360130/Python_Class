from AnalyzeData import AnalyzeData



hand = open('log.txt')

#分析資料
#初始化
VIP = dict()
member = dict()
product = dict()
#初始化


for line in hand:
    line = line.rstrip()
    #print(line)
    #print(re.search('VIP', line))
    result_find = AnalyzeData()
    if result_find.if_data(line, "VIP") :
  
        #除了字母、數字，其餘特殊符號前面最好都加"\"，比較有統一性
        name = AnalyzeData().catch_data_mid(line, "\[VIP] ", "\ buys")
        item = AnalyzeData().catch_data_mid(line, "buys ", "\ for")
        price = AnalyzeData().catch_data_back(line, "\$")


        # print("item : {}".format(item[0]))
        #print(coustomer["item"].has_key([str(item[0])])

        if not name[0] in VIP :  #如果dict中沒有"name[0]"的key，就先創一個，初始化
            VIP[name[0]] = dict()
            
        if str(item[0]) in VIP[name[0]] :  #price會變動，如果此"item[0]"已經存在，price就疊加上去
            VIP[name[0]][str(item[0])] = VIP[name[0]][str(item[0])] + int(price[0])

        else :  #如果沒有就新增
            VIP[name[0]][str(item[0])] = int(price[0])

    else :
        #print("Member")

        name = AnalyzeData().catch_data_front(line, "\ buys")
        item = AnalyzeData().catch_data_mid(line, "buys ", "\ for")
        price = AnalyzeData().catch_data_back(line, "\$")
        

        if not name[0] in member :
            member[name[0]] = dict()
            
        if str(item[0]) in member[name[0]] : 
            member[name[0]][str(item[0])] = member[name[0]][str(item[0])] + int(price[0])

        else :
            member[name[0]][str(item[0])] = int(price[0])
    
    if str(item[0]) in product : 
        product[str(item[0])] = product[str(item[0])] + int(price[0])

    else :
        product[str(item[0])] = int(price[0])

# print(VIP)
# print(member)
# print(product)
#分析資料

#列印分析結果
print("===Analysis_result.txt===\n")

print("[VIP]")
for person in VIP.keys() :
    print("{} buys".format(person), end="")

    string_item = ""
    for item in VIP[person].keys():
        string_item += " {}: {},".format(item, VIP[person][item])  #先將要列印的string串接起來
        #print("{}: {}, ".format(item, VIP[person][item]), end="")

    print(string_item[:-1])  #最後一個character不要列印，就不會列印出最後一個","


print("\n[Member]")
for person in member.keys() :
    print("{} buys".format(person), end="")

    string_item = ""
    for item in member[person].keys():
        string_item += " {}: {},".format(item, member[person][item])  #先將要列印的string串接起來

    print(string_item[:-1])  #最後一個character不要列印，就不會列印出最後一個","


print("")
for item in product :
    print("Total {} sales: {}".format(item, product[item]))
#列印分析結果

#將分析結果寫入txt檔
#可以先將要寫入的資料都"串接"起來，再寫進去txt檔
f = open('data.txt', 'w')
f.write("===Analysis_result.txt===")


f.write("\n\n[VIP]")
for person in VIP.keys() :
    f.write("\n{} buys".format(person))

    string_item = ""
    for item in VIP[person].keys():
        string_item += " {}: {},".format(item, VIP[person][item])  #先將要列印的string串接起來

    f.write(string_item[:-1])  #最後一個character不要列印，就不會列印出最後一個","


f.write("\n\n[Member]")
for person in member.keys() :
    f.write("\n{} buys".format(person))

    string_item = ""
    for item in member[person].keys():
        string_item += " {}: {},".format(item, member[person][item])  #先將要列印的string串接起來

    f.write(string_item[:-1])  #最後一個character不要列印，就不會列印出最後一個","


f.write("\n")
for item in product :
    f.write("\nTotal {} sales: {}".format(item, product[item]))

f.close()
#將分析結果寫入txt檔