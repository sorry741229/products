#讀取檔案
products = []
with open ('products.csv', 'r') as f:
	for line in f:
		if '商品,價格' in line:
			continue #繼續，跳到下一個
		name, price = line.strip().split(',')
		products.append([name, price])
print(products)

#讓使用者輸入
while True:
    name = input('請輸入商品名稱 :')
    if name == 'q': #逃出迴圈
        break
    price = input('請輸入商品價格 :')
    p = []
    p.append(name)
    p.append(price)
    # p = [name , price] 簡化上面三行
    products.append(p)
    # prducts.append([name, price]) 簡化上面四行
print(products)

#印出所有購買紀錄
for p in products:
	print(p[0],'的價格是', p[1])
#寫入檔案
with open ('products.csv', 'w') as f:
	f.write('商品,價格\n')
	for p in products:
		f.write(p[0]+ ',' + p[1] + '\n')