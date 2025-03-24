# **Description**
While analyzing the website, I found three social media icons in the footer for Facebook, Twitter, and Instagram. Each icon contained a hyperlink with the following structure:

```html
<a href="index.php?page=redirect&amp;site=facebook" class="icon fa-facebook"></a>
```

This suggested that clicking the link would redirect the user to the appropriate social media page. However, the `site` parameter was user-controlled, making it a potential candidate for an open redirect vulnerability.

## **Exploitation**
To test for vulnerability, I modified the `site` parameter by inspecting the element in my browser's developer tools. Instead of `facebook`, I changed it to an external URL:

```
index.php?page=redirect&site=https://fake.com
```

After clicking the modified link, I was redirected to the page with the flag, confirming the presence of an **Open Redirect vulnerability**.
