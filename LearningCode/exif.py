import os
from PIL import Image

def remove_exif(image_path, output_path):
    with Image.open(image_path) as image:
        # EXIF 속성 삭제
        image_without_exif = Image.new(image.mode, image.size)
        image_without_exif.putdata(list(image.getdata()))

        # 이미지 저장
        image_without_exif.save(output_path)

# 이미지가 있는 폴더 경로
folder_path = r"C:\Users\user\Desktop\backup\body"

# 폴더 내의 모든 파일에 대해 처리
for file_name in os.listdir(folder_path):
    # 파일 경로 생성
    file_path = os.path.join(folder_path, file_name)

    # 파일의 확장자가 .jpg 또는 .jpeg 인지 확인
    if file_path.lower().endswith((".jpg", ".jpeg",".png")):
        # 이미지 파일의 EXIF 속성 삭제하여 새로운 파일로 저장
        output_path = os.path.join(folder_path, "no_exif", file_name)
        os.makedirs(os.path.dirname(output_path), exist_ok=True)  # 저장할 폴더가 없으면 생성
        remove_exif(file_path, output_path)


print("fin")
