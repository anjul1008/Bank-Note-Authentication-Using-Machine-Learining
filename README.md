# Authenticate Bank Notes Using Machine Learning 💵💳


## 📌 Introduction

This Machine Learning Web Application uses a several features of Banknotes like variance, skewness, curtosis and entropy to predict the Authenticy of Banknotes weither it is Genuine or Forged with an accuracy of 99.02% using Random Forest Classifier.This Dataset is taken from UCI Repository and also available in Kaggle,Data were extracted from images that were taken from genuine and forged banknote-like specimens. For digitization, an industrial camera usually used for print inspection was used. The final images have 400x 400 pixels. Due to the object lens and distance to the investigated object gray-scale pictures with a resolution of about 660 dpi were gained. Wavelet Transform tool were used to extract features from images,***In this ml model we are considering 0 for geniune bank note and 1 for forged bank note.***

## 🎯 Purpose of the Project

Whether we pull out paper bills or swipe a credit card, most of the transactions we engage in daily use currency. Indeed, money is the lifeblood of economies around the world. Currency refers to paper money or coins that are in circulation. But currency is actually only a small piece of the monetary economy and just one consideration when looking at the total money supply.

Indeed, most money today exists as credit money or as electronic records stored in databases in banks or financial institutions. But still, the bread and butter of everyday transactions is currency, and that is what we will look more closely at here.

### Why Bank Notes Genuinity is Important 💵?
As now a days many transactions take place using plastic money , But Bank Notes and Coins are still is in the use and used by more than 56% of Indians as surveyed in 2019 and the major transactions from buying daily households to spending money in various places to buy things in small commodities shop to Barber Shops and Groceries are taken place in notes and if the notes used by people of the country are forged or duplicate this will leads to unstable economy and rise of crimes in country with illegal transactions, so we need to autheticate notes so that it can leads to stable economy and leads towards a well development of country.

Our Model performs fairly well with an accuracy of 99% and an F1 Score of 95% and Recall Score of 92% as we have used Bagging Technique which is Random Forest Classifier with Sklearn library. This provides a handy tool to utilize the power of Machine Learning and Artificial Intelligence in Binary Classification Problems where time and accuracy is the paramount objective of classification.

## 🏁 Technology Stack


* [SkLearn](https://scikit-learn.org/)
* [Flask](https://github.com/pallets/flask)
* [Swagger UI](https://swagger.io/tools/swagger-ui/)
* [Docker](https://www.docker.com/)

## 🏃‍♂️ Local Installation

1. Drop a ⭐ on the Github Repository. 
2. Clone the Repo by going to your local Git Client and pushing in the command: 

```sh
https://github.com/anjul1008/Bank-Note-Authentication-Using-Machine-Learining.git
```
3. Install the Packages: 
```sh
pip install -r requirements.txt
```
You need to install flask seperatly with a latest version to run the flask app in Postman.

## Dockerize your Application

1.Use **Dockerfile** to create a Docker Image.

```sh
FROM ubuntu:16.04

RUN apt-get update && \
    apt-get install -y --no-install-recommends \
        g++ \
        bzip2 \
        unzip \
        make \
        wget \
        git \
        python3 \
        python3-dev \
        python3-websockets \
        python3-setuptools \
        python3-pip \
        python3-wheel \
        zlib1g-dev \
        patch \
        ca-certificates \
        swig \
        cmake \
        xz-utils \
        automake \
        autoconf \
        libtool \
        pkg-config 

COPY . /app/server/.

WORKDIR /app/server

RUN pip3 install -r req.txt

CMD python3 app_flasgger.py

```

2.Build the Docker Image

`docker build -t {Name_of_your_Image}`

3.Run your Docker Image

`docker run -p 5000:5000 bank_auth`

**Note**: bank_auth is a docker image name, you can name it anything!!

Now your Docker Container is running at ` http://127.0.0.1:5000/docs` and this is the Swagger UI.

