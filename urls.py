from views import login,auth,favicon,index,timer

#url与视图函数的对应关系
urlpatterns=[
    ('/login',login),
    ('/auth/',auth),
    ('/favicon.ico',favicon),
    ('/',index),
    ('/timer',timer),

]