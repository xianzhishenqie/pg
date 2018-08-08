# 配置ningx
touch /usr/local/nginx/conf/pg.conf
cat <<"EOF" > /usr/local/nginx/conf/pg.conf
#user  nobody;
daemon off;
worker_processes  4;
events {
    worker_connections  1024;
}

stream {
    include tcp.d/*.conf;
}

http {
    include       mime.types;
    default_type  application/octet-stream;
    log_format  main  '$remote_addr - $remote_user [$time_local] "$request" '
                      '$status $body_bytes_sent "$http_referer" '
                      '"$http_user_agent" "$http_x_forwarded_for"';
    sendfile        on;
    keepalive_timeout  65;
    server {
        listen       80;
        charset utf-8;
        access_log  logs/host.access.log  main;
        location /static {alias /home/pg/static/;}
        location /media {alias /home/pg/media/;}
        location / {
            client_max_body_size    100m;
            proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
            proxy_set_header Host $http_host;
            proxy_redirect off;
            proxy_pass http://127.0.0.1:8077;
        }

        error_page   500 502 503 504  /50x.html;
        location = /50x.html {root   html; }
    }
}
EOF
