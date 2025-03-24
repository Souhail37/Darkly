# **Darkly - Web Security Auditing Project**

## **Introduction**
The **Darkly** project is an introduction to **cybersecurity in the Web domain**. It aims to help security enthusiasts and developers understand common **web vulnerabilities** by auditing an intentionally vulnerable website. These security flaws are frequently found in real-world applications, and learning how to exploit them provides valuable insights into securing web applications.

Through this project, I explored **OWASP’s Top 10 vulnerabilities**, identified and exploited security weaknesses, and documented them with detailed writeups.

---

## **Objectives**
The primary objectives of this project were to:
- Discover and exploit web vulnerabilities.
- Learn about **OWASP’s Top 10** and how frameworks handle security measures.
- Understand the impact of security flaws and propose mitigations.
- Perform penetration testing manually (without automated tools like `sqlmap`).

---

## **Discovered Vulnerabilities & Exploits**
### **1. Automated_Path_Discovery**
### **2. Brute_force**
### **3. Cookie_Manipulation**
### **4. Data_Manipulation**
### **5. File_Upload**
### **6. Hidden_Input_Manipulation**
### **7. htpasswd_Exposure**
### **8. http_request**
### **9. Image_sql_Injection**
### **10. LFI**
### **11. Members_sql_Injection**
### **12. Open_Redirect**
### **13. xss_Feedback_Form**
### **14. xss_Image_Display**

---

## **Automation & Scripting**
To streamline the exploitation process, I wrote Python scripts for:
- **Crawling `.hidden/` directories recursively** to find deeply nested files.
- **Automating SQL Injection enumeration** to extract database structure.
- **Testing XSS payloads dynamically** using `requests` and `BeautifulSoup`.

These scripts improved efficiency and helped bypass security mechanisms more effectively.

---

## **Lessons Learned & Takeaways**
1. **Understanding vulnerabilities is crucial** – Knowing how attacks work helps in securing web applications.
2. **Manual exploitation provides deep insights** – Automated tools (`sqlmap`, `burpsuite intruder`) are powerful, but manually crafting attacks improves knowledge.
3. **Proper validation & security best practices matter** – Many exploits could have been prevented with:
   - **Input sanitization** (`SQLi`, `XSS`, `LFI`)
   - **Session security** (`cookie manipulation`)
   - **Rate limiting** (`brute force login`)
   - **Access control** (`file uploads, directory traversal`)

---

## **Conclusion**
This project provided hands-on experience in **web application security** by exposing and exploiting real-world vulnerabilities. It reinforced key **penetration testing techniques** and showcased the importance of secure coding practices. By documenting my findings and mitigation strategies, this repository serves as a **reference for learning and improving web security skills**.
