# THUMBOR DEMO

Thumbor demo using image handler conf.

### INSTALLATION

```bash
docker-compose run demo bash -c "./install.sh"
```

### START THE SERVER
```bash
docker-compose run -p 18888:8888 demo bash -c "./run.sh"
```
now the demo is available at http://localhost:18888

### Examples

http://localhost:18888/unsafe/800x600/jeju-do.jpg
http://localhost:18888/unsafe/800x600/smart/jeju-do.jpg
http://localhost:18888/unsafe/meta/800x600/jeju-do.jpg
http://localhost:18888/unsafe/600x600/smart/filters:watermark(watermark.jpg,0,-0,20)/jeju-do.jpg
http://localhost:18888/unsafe/600x600/filters:watermark(watermark.jpg,0,-0,20,10,0)/jeju-do.jpg

