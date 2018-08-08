# 配置nginx, memcached
touch /etc/supervisord.d/service.conf
cat <<"EOF" > /etc/supervisord.d/service.conf
[program:nginx]
command=/usr/local/nginx/sbin/nginx -c /usr/local/nginx/conf/pg.conf
autostart=true
autorestart=true
user=root

[program:memcached]
command=memcached -uroot -l127.0.0.1
autostart=true
autorestart=true
user=root
EOF


# 配置pg supervisor
touch /etc/supervisord.d/pg.conf
cat <<"EOF" > /etc/supervisord.d/pg.conf
[program:pg]
command=/root/.virtualenvs/pg/bin/gunicorn pg.wsgi -c gunicorn_config.py
directory=/home/pg/
autostart=true
autorestart=true
user=root
EOF
