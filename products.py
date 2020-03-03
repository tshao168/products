import os # operating system

#讀取檔案
def read_file (filename) :
	products = []
	if  os.path.isfile (filename) : #檢查檔案在不在
		print ('檔案存在')
		with open (filename, 'r') as f:
			for line in f:
				if '商品,價格' in line :
					continue # 跳過這一次的迴1圈,進行下一迴
				name, price = line.strip().split(',') # 先把換行\n符號處理掉再分割
				products.append ([name, price])
		print (products)

	else :
		print ('檔案不在')
	return products

#使用者輸入

def user_input(products):
	while True :
		name = input ('請輸入商品名稱: ')
		if name == 'q' :
			break
		price = input ('請輸入商品價格: ') 
		price = int (price)
		products.append ([name, price])
	return products

# print (products)
#印出購買記錄
def print_products(products) :
	for p in products :
		print (p[0], '的價格是', p[1])
# 寫入檔案 
def write_file(filename,products):
	with open (filename, 'w') as f : # with 的 功能 是在程式走出with block 就會自動關檔
		f.write ('商品,價格\n')
		for p in products :
			f.write (p[0] + ',' + str(p[1]) + '\n') # 利用+號來聯結字串

products = read_file('products.csv')
products = user_input(products)
print_products(products)
write_file('products.csv',products)
