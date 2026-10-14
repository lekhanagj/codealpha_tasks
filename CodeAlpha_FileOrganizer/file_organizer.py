import os
import shutil

folder = input("Enter the folder path: ")

jpg_folder = os.path.join(folder, "JPG_Files")

if not os.path.exists(jpg_folder):
    os.mkdir(jpg_folder)

for file in os.listdir(folder):
    if file.lower().endswith(".jpg"):
        source = os.path.join(folder, file)
        destination = os.path.join(jpg_folder, file)
        shutil.move(source, destination)

print("All JPG files have been moved successfully!")