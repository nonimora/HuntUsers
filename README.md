# HuntUsers

Introduction: File Reading in Python

This Python script uses File Reading to read a list of usernames from a text file and check which usernames may exist on a web application, such as a TryHackMe (THM) lab.

The program opens a file containing a list of usernames, reads it line by line, and sends HTTP requests to the target web application. It then analyzes the server's responses to identify potentially valid usernames based on the messages returned.
Main concepts used in the code

    File Reading: Reads usernames from a text file using Python's open() function.
    Loop (for): Iterates through the file line by line.
    String Cleaning (strip()): Removes whitespace and newline characters from each username.
    HTTP Requests (requests): Sends requests to the web application.
    Response Analysis: Checks the server's responses to distinguish potentially valid usernames from invalid ones.
    Exception Handling (try/except): Handles errors, such as a missing file or a failed HTTP request.
