import webdav.client as wc
options = {
 'webdav_hostname': "http://localhost:8888/webdav/",
 'webdav_login':    "test",
 'webdav_password': "test"
}
client = wc.Client(options)

client.upload_sync(remote_path="file1", local_path="/Users/edhs0011/Desktop/file1")