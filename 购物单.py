'''题目描述
本题为填空题，只需要算出结果后，在代码中使用输出语句将所填结果输出即可。

小明刚刚找到工作，老板人很好，只是老板夫人很爱购物。老板忙的时候经常让小明帮忙到商场代为购物。小明很厌烦，但又不好推辞。

这不，大促销又来了！老板夫人开出了长长的购物单，都是有打折优惠的。

小明也有个怪癖，不到万不得已，从不刷卡，直接现金搞定。

现在小明很心烦，请你帮他计算一下，需要从取款机上取多少现金，才能搞定这次购物。

取款机只能提供 
100 元面额的纸币。小明想尽可能少取些现金，够用就行了。 你的任务是计算出，小明最少需要取多少现金。

以下是让人头疼的购物单，为了保护隐私，物品名称被隐藏了。'''
#解法步骤
alldatas = '''
****     180.90       88折
****      10.25       65折
****      56.14        9折
****     104.65        9折
****     100.30       88折
****     297.15        半价
****      26.75       65折
****     130.62        半价
****     240.28       58折
****     270.62        8折
****     115.87       88折
****     247.34       95折
****      73.21        9折
****     101.00        半价
****      79.54        半价
****     278.44        7折
****     199.26        半价
****      12.97        9折
****     166.30       78折
****     125.50       58折
****      84.98        9折
****     113.35       68折
****     166.57        半价
****      42.56        9折
****      81.90       95折
****     131.78        8折
****     255.89       78折
****     109.17        9折
****     146.69       68折
****     139.33       65折
****     141.16       78折
****     154.74        8折
****      59.42        8折
****      85.44       68折
****     293.70       88折
****     261.79       65折
****      11.30       88折
****     268.27       58折
****     128.29       88折
****     251.03        8折
****     208.39       75折
****     128.88       75折
****      62.06        9折
****     225.87       75折
****      12.89       75折
****      34.28       75折
****      62.16       58折
****     129.12        半价
****     218.37        半价
****     289.69        8折
'''
alldatas = alldatas.split() #用这种方法按空格取消
sum = 0
sum2 = 1
discount = []
price = []
for i in alldatas:
    sum+=1
    sum2+=1
    if sum%3==0:
        #print(i)
        discount.append(i)
    if sum2%3==0:
        price.append(i)

alldict = dict(zip(list(price),list(discount))) #创建字典
formoney = 0
for k,v in alldict.items():

    if v == '半价':
        v = 0.5
    elif v!='半价':
        v=v.split("折")[0]
        v=float('0.'+v)
    formoney+=float(k) * v

print(round(formoney/100+0.5)*100)
