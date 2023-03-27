import os
import imageio.v2 as imageio

# 設置文件路徑和文件名
folder_path = r'C:\Users\joe51\OneDrive\桌面\profile_ntu\Summer_Reasearch_Preparation\Lorenz Model\dfi_init_z'
file_name = "lorenz_dif_z.gif"

# 獲取文件夾中所有圖像的文件名
file_names = sorted((fn for fn in os.listdir(folder_path) if fn.endswith('.png')))

# 使用imageio庫將圖像讀取到內存中
images = [imageio.imread(os.path.join(folder_path, file_name)) for file_name in file_names]

# 使用imageio庫創建GIF
imageio.mimsave(os.path.join(folder_path, file_name), images, fps=3)
