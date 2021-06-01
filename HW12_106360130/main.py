import re

hand = open('log.txt')


#初始化
VIP = dict()
member = dict()
product = dict()
#初始化


for line in hand:
    line = line.rstrip()
    #print(line)
    #print(re.search('VIP', line))
    if re.search('VIP', line) :
        #print("VIP")

        #print(line)
        #print("re.search : {}".format(re.search('From:', line)))
        #(?<=)  //前面的string
        #(?=)  //後面的srting
        #(?<=)()(?=)  //"抓取"在這兩個string之間的"character"
        name = re.findall('(?<=\[VIP]\ )(.*?)(?=\ buys)', line)
        item = re.findall('(?<=buys )(.*?)(?= for)', line)
        price = re.findall('\$([0-9]+)', line)
        
        
        # print("type(name)) : {}".format(type(name)))
        # print("name : {}".format(name))
        # print("price : {}".format(price))


        # print("item : {}".format(item[0]))
        #print(coustomer["item"].has_key([str(item[0])])

        if not name[0] in VIP :
            VIP[name[0]] = dict()
            
        if str(item[0]) in VIP[name[0]] : 
            VIP[name[0]][str(item[0])] = VIP[name[0]][str(item[0])] + int(price[0])

        else :
            VIP[name[0]][str(item[0])] = int(price[0])

    else :
        #print("Member")

        name = re.findall('(.*?)(?=\ buys)', line)
        item = re.findall('(?<=buys )(.*?)(?= for)', line)
        price = re.findall('\$([0-9]+)', line)

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

print(VIP)
print(member)
print(product)

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