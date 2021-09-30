#!/bin/bash
echo -e "app name insert"
read appname
python manage.py makemigrations ${appname}

echo "--- migrate 실행합니데이 ---"
python manage.py migrate ${appname}
