# XSS attacks lab  
  
## Setup  
  
In order to complete the lab, make sure that you have installed: a web browser (such as Chrome or Firefox), Python and pip packet manager, Docker, and an IDE for editing JavaScript and Python code (e.g. you can use Notepad, VSCode, PyCharms, etc.).  
  
There are two options of how you can run the application:  
-	By activating the virtual environment and running the application from the terminal;  
-	By deploying a Docker container  
  
Option 1:  
1.1.	 Navigate to the root folder of the project.  
1.2.	 In the terminal, run “pipenv shell” – this activates a virtual environment.  
1.3.	 In the same terminal, run “pip install -r requirements.txt” – this installs the necessary libraries, including Flask, needed for the correct work of the application.  
1.4.	 Run “flask run” in the terminal.  
1.5.	 Navigate in the browser to localhost:5000 – you should be able to access the index page of the application.  
  
Option 2:  
1.1.	 Make sure Docker is running.  
1.2.	 Navigate to the root folder of the project.  
1.3.	 In the terminal, run the command “docker build -t xss-demo:latest –build-arg APP_IMAGE=python:3.7. -f Dockerfile .”  
1.4.	 After the image is built, run “docker container run -p 5000:5000 -dit –name xss-demo xss-demo:latest”  
1.5.	 Once the container is running, navigate in the browser to localhost:5000 – you should be able to access the index page of the application.  
  
