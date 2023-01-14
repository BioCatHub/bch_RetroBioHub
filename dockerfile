# define base image

FROM python:3.7-slim
LABEL version="1.0" maintainer="Stephan Malzacher"

# set working directory in docker container

WORKDIR /app

# define environment variables
ENV FLASK_APP app.py
ENV FLASK_RUN_HOST 0.0.0.0
EXPOSE 5000

# install supporting software

COPY Requirements.txt Requirements.txt 
RUN pip3 install -r Requirements.txt

COPY . .

# start app

CMD ["flask", "run"]