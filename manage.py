from urls import urlpatterns
from wsgiref.simple_server import make_server


#这个文件里面是框架的主体内容
def application(environ, start_response):
    start_response('200 OK', [('Content-Type', 'text/html')])
    path = environ['PATH_INFO']
    for url_tuple in urlpatterns:
        if url_tuple[0] == path:
            data = url_tuple[1](environ) #environ要传进去，因为处理逻辑里面可能要用
            break
        else:
            data = b'sorry 404!,not found the page'
    return [data]
        #注意昂，我们如果直接返回中文，没有给浏览器指定编码格式，默认是gbk，所以我们需要gbk来编码一下，浏览器才能识别
        # data='登陆成功！'.encode('gbk')



#和咱们学的socketserver那个模块很像啊
httpd = make_server('127.0.0.1', 8080, application)

print('Serving HTTP on port 8080...')
# 开始监听HTTP请求:
httpd.serve_forever()

#整个框架写好了，那么我们将来想添加一些新的功能，比如说有人想在网址里面输入http://127.0.0.1:8080/timer 来查看当前时间，你只需要两步，写一个url映射关系，写一个应对的处理函数就搞定了，有了框架就不需要你在重新写一遍这所有的逻辑了，简单两步搞定新功能

