1. автоматическая генерация requirements.txt:  pip freeze > requirements.txt 
2. dev создание образа: docker build -t mailer:latest .
3. dev запуск контейнера: docker run --name mailer -p 5000:5000 mailer:latest
4. prod отправка контейнера контейнера: heroku container:push web
5. prod запуск удаленного контейнера: heroku container:release web
6. обновление git remote: heroku git:remote -a mailer24
