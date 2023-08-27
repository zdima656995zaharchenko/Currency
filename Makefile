run:
	python app/manage.py runserver

migrate:
	python app/manage.py migrate

makemigrations:
	python app/manage.py makemigratiions

shell:
	python app/manage.py shell_plus --print-sql


