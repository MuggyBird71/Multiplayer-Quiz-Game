## Overview

**Project Title**: Quiz Game Server

**Project Description**: 
This project is a Python-based multiplayer quiz game server that allows clients to connect and compete by answering dynamically generated quiz questions. The server generates questions using the OpenAI API and provides a scoring system to keep track of client scores. The project demonstrates the use of socket programming, threading, and API integration.

**Project Goals**: 
- To develop a Python application that handles network communication using socket programming.
- To provide a multiplayer quiz experience with dynamically generated questions.
- To demonstrate the integration of external APIs (OpenAI) for dynamic content generation.

## Instructions for Build and Use

**Steps to build and/or run the software:**

1. Clone the repository or download the source code to your local machine.
2. Ensure Python is installed on your system (Python 3.7 or later is recommended).
3. Install the required libraries using pip:
   ```sh
   pip install -r requirements.txt

**Instructions for using the software:**

1. Run the 'server.py' file to start the server.
   ```sh
   python server.py
3. In a separate terminal, run the client.py file to start a client.
   ```sh
   python client.py
5. Follow the on-screen instructions to enter your username and password, and answer the quiz questions.

## Development Environment 

To recreate the development environment, you need the following software and/or libraries with the specified versions:

*Python - Version 3.7 or higher
*OpenAI Python Client - Latest version
*Requests Library - Latest version
*Any IDE that supports Python (PyCharm, Visual Studio Code, etc.)

## Useful Websites to Learn More

I found these websites useful in developing this software:

*[Python Documentation](https://docs.python.org/3/)
*[OpenAI Documentation](https://beta.openai.com/docs/
*Socket Programming in Python (GeeksforGeeks)
*[Stack Overflow](https://stackoverflow.com/)

## Future Work

The following items I plan to fix, improve, and/or add to this project in the future:
* [ ] Add functionality to handle more complex quiz questions and types.
* [ ] Implement a graphical user interface (GUI) to make the client application more user-friendly.
* [ ] Enhance the scoring system to include more metrics such as time taken to answer each question.
* [ ] Add support for user registration and persistent score tracking.
