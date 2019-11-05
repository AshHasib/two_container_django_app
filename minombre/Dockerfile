FROM ashhasib/codebari_img
ENV PYTHONUNBUFFERED 1
RUN mkdir /minombre
WORKDIR /minombre
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY . .
