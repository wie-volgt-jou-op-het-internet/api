FROM python
COPY requirements.txt /
RUN pip install -r requirements.txt gunicorn
COPY api.py wsgi.py /
CMD gunicorn --bind 0.0.0.0:9000 --workers=8 wsgi:app
