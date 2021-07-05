import datetime,os,shutil

def timenow():
    now_str = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")

    return now_str

def backup():
    folder_name = str(input("folder name:"))
    time_stamp = timenow();

    zip_name = folder_name + '_' + time_stamp

    print("start backup:",folder_name)
    shutil.make_archive(zip_name,"zip",base_dir=folder_name)

if __name__ == '__main__':
    backup()
