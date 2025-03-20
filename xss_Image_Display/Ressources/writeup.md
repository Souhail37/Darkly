# **Description:**
While navigating the website, I discovered an image that could be clicked. Upon clicking, the URL changed to:
```
http://10.11.100.242/?page=media&src=nsa
```
This indicated that the `src` parameter controlled the displayed content.

## **Vulnerability:**
The website was vulnerable to **Reflected Cross-Site Scripting (XSS)**, allowing JavaScript execution via user input manipulation.

## **Exploitation:**

### **Initial Attempts:**
- I first tried injecting a simple `<script>` tag inside the `src` parameter, but it was not executed.
- On inspecting the page source, I found that the image was being embedded within an `<object>` element:
  ```html
  <object data="http://10.11.100.242/images/nsa_prism.jpg"></object>
  ```
- Attempting to break out of the `data` attribute using `src=nsa"><script>alert(1)</script>` failed because the injected quotes were still encapsulated within the attribute.

### **Bypassing Restrictions:**
To execute JavaScript, I leveraged a **data URI payload** that directly injects a base64-encoded script:
```
src=data:text/html;base64,PHNjcmlwdD5hbGVydCgxKTwvc2NyaXB0Pg==
```
Decoding the base64 string reveals:
```html
<script>alert(1)</script>
```
### **Execution & Flag Retrieval:**
By injecting this payload, the script executed successfully, triggering an alert and revealing the flag.
