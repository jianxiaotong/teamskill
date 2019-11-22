#基础镜像
FROM python:3.7
#设置代码工作目录
WORKDIR /app
#复制代码到容器
ADD . /app
#安装所需包
RUN pip install -r requirements.txt \
    && python manage.py makemigrations \
    && python manage.py migrate
    
CMD python manage.py runserver 0.0.0.0:8000
