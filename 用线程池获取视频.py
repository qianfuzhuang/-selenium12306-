import time
from multiprocessing.dummy import Pool

def get_page(str):
    print("正在下载",str)
    time.sleep(2)
    print("下载完成",str)
name_list=['aaa','bbbb','cccc','dddd']
pool=Pool(4)
pool.map(get_page,name_list)




