FROM python:3
ADD task9.py /
ADD requirements.txt /
ADD data.csv / 
RUN pip install -r requirements.txt
CMD [ "python", "./task9.py" ]