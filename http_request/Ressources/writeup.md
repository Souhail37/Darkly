# **Description:**

The website's footer contained a button labeled "© BornToSec" that, when clicked, redirected to a page displaying text and an image. Upon inspecting the page's source code, HTML comments were discovered that revealed conditional access logic. The comments indicated that access was restricted based on the `Referer` and `User-Agent` headers of the HTTP request.

## **Vulnerability Analysis:**

The application implemented client-side logic checks within HTML comments to enforce access restrictions. However, these checks were easily bypassed by manipulating the corresponding HTTP headers.

## **Exploitation Steps:**

1.  **Initial Observation:**
    * Clicking the "© BornToSec" button in the website's footer redirected to a page with static content.
    * Inspecting the page's source code revealed the following HTML comments:
        ```html
        You must come from : "https://www.nsa.gov/"
        Let's use this browser : "ft_bornToSec". It will help you a lot
        ```

2.  **Request Interception and Modification:**
    * Burp Suite was used to intercept the HTTP request to the vulnerable page.
    * The `Referer` header was modified to `https://www.nsa.gov/`.
    * The `User-Agent` header was modified to `ft_bornToSec`.

3.  **Successful Bypass:**
    * The modified request was sent to the server.
    * The server's response contained the flag, indicating that the access restriction had been successfully bypassed.
