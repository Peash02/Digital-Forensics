import os
import shutil
import hashlib
import csv
from datetime import datetime

source_folder = "Evidence_Source"
dest_folder = "Collected_Evidence"

os.makedirs(dest_folder,exist_ok = True)

report_file = "evidence_report.csv"

def calculate_hash(file_path):
    sha256 = hashlib.sha256()
    with open(file_path,"rb") as file:
        while True:
            data = file.read(4096)
            if not data:
                break
            sha256.update(data)
    return sha256.hexdigest()

with open(report_file,"w",newline="") as csvfile :
    writer = csv.writer(csvfile)

    writer.writerow([
        "File Name",
        "File Size",
        "Modified Time",
        "SHA-256 Hash"
    ])
    for file_name in os.listdir(source_folder):
        source_path = os.path.join(source_folder,file_name)

        if os.path.isfile(source_path):
            destination_path = os.path.join(
                dest_folder,
                file_name
            )

            shutil.copy2(source_path,destination_path)

            file_size = os.path.getsize(source_path)

            modiified_time = datetime.fromtimestamp(
                os.path.getmtime(source_path)
            )

            file_hash = calculate_hash(source_path)
            writer.writerow([
                file_name,
                file_size,
                modiified_time,
                file_hash
            ])

            print("Collected:",file_name)

print("\n Digital Evidence collection completed.")
print("Evidence Saved in:",dest_folder)
print("Report Saved as : ",report_file)