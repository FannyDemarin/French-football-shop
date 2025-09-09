# French-football-shop
Assignment 2 PBD
Name: Fanny Demarin
Student ID: 2506561542
Class: KKI


For this assignment, I carefully followed the checklist while trying to fully understand each step rather than just copy-pasting from a tutorial. My approach was to intuitively learn the order of tasks and the purpose of each file, so that in the future I will be able to set up a Django project without relying on a detailed tutorial.
During this assignment, I also became more comfortable using GitHub. At first GitHub felt a bit new, but now I am much more used to committing changes, pushing to remote, and connecting my repository to deployment platforms.

Throughout all these steps, I didn’t just “code blindly.” I focused on understanding what each file does and how the pieces connect: urls.py handles routing, views.py controls logic, models.py defines data, and templates handle presentation. Each time, I tried to keep in mind the definitions of the purpose of each file and reread them if necessary.

<img width="2360" height="450" alt="diagramme django" src="https://github.com/user-attachments/assets/bcbb1efb-01e5-4fb7-a9a1-816be2816df8" />


The settings.py file controls the environment and behavior of the whole project. Without it, Django would not know how to run your app. In this configuration file we can found which apps are installed, the allowed hosts, debug mode, and security settings for example.

Migration in Django is the process that makes sure the database structure follows the defined models. Whenever I add or change a field in models.py, I run makemigrations so Django prepares the update, and then migrate to apply it to the database. This way, I don’t have to edit the database manually. It keeps everything organized and makes it easy to track changes step by step. Makemigrations only creates a migration explaining the changes we made to the models. Next, we need to use the migrate command to make the model effective.


In my opinion, Django is chosen for learning because it has a clear structure and comes with many tools already included. However we still have to understand the main ideas of web development such as models, views, and templates and we can learn easier. At the same time, Django is widely used in real projects, so the things I practice here are directly useful if I want to build more advanced applications later.

I think tutorial 1 was quite clear, but there was a lot to take in and I would prefer to have a short oral presentation of the key concepts before we start. It's just my personal opinion, but I find it difficult to understand new things by reading a document. I would have preferred the MVT course to take place before tutorial 1.
