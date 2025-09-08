FROM 

WORKDIR /app
COPY . .
RUN pip install -r requirements.txt

CMD ["pytest"]