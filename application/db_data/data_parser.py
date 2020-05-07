# import boto3
# #Put Item
# #75, 79, 85, 80, 78,82 채움
# dynamodb = boto3.resource('dynamodb')
# table = dynamodb.Table('ChatBotForInformation')

r = open('crawling_result/crollingResult_Total_Dinning82.txt', mode='rt', encoding='utf-8')
i = 0

#|addr1|areacode|contentid|contenttypeid|dongcode|firstimage|homepage|map x,y|overview|sigungucode|tel|title|zipcode|cat1|cat1|cat2|cat3

def readUntilOr(variable):
    text = r.read(1)
    buffer = ''
    while (text != '|'):
        buffer = str(buffer) + text
        text = r.read(1)
    variable = buffer
    return variable

def readHomepage(HP) : #긁어온 양식을 조금 수정해서 http만 남도록
    start_Index = HP.find("http")
    slicedHomepage = ''

    if (start_Index == -1):
        return "None homepage"

    i = start_Index
    try :
        while(HP[i] != '''"''') :
            slicedHomepage = slicedHomepage + HP[i]
            i = i+1
        return slicedHomepage
    except:
        return HP

new_txt = open('data2', 'w', -1, "utf-8")

while(i < 442) :
    addr1 = None; areacode = None; contentid = None; contenttypeid = None; dongcode = None; firstimage = None;
    homepage = None; maps = None; overview = None; sigungucode = None; tel = None; title = None; zipcode = None;
    cat1 = None; cat2 = None; cat3 = None; missCat = None;

    #print("_____________NEW________________________")
    i = i+1
    print(i)
    if i == 442:
        break
    new_txt.write(str(i)+'\n')
    addr1 = readUntilOr(addr1)
    print("addr1 :", addr1)
    #count_OR = count_OR + 1

    areacode = readUntilOr(areacode)
    # print("areacode: ",areacode)
    #count_OR = count_OR + 1

    contentid = readUntilOr(contentid)
    print("contentid: ", contentid)
    # new_txt.write(str(contentid)+'\n')
    #count_OR = count_OR + 1

    contenttypeid = readUntilOr(contenttypeid)
    #print("contenttypeid: ", contenttypeid)
    #count_OR = count_OR + 1

    dongcode = readUntilOr(dongcode)
    #print("dongcode: ", dongcode)
    #count_OR = count_OR + 1

    firstimage = readUntilOr(firstimage)
    # print("firstImage: ", firstimage)
    # new_txt.write(str(firstimage)+'\n')
    #count_OR = count_OR + 1

    homepage = readUntilOr(homepage)
    homepage = readHomepage(homepage)
    # print("homepage:", homepage)
    #count_OR = count_OR + 1

    maps = readUntilOr(maps)
    #print("maps: ", maps)
    #count_OR = count_OR + 1

    overview = readUntilOr(overview)
    if(overview=='') :
        overview = "None overview"

    # print("overview: ", overview)
    # new_txt.write(str(overview)+'\n')

    #count_OR = count_OR + 1

    sigungucode = readUntilOr(sigungucode)
    #print("sigungucode: ", sigungucode)
    #count_OR = count_OR + 1

    tel = readUntilOr(tel)
    print("tel: ", tel)
    #count_OR = count_OR + 1

    title = readUntilOr(title)
    print("title: ", title)
    #count_OR = count_OR + 1

    zipcode = readUntilOr(zipcode)
    #print("zipcode: ", zipcode)
    #count_OR = count_OR + 1

    cat1 = readUntilOr(cat1)
    # print("cat1: ", cat1)

    missCat = readUntilOr(missCat)

    cat2 = readUntilOr(cat2)
    # print("cat2: ", cat2)

    cat3 = readUntilOr(cat3)
    # print("cat3: ", cat3)
    print()

    r.read(1)   #줄바꿈문자

    new_txt.write(str(contentid) + "\n")
    new_txt.write(str(title) + "\n")
    new_txt.write(str(addr1) + "\n")
    new_txt.write(str(tel) + "\n")
    new_txt.write('\n')

    if(areacode == "No areacode"):      # 아니무슨 areacode가 없는 놈들이있냐
        areacode = -1

new_txt.close()
