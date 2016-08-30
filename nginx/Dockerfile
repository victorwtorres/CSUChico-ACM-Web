FROM tutum/nginx
RUN rm /etc/nginx/sites-enabled/default
ADD sites-enabled/ /etc/nginx/sites-enabled
RUN mkdir -p /etc/letsencrypt/live/
ADD live/ /etc/letsencrypt/live

