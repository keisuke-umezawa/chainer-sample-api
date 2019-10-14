# chainer-sample-api

## Contents
If you upload an image file, the server classify the image from 0 to 9 digits.
In the server, the model which is trained by mnist dataset is used.

## Procedure
1. Upload an image file
2. Chainer model classify the image from 0 to 9 digits.
3. Return the digit.

## How to use?
1. Install docker, make and docker-compose.

2. Type following commands.
```
$ git clone https://github.com/keisuke-umezawa/chainer-sample-api.git
$ cd chainer-sample-api
$ make build run
```

3. Access to `localhost:8080`.

