### How to start containters and app
1. From  project folder in terminal :
     ```bash
     docker-compose --env-file .env build
     ```
     This command creates docker images for the application.
2. To run  containers , created from images, from the previous step :
     ```bash
		 docker-compose --env-file .env up -d
    ```
3.  In browser, navigate to **localhost:5000**:<br>
   ![enter image description here](https://raw.githubusercontent.com/Rayveni/blog/main/articles/flask%20redis/img/app_screen.jpg)
4. Run background tasks by submitting task parameters in the input form (in implemented background task, the input parameter is returned with a 60 second delay) and review the results (click the **Completed Tasks** link).
Explanation of the project's source code below.
5.  To stop the containers and the application:  
     ```bash
	   docker-compose --env-file .env down
     ```