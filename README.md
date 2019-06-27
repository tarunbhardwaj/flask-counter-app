# Flask Counter App

RUN

```sh
docker run -d -p 5000:5000 -e REDIS_URL='redis://redis-host:6379/0' --name counter_app tarunbhardwaj/flask-counter-app
```

