python -m venv venv
source venv/Scripts/activate
pip freeze > requirements.txt
pip install -r requirements.txt
python manage.py dumpdata <app_name><model_name>(model name은 소문자!) > movies.json

fixtures/movies/movies.json

python manage.py loaddata <file> ex. movies/movies.json

모델링 하는게 제일 중요!