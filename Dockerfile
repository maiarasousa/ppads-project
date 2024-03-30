FROM python:3.12-bullseye

WORKDIR /app

# Required for msodbcsql17 and mssql-tools
RUN curl https://packages.microsoft.com/keys/microsoft.asc | apt-key add -
RUN curl https://packages.microsoft.com/config/debian/11/prod.list > /etc/apt/sources.list.d/mssql-release.list
RUN apt-get update

RUN ACCEPT_EULA=Y apt-get install -y msodbcsql18 mssql-tools18
RUN apt-get install unixodbc-dev
RUN pip3 install --upgrade pyodbc

COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt

COPY . .

EXPOSE 5000

ENV FLASK_APP=app.py

CMD ["flask", "run", "--host", "0.0.0.0"]