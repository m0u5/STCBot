FROM python:3.11
COPY ./requirements.txt /STCbot/requirements.txt
WORKDIR /STCbot
RUN pip install -r requirements.txt
COPY . /STCbot
CMD ["sh", "-c", "python main.py"]