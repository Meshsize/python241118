import os
import shutil

# 다운로드 폴더 경로
download_folder = r"C:\Users\student\Downloads"

# 파일 이동 대상 폴더
folders = {
    "images": [".jpg", ".jpeg"],
    "data": [".csv", ".xlsx"],
    "docs": [".txt", ".doc", ".pdf"],
    "archive": [".zip"],
    "execution": ['.exe']
}

# 각 폴더 생성 및 파일 이동
for folder, extensions in folders.items():
    # 폴더 경로 생성
    target_folder = os.path.join(download_folder, folder)
    if not os.path.exists(target_folder):
        os.makedirs(target_folder)
    
    # 다운로드 폴더의 파일 탐색 및 이동
    for file in os.listdir(download_folder):
        if os.path.isfile(os.path.join(download_folder, file)):
            # 파일 확장자 검사 및 이동
            if any(file.lower().endswith(ext) for ext in extensions):
                shutil.move(os.path.join(download_folder, file), target_folder)
                print(f"{file} -> {target_folder}")
