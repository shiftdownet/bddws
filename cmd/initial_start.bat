cd ../

del ".\\db.sqlite3"
del ".\\accounts\\migrations\\0001_initial.py"

python manage.py makemigrations accounts

python manage.py migrate

python manage.py loaddata DeptMaster.json
python manage.py loaddata SectMaster.json
python manage.py loaddata TeamMaster.json
python manage.py loaddata WorkersPosition.json
python manage.py loaddata AuthGroups.json
python manage.py loaddata CustomUser.json

python manage.py runserver 8000

pause
