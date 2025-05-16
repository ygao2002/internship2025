#记录图像元数据
from PIL import Image
from PIL.ExifTags import TAGS
import os
import csv


def extract_metadata(image_path):
    metadata = {}
    try:
        with Image.open(image_path) as img:
            info = img._getexif()
            if info:
                for tag, value in info.items():
                    decoded = TAGS.get(tag, tag)
                    metadata[decoded] = value
    except Exception as e:
        print(f"无法提取元数据: {image_path}，原因: {e}")
    return metadata

def save_metadata_to_csv(image_dir, output_csv):
    with open(output_csv, 'w', newline='', encoding='utf-8-sig') as csvfile:
        fieldnames = ['文件路径', '拍摄时间', '场景描述']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        for root, _, files in os.walk(image_dir):
            for file in files:
                filepath = os.path.join(root, file)
                metadata = extract_metadata(filepath)
                capture_time = metadata.get('DateTime', '未知')
                scene_description = '交通场景'  # 根据实际情况填写
                writer.writerow({
                    '文件路径': filepath,
                    '拍摄时间': capture_time,
                    '场景描述': scene_description
                })

image_directory = 'C:/Users/0916g/OneDrive/Desktop/siemens_intern/val2017'
output_csv_path = 'C:/Users/0916g/OneDrive/Desktop/siemens_intern/data/raw/original_data.csv'
save_metadata_to_csv(image_directory, output_csv_path)
