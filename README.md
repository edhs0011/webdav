# Upload file with WebDAV
#
### 1. Start a locol WebDAV server
***
#
#### Pull docker image
```
docker pull morrisjobke/webdav
```
> If you haven't install docker, please see [docker](https://docs.docker.com/engine/installation/)
> The docker repository: [morrisjobke/webdav/](https://hub.docker.com/r/morrisjobke/webdav/)
#### Open browser to make sure the WebDAV server is started
> http://localhost:8888/webdav
### 2. Try to upload a file to the server
***
#### Modify the file path in code
```
# Modify the path to what you want to upload
remote_path = "file1"
local_path = "/Users/ipython/Desktop/file1"
```
#
#### Run the command
> python webdav.py
***
### 3. See the result
![browser.png](https://github.com/edhs0011/webdav/blob/master/browser.png)
