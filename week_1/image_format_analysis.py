#分析图片数据格式
import os
import cv2
import csv


def analyze_image_format(image_dir, output_csv):
    # 打开 CSV 文件以写入数据
    with open(output_csv, 'w', newline='', encoding='utf-8-sig') as csvfile:
        fieldnames = ['文件名', '分辨率', '颜色模式', '文件类型']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()

        # 遍历指定目录下的所有文件
        for root, _, files in os.walk(image_dir):
            for file in files:
                filepath = os.path.join(root, file)
                img = cv2.imread(filepath)
                if img is not None:
                    height, width, channels = img.shape
                    color_mode = '灰度' if channels == 1 else 'RGB'
                    file_type = os.path.splitext(file)[1].lower()
                    writer.writerow({
                        '文件名': file,
                        '分辨率': f'{width}x{height}',
                        '颜色模式': color_mode,
                        '文件类型': file_type
                    })
                else:
                    print(f"无法读取图像: {filepath}")

image_directory = 'C:/Users/0916g/OneDrive/Desktop/siemens_intern/val2017'
output_csv_path = 'C:/Users/0916g/OneDrive/Desktop/siemens_intern/data/raw/format_data.csv'
analyze_image_format(image_directory, output_csv_path)