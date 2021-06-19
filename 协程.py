import asyncio
async def request(url):
    print('正在请求的url的是',url)
    print('请求成功',url)
    # async修饰的函数、调用之后返回的一个协程对象
c=request('www.baidu.com')

# # 创建一个事件循环对象
# loop=asyncio.get_event_loop()
# # 将协程对象注册到loop中，然后启动loop
# loop.run_until_complete(c)

# task使用
loop=asyncio.get_event_loop()
task=loop.create_task(c)
print(task)
loop.run_until_complete(task)
print(task)