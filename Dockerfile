FROM python:3
#ubuntu

RUN apt-get update
#apt install できるよう更新

#RUN apt-get update && apt-get install -y python3.9 python3.9-dev
#python3.9をインストール

COPY ./Chat /Chat
#コンテナ上にソースコードコピー

RUN pip install Flask
#flask（バックエンド）のモジュールをインストール

RUN pip install flask_cors
#flask（バックエンド）のモジュールをインストール

RUN apt-get install -y nodejs
#フロントエンドのnodeをインストール

RUN apt-get install -y npm
#フロントエンドのnodeをインストール

