# 輸入秒數
x = input('please input seconds:')
x = int(x)
# 計算小時數
a = x % 3600
l = (x-a)/3600
# 計算分鐘數
b = a % 60
m = (a-b)/60
# 輸出時間
print(l,'hours',m,'minutes',b,'seconds')