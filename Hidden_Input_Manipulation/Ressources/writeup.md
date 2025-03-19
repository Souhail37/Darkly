# **Description:**

The challenge presented a **Forgot Password** functionality on the sign-in page. Clicking on the **"I forgot my password"** button redirected to a page displaying:

```
RECOVER PASSWORD:
[Submit Button]
```

Notably, there was no visible input field for entering an email to recover the password.

---

## **Vulnerability:**

The form contained a **hidden input field** with a predefined email value:

```html
<form action="#" method="POST">
    <input type="hidden" name="mail" value="webmaster@borntosec.com" maxlength="15">
    <input type="submit" name="Submit" value="Submit">
</form>
```

This indicated that the email was being sent to the server without user input, making it vulnerable to **Hidden Input Manipulation (Client-Side Parameter Tampering)**.

---

## **Exploitation:**

By modifying the **value** of the `mail` hidden input field in the browser’s developer tools (or using a manual HTTP request), I changed:

```
value="webmaster@borntosec.com"
```

to:

```
value="test"
```

Then, after clicking **Submit**, the response revealed:

```
The flag is : 1d4855f7337c0c14b6f44946872c4eb33853f40b2d54393fbe94f49f1e19bbb0
```

This confirmed the ability to manipulate hidden input values to influence backend processing.

---
