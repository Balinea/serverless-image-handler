FROM amazonlinux:2017.03.1.20170812

 # lock yum to the same repository version
RUN sed -i 's/releasever=.*/releasever=2017.03/g' /etc/yum.conf

# see https://github.com/awslabs/serverless-image-handler
RUN yum update -y && \
    yum -y install make && yum -y install which && \
    yum install yum-utils epel-release -y && yum clean all && \
    yum-config-manager --enable epel && yum install -y python-pip && yum clean all && \
    yum install zip wget git libpng-devel libcurl-devel gcc python27-devel libjpeg-devel -y

# ImageMagick
RUN yum install -y ImageMagick-devel openssl-devel

# Other libraries
RUN yum install -y pngcrush libjpeg* gifsicle

# optipng
RUN wget http://dl.fedoraproject.org/pub/epel/6/x86_64/Packages/o/optipng-0.7.6-6.el6.x86_64.rpm && \
    yum localinstall optipng-0.7.6-6.el6.x86_64.rpm -y && rm optipng*rpm

# pngquant
RUN wget http://dl.fedoraproject.org/pub/epel/6/x86_64/Packages/l/libimagequant-2.5.2-5.el6.x86_64.rpm && \
    yum localinstall libimagequant-2.5.2-5.el6.x86_64.rpm -y && rm libimagequant*rpm && \
    wget http://dl.fedoraproject.org/pub/epel/6/x86_64/Packages/p/pngquant-2.5.2-5.el6.x86_64.rpm && \
    yum localinstall pngquant-2.5.2-5.el6.x86_64.rpm -y && rm pngquant*rpm

RUN alias sudo='env PATH=$PATH' && \
    curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py && \
    python get-pip.py && rm get-pip.py && \
    pip install setuptools==39.0.1 && \
    pip install virtualenv==15.2.0 && \
    pip install awscli --upgrade --user

ENV PATH "$PATH:~/.local/bin:$PATH"

