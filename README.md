ganymede-notificator is a web app that send email nofication, this app is developed for the ganymede project, but more work will be done to made it a standalone app that can push email notification for any use case

```
SENDER_EMAIL_ADDRESS=sender@gmail.com
SMTP_APP_PASSWORD=some app password
```

```Bash
docker run -p 8000:8000 -v $(pwd)/:/app --env-file .env -t ganymede-notificator
```
