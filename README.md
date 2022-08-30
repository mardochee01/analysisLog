# Analyse de fichier log

## log file analyzed
```
"POST /loger/api/v1/log/HTTP/1.1" 201
"POST /loger/api/v1/log/HTTP/1.1" 201
"POST /loger/api/v1/log/HTTP/1.1" 201
"POST /loger/api/v1/log/HTTP/1.1" 500
"POST /loger/api/v1/log/HTTP/1.1" 500
"POST /loger/api/v1/log/HTTP/1.1" 201
...

```



## Result in JSON format
```

$ python3 $ analyselog.py

{
    "request": "POST",
    "URL": "/loger/api/v1/log/HTTP/1.1",
    "status": "201"
}
{
    "request": "POST",
    "URL": "/loger/api/v1/log/HTTP/1.1",
    "status": "201"
}
{
    "request": "POST",
    "URL": "/loger/api/v1/log/HTTP/1.1",
    "status": "201"
}
{
    "request": "POST",
    "URL": "/loger/api/v1/log/HTTP/1.1",
    "status": "500"
}
{
    "request": "POST",
    "URL": "/loger/api/v1/log/HTTP/1.1",
    "status": "500"
}
{
    "request": "POST",
    "URL": "/loger/api/v1/log/HTTP/1.1",
    "status": "201"
}
{
    "request": "..."
}
```
## why json format

We can perform any other operation on it. 
For example :
* store in a database for future analysis.
* import NumPy and Matplotlib and draw graphs to understand the information graphically. 
