# **Description:**  
While inspecting the website using browser developer tools, I discovered a cookie named `I_am_admin` with the following value:

```
Name: I_am_admin  
Value: 68934a3e9455fa72420237eb05902327  
```

Recognizing the value as an MD5 hash, I attempted to decrypt it and found that it corresponded to the plaintext string `false`. This suggested that the application was using a simple boolean check based on the cookie value.

## **Exploitation:**  
To escalate privileges, I modified the cookie value to `true` by hashing it with MD5:

```
true → MD5 → b326b5062b2f0e69046810717534cb09
```

I then replaced the original cookie value with the newly generated hash:

```
Name: I_am_admin  
Value: b326b5062b2f0e69046810717534cb09  
```

Upon reloading the website, I successfully gained admin privileges and was presented with the flag.

## **Flag Retrieval:**  
The flag was displayed on the webpage after the privilege escalation through cookie manipulation.
