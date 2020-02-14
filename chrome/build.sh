heroku container:push web -a chrome-selenium
heroku container:release web -a chrome-selenium
# heroku ps:scale web=1 chrome=0 -a chrome-selenium
heroku logs -t -a chrome-selenium