# **Description**  
During the assessment of the target website, I used **dirb**, a directory brute-forcing tool, with a wordlist to enumerate hidden paths. The scan revealed two interesting directories:  

- `/admin` → A secured area requiring authentication.  
- `/whatever` → Contained a file named **htpasswd**.  

## **Exploitation Steps**  

1. **Downloading the `.htpasswd` file**  
   - Visiting `/whatever/htpasswd` prompted a file download.  
   - Using `cat` on the file revealed:  

     ```plaintext
     root:437394baff5aa33daa618be47b75cb49
     ```

2. **Cracking the Password**  
   - The password hash was identified as **MD5**.  
   - Decrypting it using an online hash lookup revealed:  

     ```plaintext
     qwerty123@
     ```

3. **Gaining Access**  
   - Logging into `/admin` using the credentials `root:qwerty123@` successfully granted access.  
   - The page displayed the flag! 
