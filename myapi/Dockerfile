FROM ashhasib/codebari_img
ENV PYTHONUNBUFFERED 1
RUN mkdir /myapi
WORKDIR /myapi
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY . .
