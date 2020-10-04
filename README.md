# Unicode Training 2 [Django Rest Framework]
## Student Teacher Quiz CRUD with User Authentication using DJANGO REST FRAMEWORK

An app where student and teachers can register/log in. Teachers can create a quiz on a subject and can view students that have given it and see their markd. Student can take a quiz (only once) and can see the correct answers and their marks

## ABOUT THE PROJECT
---
### **User Authentication :**
The *accounts* app manages all tasks related to registration, login, logout. It has 3 models: User, Student, Teacher. All these models are derived from **AbstractBaseUser** as it helps us in getting complete control over the model. The models use 'Email' as the 'Username' field and all the models are accessible in the Django Admin page. The registeration form is seperate for students and teachers and the whole project can be authorised using *is_student* and *is_teacher* boolean variables along with *ROLE (STUDENT or TEACHER)*. The project uses Django built-in **auth_views** for login and logout.

### **CRUD APP**
The CRUD app is regulated using *is_student*, *is_teacher* and *is_authenticated* booleans. There is a create-quiz form where teachers can name the quiz subject/topic and the number of questions in that quiz. They are then directed to the add-questions page where they can add questions with options and the correct answer and then submit the quiz for students. They can also update the quiz questions by going to the *update/<quiz_id>* page and updating the questions. They can delete the quiz in the same way by going to *delete/<quiz_id>* url. Teachers can also view the students list and their score on *result-list/<quiz_id>*. Students can take the quiz by going to *display<quiz_id>* and can check their score on *result/<quiz_id>*. Students can take a quiz only once. 


## Installation 
----

1. Clone the project.
    ```shell
    $ git clone https://github.com/junaidgirkar/Unicode_REST-API
    ```
2. `cd` intro the project directory
    ```shell
    $ cd Unicode_REST-API
    ```
3. Create a new virtual environment activate it.
    ```shell
    $ python3 -m venv env
    $ env/bin/activate
    ```
4. Install dependencies from requirements.txt:
    ```shell
    (env)$ pip install -r requirements.txt
    ```
5. Migrate the database.
    ```shell
    (env)$ python manage.py migrate
    ```

6. Run the local server via:
    ```shell
    (env)$ python manage.py runserver 8000
    ```

### Done!
The local application will be available at <a href="http://localhost:8000" target="_blank">http://localhost:8000</a>.



## Contributing
Pull requests are welcome. For major
changes, please open an issue first 
to discuss what you would like to change.

===================================
