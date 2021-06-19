import time
import aiohttp
import asyncio

async def request(url):
    print('',url)
    # 在异步协程中如果出现了同步模块相关代码，那么就无法实现异步
    # time.sleep(2)
    # 当在asyncio中遇到阻塞操作必须进行手动挂起
    await asyncio.sleep(2)

    # async with aiohttp.ClientSession() as session:
    #     async with await session.get(url) as respone:
    #         page_text=await respone.test()
    #         print(page_text)




    print('',url)
start=time.time()
urls={
    'www.baidu.com',
    'www.sougou.com',
    'www.goubanjia.com'
}
# 任务列表：存放多个任务对象
starts=[]
for url in urls:
    c=request(url)
    task=asyncio.ensure_future(c)
    starts.append(task)
loop=asyncio.get_event_loop()
# 需要将任务封装到wait中
loop.run_until_complete(asyncio.wait(starts))
print(time.time()-start)