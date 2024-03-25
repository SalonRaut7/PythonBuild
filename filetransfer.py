import os,shutil
types = [".mp4",".jpg", ".jpeg",".docx", ".m4a", ".mp3"]
folder_path = r'D:\\collection'
for filename in os.listdir(folder_path):
    src = os.path.join(folder_path, filename)
    if os.path.isfile(src):
        root, extension = os.path.splitext(filename)
        if extension in types:
            if extension == ".mp4":
                dst = r'D:\\python_videos'
            elif extension == ".docx":
                dst = r'D:\\python_docs'
            elif extension == ".jpg" or extension == ".jpeg":
                dst = r'D:\\python_image'
            elif extension == ".m4a" or extension == ".mp3":
                dst = r'D:\\python_music'
            else:
                dst = r'D:\\other_files'
            shutil.move(src, dst)