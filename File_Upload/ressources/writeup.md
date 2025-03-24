# **Description:**
While testing the file upload functionality on the website, I discovered that the application does not properly validate uploaded file types. This allowed me to upload a PHP script disguised as an image, which was then executed on the server, revealing the flag.

---

## **Method 1: Using curl**
I used the following `curl` command to upload a PHP file with a fake `Content-Type` header:

```bash
curl -X POST -F "Upload=Upload" -F "uploaded=@file.php;type=image/jpeg" "http://10.11.100.245/index.php?page=upload"
```

- `-X POST` sends a POST request.
- `-F "Upload=Upload"` simulates the upload form submission.
- `-F "uploaded=@file.php;type=image/jpeg"` attaches a PHP file while spoofing its content type as `image/jpeg`.
- The server accepted the file and executed it, revealing the flag.

---

## **Method 2: Using Burp Suite**
Another approach involved **Burp Suite** to manipulate the request manually:

1. **Intercept the Request:**
   - I navigated to the upload page and uploaded a dummy image.
   - Burp Suite intercepted the request.

2. **Modify the Request:**
   - Inside Burp Proxy, I changed the `Content-Type` of the uploaded file to `image/jpeg` while keeping the filename as `file.php`.
   - This tricked the server into accepting and executing my PHP payload.

3. **Forward the Request:**
   - After modifying the request in **Burp Proxy**, I forwarded it.
   - The file was successfully uploaded and executed when accessed, revealing the flag on the webpage.

---
