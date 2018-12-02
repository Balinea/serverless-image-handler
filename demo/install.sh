#!/bin/bash

echo "virtualenv --no-site-packages env"
virtualenv --no-site-packages env
echo "source env/bin/activate"
source env/bin/activate

echo "copying img libs into $VIRTUAL_ENV"
cp -f /usr/bin/jpegtran $VIRTUAL_ENV
cp -f /usr/bin/optipng $VIRTUAL_ENV
cp -f /usr/bin/pngcrush $VIRTUAL_ENV
cp -f /usr/bin/gifsicle $VIRTUAL_ENV
cp -f /usr/bin/pngquant $VIRTUAL_ENV
cp -f /usr/lib64/libimagequant.so* $VIRTUAL_ENV/bin/lib

export PYCURL_SSL_LIBRARY=nss

python -m pip install --upgrade pip==9.0.3

pip install -r requirements.txt
