heroku login
set heroku_app_name=ryan-stock-9427
echo %heroku_app_name%
heroku git:remote -a %heroku_app_name%