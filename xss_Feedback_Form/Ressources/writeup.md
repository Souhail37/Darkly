# **Description:**

The challenge presented a feedback form with two input fields:
- **Name*** (Text input)
- **Message*** (Text input)

After submitting a message, the input was expected to be stored and displayed elsewhere on the website. Given this setup, an initial hypothesis was that the website might be vulnerable to **Stored Cross-Site Scripting (XSS).**

---

## **Exploitation:**

### **Initial Test**

To test for XSS, I entered the following values into the form:

- **Name:** `test`
- **Message:** `script`

Upon submitting, the page immediately returned the flag, without needing to include a `<script>` tag or any payload. 

This behavior suggests that the backend misinterpreted certain input values or had improper filtering, allowing the input **"script"** alone to trigger a response containing the flag.

---

## **Flag Retrieval:**

The flag was displayed directly after submitting the form with "script" as the message content.

### **Possible Explanation:**
- The application might be using an unsafe keyword-based filter that mistakenly triggers when the word "script" appears.
- The input might be evaluated in a way that treats certain reserved words as executable elements, causing an unintended response.
