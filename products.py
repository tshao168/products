products = []
while True :
	name = input ('請輸入商品名稱: ')
	if name == 'q' :
		break
	price = input ('請輸入商品價格: ') 
	price = int (price)
	# p = []
	#p.append (name)
	#p.append (price)
	# 簡寫法
	#p = [name, price]
	# 1 行寫法
	products.append ([name, price])

# print (products)
for p in products :
	print (p[0], '的價格是', p[1])
# 寫入檔案 
with open ('products.csv', 'w', encoding = 'utf-8') as f : # with 的 功能 是在程式走出with block 就會自動關檔
	f.write ('商品,價格\n')
	for p in products :
		f.write (p[0] + ',' + str(p[1]) + '\n') # 利用+號來聯結字串

