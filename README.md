# Some SQLi Lab 2

Blacklist-based SQLi protection bypass lab 2 (harder than some-sqli-lab 1 a little bit)

## Let Play

> Please finish [Some Sqli Lab](https://github.com/suam-team/some-sqli-lab) before hacking this lab.

Please find a bud in the [app.py](/app.py) file. Then, hack this lab on your own environment. Next, get a real flag [https://some-sqli-lab-2.herokuapp.com/](https://some-sqli-lab-2.herokuapp.com/). Finally, submit flag on [https://lab.suam.wtf/](https://lab.suam.wtf/).

## Running Locally

Make sure you have Docker [installed locally](https://docs.docker.com/get-docker/).

```sh
$ git clone https://github.com/suam-team/some-sqli-lab-2.git
$ cd some-sqli-lab-2
$ docker build -t some-sqli-lab-2 .
$ docker run -p 5000:1337 -d -e PORT=1337 -e FLAG=flag{IloveYou} --rm some-sqli-lab-2
```

Your app should now be running on [localhost:5000](http://localhost:5000/).

## Deploying to Heroku

```sh
$ heroku create
$ git push heroku main
$ heroku open
```
or

[![Deploy](https://www.herokucdn.com/deploy/button.svg)](https://heroku.com/deploy)