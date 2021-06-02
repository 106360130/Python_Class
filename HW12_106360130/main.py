from AnalyzeData import AnalyzeData


def main() :
    data_log = open('log.txt')

    [VIP, member, product] = analyze_data(data_log)  #分析資料

    string_data_reault =  gather_data_to_string(VIP, member, product)  #匯集data,串接成string
    #print(string_data_reault)  #列印分析結果

    write_in_txt("data.txt", string_data_reault)  #將分析結果寫入txt檔
    
    data_log.close()


#分析資料
def analyze_data(data_log) :
    #初始化
    VIP = dict()
    member = dict()
    product = dict()
    #初始化

    for line in data_log:
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
    print("Finishing analyzing data.")
    return VIP, member, product
#分析資料

#將分析結果寫入txt檔
#可以先將要寫入的資料都"串接"起來，再寫進去txt檔
def write_in_txt(txt_name, data_reault) :
    f = open('{}'.format(txt_name), 'w')
    f.write(data_reault)
    f.close()
    print("Finishing writing into {}.".format(txt_name))
#將分析結果寫入txt檔

#匯集data,串接成string
def gather_data_to_string(VIP, member, product) :
    string_data_reault = ""

    string_data_reault += "===Analysis_result.txt==="
    
    string_data_reault += "\n\n[VIP]"

    for person in VIP.keys() :
        string_data_reault += "\n{} buys".format(person)

        string_item = ""
        for item in VIP[person].keys():
            string_item += " {}: {},".format(item, VIP[person][item])  #先將要列印的string串接起來

        string_data_reault += string_item[:-1]  #最後一個character不要列印，就不會列印出最後一個","


    string_data_reault += "\n\n[Member]"
    for person in member.keys() :
        string_data_reault += "\n{} buys".format(person)

        string_item = ""
        for item in member[person].keys():
            string_item += " {}: {},".format(item, member[person][item])  #先將要列印的string串接起來

        string_data_reault += string_item[:-1]  #最後一個character不要列印，就不會列印出最後一個","


    string_data_reault += "\n"
    for item in product :
        string_data_reault += "\nTotal {} sales: {}".format(item, product[item])

    return string_data_reault
#匯集data,串接成string

    
main()