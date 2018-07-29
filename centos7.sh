# python3安装
yum -y groupinstall "Development tools"
yum -y install zlib-devel bzip2-devel openssl-devel ncurses-devel sqlite-devel readline-devel tk-devel gdbm-devel db4-devel libpcap-devel xz-devel
yum -y install libffi-devel
cd /tmp/
mkdir /usr/local/python3
wget https://www.python.org/ftp/python/3.7.0/Python-3.7.0.tar.xz
tar -xvJf  Python-3.7.0.tar.xz
cd Python-3.7.0
./configure --prefix=/usr/local/python3 --enable-optimizations
make && make install

ln -s /usr/local/python3/bin/python3 /usr/bin/python3
ln -s /usr/local/python3/bin/pip3 /usr/bin/pip3

# pip源配置
mkdir ~/.pip/
cat <<EOF >> ~/.pip/pip.conf
[global]
index-url = http://mirrors.aliyun.com/pypi/simple/

[install]
trusted-host=mirrors.aliyun.com
EOF
# 虚拟环境
pip3 install virtualenv
pip3 install virtualenvwrapper
# 配置虚拟环境
cat <<"EOF" >> /etc/profile
export PATH=/usr/local/python3/bin/:$PATH
export WORKON_HOME=$HOME/.virtualenvs
export VIRTUALENVWRAPPER_PYTHON=/usr/bin/python3
source /usr/local/python3/bin/virtualenvwrapper.sh
EOF
source /etc/profile


# 基础工具服务安装
yum -y install vim
yum -y install mariadb mariadb-devel mariadb-server
yum -y install memcached

cd /tmp
wget http://nginx.org/download/nginx-1.14.0.tar.gz
tar zxvf nginx-1.14.0.tar.gz
cd nginx-1.14.0
./configure --prefix=/usr/local/nginx --with-stream
make
make install
# 添加代理配置目录
mkdir /usr/local/nginx/conf/tcp.d/


# python2 pip安装
cd /tmp
curl -O https://bootstrap.pypa.io/get-pip.py
python get-pip.py
pip install  --upgrade pip
# 配置supervisor 
pip install supervisor
cd /tmp
echo_supervisord_conf > supervisord.conf
cat <<EOF >> supervisord.conf
[include]
files = /etc/supervisord.d/*.conf
EOF
mv supervisord.conf /etc/
mkdir /etc/supervisord.d/
# 启动supervisor
supervisord -c /etc/supervisord.conf




mysql -e "
CREATE USER 'album'@'%' IDENTIFIED BY 'album';
CREATE USER 'album'@'localhost' IDENTIFIED BY 'album';
CREATE DATABASE album DEFAULT CHARACTER SET utf8 COLLATE utf8_general_ci;
GRANT ALL PRIVILEGES ON album.* TO 'album'@'%';
GRANT ALL PRIVILEGES ON album.* TO 'album'@'localhost';
"