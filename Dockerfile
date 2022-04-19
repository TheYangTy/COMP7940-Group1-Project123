FROM python
COPY main.py /
COPY bot.py /
COPY responses.py /
COPY config.ini /
COPY requirements.txt /
RUN pip install pyrebase4
RUN pip install update
RUN pip install urllib3
RUN pip install uplink
RUN pip install pyrebase-t
RUN pip install pycryptodome
RUN pip install -r requirements.txt
ENV PYTHONUNBUFFERED True
ENTRYPOINT ["python"]
CMD exec gunicorn --bind :$PORT --workers 1 --threads 8 --timeout 0 main:app
