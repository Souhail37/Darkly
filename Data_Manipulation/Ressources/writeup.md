# **Description:**

A survey voting system was found to be vulnerable to an Insecure Direct Object Reference (IDOR) vulnerability, allowing users to manipulate grade values beyond the intended range. This vulnerability was present in the grade selection mechanism, which lacked proper server-side validation.

## **Vulnerability Analysis:**

The voting system utilized a `<select>` element to allow users to choose a grade. When a grade was selected, the form was automatically submitted. The application failed to validate the selected grade value on the server-side, allowing users to submit arbitrary values.

## **Exploitation:**

The survey section presented a table with voting options, including a grade selection dropdown.
Inspecting the HTML revealed the grade selection mechanism:
```html
        <form action="#" method="post">
            <input type="hidden" name="sujet" value="2">
            <SELECT name="valeur" onChange='javascript:this.form.submit();'>
                <option value="1">1</option>
                <option value="2">2</option>
                <option value="3">3</option>
                <option value="4">4</option>
                <option value="5">5</option>
                <option value="6">6</option>
                <option value="7">7</option>
                <option value="8">8</option>
                <option value="9">9</option>
                <option value="10">10</option>
            </SELECT>
        </form>
```
The `onChange='javascript:this.form.submit();'` attribute indicated that the form would submit automatically upon grade selection.

Using browser developer tools, the `value` attribute of one of the `<option>` tags was modified from `value="2"` to `value="2000"`.
Selecting the modified option (grade 2) submitted the form.

## **Flag Retrieval:**  
The application accepted the value "2000" without validation, resulting in the successful manipulation of the grade value and the retrieval of the challenge flag.
