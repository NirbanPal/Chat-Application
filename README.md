# Chat-Application
<p>This is a real-time chat application. Here we can create groups and add users and users can add himself to that group and every can chat with each other. A notification will also be send if there is any activity in that group.</p>
<P>Users have to register himself atfirst. Then there are also some features like login, logout, create room, add user, Chat in group etc</P>

**Tech used->**
<p> HTML , CSS, TAILWIND CSS, JAVASCRIPT, JQUERY, AJAX, DJANGO, PYTHON, MYSQL, DJANGO CHANNELS, CHANNEL LAYER, SOCKETS, UVICORN(AS ASGI SERVER)</p>

**Setup this project**
1. Clone this git repo->

  ```git
  git clone <gitRepoLink>
  ```
2. Go to the directory->

   ```git
   cd <directory>
   ```
   
3. Put your django secret key in the settings.py SECRET_KEY section and create a online redis account and get the host from it and put in the host section of CHANNEL_LAYERS. I have given the instructions how to get the host from online in settings.py also.
   
4. Create virtual environment->
   
   ```python
   python -m venv <your_virtual_environment_name>
   ```
5. To activate your virtual environment(windows)->

   ```python
   <your_virtual_environment_name>\Scripts\activate
   ```
   
6. Install requirements.py file->
   
   ```python
   pip install -r requirements.py
   ```

7. Migrate your database->

   ```python
   python manage.py makemigrations
   ```

   ```python
   python manage.py migrate
   ```

8. To run the application in your local machine->
   
   ```uvicorn
   uvicorn chatproject.asgi:application
   ```
   or
   
   ```uvicorn
   #Here n is number of workers. example->uvicorn chatproject.asgi:application --workers=4
   uvicorn chatproject.asgi:application --workers=n
   ```

