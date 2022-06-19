FROM python

RUN pip3 install requests beautifulsoup4
WORKDIR "/app"
COPY question3.py .
ENV site=http://api.open-notify.org/astros.json
ENV times=5

CMD ["python3", "question3.py"]
