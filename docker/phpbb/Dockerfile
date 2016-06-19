FROM php:7-apache
RUN apt-get update && apt-get install -y php5-mysql mysql-client imagemagick
RUN docker-php-ext-install -j$(nproc) mysqli
