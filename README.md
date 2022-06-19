# AutumnLeafApp
## Prerequisites: 
* Download Oracle VM VirtualBox Manager and install Ubuntu 22.04.
* After installation boot Ubuntu on your VirtualBox and open terminal (ctrl + alt + t) to install python, pytest and requests:
   ```bash
    sudo apt udate
    sudo apt install python3 -pip
    pip install -U pytest
    python3-m pip install requests
   ```
* Next we are installing and testing docker with the following commands:
  ```bash
    sudo apt- get remover docker docker-engine docker.io
    sudo apt- get update
    sudo apt install docker.io
    sudo snap install docker
    docker --version
    sudo docker run hello-world
    sudo docker images
    sudo docker ps -a
    sudo docker ps
  ```
  ## Question 1
  * Open question1.py in a text editor
  * We will need to declare counter as a global variable inside the function tester() as the scope of counter won't allow us to use it inside of a fuction:
    * inside def tester() we need to add: ```global counter``` 
  * The script will now run
  * Make sure you've navigated to the correct directory in the terminal using ```cd```

  ## Question 2 
  * We need to use pytest to test the code in question2.py, specifically whether the funtion inc(x) returns a value equal to 5.
  * Using the terminal we can test this with pytest using ```python3 -m pytest question 2.py ```
  * The test will fail unless you run it after changing the funtion inc(4)

  ## Question 3
  * We'll be writing a python script in a text editor saved as question3.py which will loop and hit a website a certain amount of times and record request times, number of iterations and the name of the website
    * Firstly we'll be using requests and BeautifulSoup so we'll need to imort requests and bs4
    * We're declaring two variables, times (number of iterations) and site (raw data recieved from the url using get request)
    * We set up a for loop with the condtion being it runs while iterations are less than 6
    * Inside of the for loop we set up an if statement which will run if we receive data from the selected url 
    * For every loop we add 1 to the variable times and print the current iteration number
    * We also print the elapsed request time of the current iteration using .elapsed on the data received from the get request
    * Next we will find the name of the website by firstly declaring a new variable "page" and using BeautifulSoup we store the parsed text data from site (the data received using get request)
    * We print out the name of the site using page.title.text
  ## Question 4 
  * We'll create a docker file in order to create a docker image in our terminal.
  * We need to open Dockerfile provided to us and add in the 3rd RUN line: beautifulsoup4 because we used beautiful soup in question3.py
  * In the terminal we use the following commands to create a docker image:
    * ```docker build -t question3 .```
    
  * Run container with
    * ```docker run python-question3```



  
