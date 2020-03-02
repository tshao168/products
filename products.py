import os # operating system
products = []
if  os.path.isfile ('products.csv') : #檢查檔案在不在
	print ('檔案存在')
	with open ('products.CSV', 'r') as f:
		for line in f:
			if '商品,價格' in line :
				continue # 跳過這一次的迴1圈,進行下一迴
			name, price = line.strip().split(',') # 先把換行\n符號處理掉再分割
			products.append ([name, price])
	print (products)

else :
	print ('檔案不在')
#使用者輸入
while True :
	name = input ('請輸入商品名稱: ')
	if name == 'q' :
		break
	price = input ('請輸入商品價格: ') 
	price = int (price)
	products.append ([name, price])

# print (products)
#印出購買記錄
for p in products :
	print (p[0], '的價格是', p[1])
# 寫入檔案 
with open ('products.csv', 'w') as f : # with 的 功能 是在程式走出with block 就會自動關檔
	f.write ('商品,價格\n')
	for p in products :
		f.write (p[0] + ',' + str(p[1]) + '\n') # 利用+號來聯結字串

