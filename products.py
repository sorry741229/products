products = []
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

for p in products:
	print(p[0],'的價格是', p[1])

with open ('products.csv', 'w') as f:
	f.write('商品,價格\n')
	for p in products:
		f.write(p[0]+ ',' + p[1] + '\n')