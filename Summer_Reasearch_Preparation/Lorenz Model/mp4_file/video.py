from PIL import Image, ImageDraw
import imageio

# 設置GIF圖像的大小和背景色
size = (200, 200)
background_color = (255, 255, 255)

# 創建一個新的Pillow圖像對象
im = Image.new('RGB', size, background_color)

# 在圖像上繪製一些形狀
draw = ImageDraw.Draw(im)
draw.rectangle((50, 50, 150, 150), fill=(255, 0, 0))
draw.ellipse((75, 75, 125, 125), fill=(0, 0, 255))

# 保存第一幀圖像
im.save('frame0.png')

# 創建一個圖像列表，其中包含每一幀圖像
frames = []
frames.append(im)

# 創建一個動畫，其中包含所有幀圖像
for i in range(1, 5):
    # 創建新的幀圖像
    im = Image.new('RGB', size, background_color)
    draw = ImageDraw.Draw(im)
    draw.rectangle((50+i*10, 50+i*10, 150-i*10, 150-i*10), fill=(255-i*20, 0, i*20))
    draw.ellipse((75+i*10, 75+i*10, 125-i*10, 125-i*10), fill=(0, i*20, 255-i*20))
    # 將幀圖像添加到圖像列表中
    frames.append(im)
    # 保存幀圖像
    im.save(f'frame{i}.png')

# 使用imageio模塊將圖像列表保存為GIF圖像
imageio.mimsave('animation.gif', frames, duration=0.2)
