FROM python:3.7-slim

LABEL version="1.0" maintainer="Stephan Malzacher"


WORKDIR /app

ENV FLASK_APP app.py

ENV FLASK_RUN_HOST 0.0.0.0
EXPOSE 5000
#ENV FLASK_RUN_PORT 5050

COPY Requirements.txt Requirements.txt 
RUN pip3 install -r Requirements.txt


COPY . .

#CMD [ "python3", "-m" , "flask", "run", "--host=0.0.0.0"]
#CMD [ "flask", "run"]

CMD ["flask", "run"]