FROM ubuntu

WORKDIR /app

COPY package*.py ./

RUN pip install

COPY . .

ENV PORT=8080

EXPOSE 8080

CMD  
