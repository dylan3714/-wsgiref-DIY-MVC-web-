import datetime
import webauth
from urllib.parse import parse_qs

def login(environ):
    with open('templates/web.html', 'rb') as f:
        data = f.read()
    return data

def auth(environ):
    # 登陆认证
    # 1.获取用户输入的用户名和密码

    # 2.去数据库做数据的校验，查看用户提交的是否合法
    # user_information = environ['']
    if environ.get("REQUEST_METHOD") == "POST":
        # 获取请求体数据的长度,因为提交过来的数据需要用它来提取,注意POST请求和GET请求的获取数据的方式不同
        try:
            request_body_size = int(environ.get('CONTENT_LENGTH', 0))
        except (ValueError):
            request_body_size = 0
        # POST请求获取数据的方式
        request_data = environ['wsgi.input'].read(request_body_size)
        print('>>>>>', request_data)  # >>>>> b'username=chao&password=123'，是个bytes类型数据
        print('?????', environ['QUERY_STRING'])  # ????? 空的，因为post请求只能按照上面这种方式取数据
        # parse_qs可以帮我们解析数据
        re_data = parse_qs(request_data)
        print('拆解后的数据', re_data)  # 拆解后的数据 {b'password': [b'123'], b'username': [b'chao']}
        #post请求的返回数据我就不写啦
        pass
    if environ.get("REQUEST_METHOD") == "GET":
        # GET请求获取数据的方式，只能按照这种方式取
        print('?????', environ['QUERY_STRING'])  # ????? username=chao&password=123,是个字符串类型数据
        request_data = environ['QUERY_STRING']

        # parse_qs可以帮我们解析数据
        re_data = parse_qs(request_data)
        print('拆解后的数据', re_data)  # 拆解后的数据 {'password': ['123'], 'username': ['chao']}
        username = re_data['username'][0]
        password = re_data['password'][0]
        print(username, password)
        # 进行验证：
        status = webauth.auth(username, password)
        if status:
            # 3.将相应内容返回
            with open('templates/websuccess.html', 'rb') as f:
                data = f.read()
        else:
            data = b'auth error'
    return data

def favicon(environ):
    with open('wechat.ico','rb') as f:
        data = f.read()
    return data

def index(environ):
    with open('templates/index.html','rb') as f:
        data = f.read()
    return data

#查看当前时间的
def timer(environ):
    data = str(datetime.datetime.now()).encode('utf-8')
    return data
