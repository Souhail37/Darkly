## **Discovery Process**
While performing directory enumeration using `dirb`, I discovered a `robots.txt` file. This file contained a disallowed directory named `.hidden`. Navigating to this directory revealed multiple subdirectories with randomly generated names.

Upon further investigation, each of these subdirectories contained additional randomly named directories, forming a deeply nested structure. Manually checking each path would be inefficient, so I decided to automate the process.

## **Automation Strategy**
To efficiently traverse the directory tree and locate the flag, I wrote a Python script that:
1. **Extracts all links** from each visited page.
2. **Recursively follows discovered links** while avoiding duplicate paths.
3. **Checks each path** to determine if it contains the flag file.

## **Outcome**
After executing the script, it successfully navigated through the nested directories and located the flag file, completing the challenge efficiently.

---

The full script is available in the repository along with this writeup.
