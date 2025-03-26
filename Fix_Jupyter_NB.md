# How to fix the git errors staging JP NB files
The easy fix seemed to be changing safeclrf from true to warn:
> git config --global core.safecrlf warn

Otherwise, you can use the function below. also shown later on in this NB

```python
    def convert_to_windows_line_endings(file_path):
        with open(file_path, 'rb') as file:
            content = file.read()
        content = content.replace(b'\n', b'\r\n')
        with open(file_path, 'wb') as file:
            file.write(content)
    convret_to_windows_line_endings(file_path)
```