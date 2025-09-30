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

/////

ASSIGNMENT 3    

Data delivery is essential because platforms rely on communication between different components (frontend, backend, databases, APIs). Without a way to transfer data, users couldn’t see updated content, send inputs, or interact with the system. Data delivery ensures synchronization, interaction, and real-time functionality.

In my opinion, JSON is better than XML. Personally, I find JSON much easier to read and write because it looks very similar to Python dictionaries or JavaScript objects. It is also less verbose since it does not require opening and closing tags like XML. I prefer JSON because it feels more natural to use when working with APIs, especially in web development. JSON is also faster to parse and is directly supported by most modern programming languages. In addition during my previous internship, everyone advises me to use JSON file.
So I think that JSON is much more popular than XML for all theses reasons.

The is_valid() method is essential because it ensures that the data submitted through a form is correct before we process it. For example, if a user tries to submit an empty required field or enters text where only numbers are expected, is_valid() will detect that and prevent errors in the application. Personally, I think this makes development much safer and cleaner, because it avoids having to manually check every input. It gives me confidence that the data I save into the database is reliable.

I think the csrf_token is very important because it adds an extra layer of protection against Cross-Site Request Forgery (CSRF) attacks. Basically, it makes sure that a form submission is really coming from the legitimate user on the site, and not from a malicious third-party page. Without it, an attacker could trick someone into submitting hidden forms that perform dangerous actions, like changing account settings or making unwanted purchases. For me, the csrf_token is a simple but powerful way to secure forms and prevent these kinds of attacks.

At each step, I carefully checked that everything was working before moving on to the next one. I paid close attention to following the tutorial so I wouldn’t miss any important detail, and I adapted the code meticulously to fit my own project, the Football Shop. Along the way, I faced some display issues, for example the release year was showing as day-month-year instead of only the year. To fix this, I modified the model and had to redo the migrations properly. I also made a mistake when creating one product, so I decided to create an admin account in Django in order to correct and manage the data. At that point, I realized I didn’t know another way to edit my data except through the /admin URL, so using the admin site was very helpful.

I would have appreciated having a bit more context in the assignment instructions instead of only receiving a checklist.
I really appreciate the fact that we can always contact the TAs in case of doubt or confusion. Their availability makes the process much easier and more reassuring.

<img width="959" height="503" alt="postman json id" src="https://github.com/user-attachments/assets/63bf8503-7b0e-4301-8ec0-07b5237dbcad" />
<img width="959" height="501" alt="postman json" src="https://github.com/user-attachments/assets/faab7575-1455-4002-a9e0-9229660b30d0" />
<img width="959" height="503" alt="postman XML id" src="https://github.com/user-attachments/assets/caf2e187-51cd-4872-a911-f23c635c8f4a" />
<img width="958" height="500" alt="postman xml" src="https://github.com/user-attachments/assets/5fd4157a-2a17-49c1-b1a5-ef67bfe1b9d2" />



/////

ASSIGNMENT 4  

Django provides the built-in AuthenticationForm to handle user login. It automatically validates a username and password, checks if the account exists and is active, and returns an authenticated user object if the credentials are correct. Its main advantage is that it is fully integrated with Django’s authentication system and saves development time. However, it is limited in flexibility, since it is tied to Django’s default user model and requires customization when using alternative login methods such as email-only authentication.

Authentication is the process of verifying a user’s identity, for example by checking their username and password. Authorization, on the other hand, defines what resources or actions the authenticated user is allowed to access. In Django, authentication is managed by the django.contrib.auth module through functions like authenticate() and login(). Authorization is handled by Django’s permission system, which assigns specific permissions and group-based roles to users, along with special flags like is_staff or is_superuser.

Cookies and sessions are two mechanisms used to maintain state in web applications. Cookies store data directly in the client’s browser, making them lightweight and persistent, but they are limited in size and exposed to security risks. Sessions store data on the server and only send a session ID through a cookie, which is more secure and allows larger or more complex data to be managed. However, sessions add extra server load and require management of expired session data. Django uses a combination of both by storing session data server-side and linking it to the client through a session cookie.

Cookies are not secure by default and can be vulnerable to attacks such as session hijacking, cross-site scripting (XSS), or cross-site request forgery (CSRF). To mitigate these risks, Django stores sensitive session data on the server and only transmits a session ID in the cookie. It also provides built-in protections such as HttpOnly to prevent JavaScript access to cookies, Secure to enforce HTTPS-only transmission, and CSRF protection through unique tokens in forms. These measures make cookie usage safer in Django applications.

How I implemented the checklist above step-by-step : 

- I modified the Product model so that it is directly linked to Django’s built-in User model using a ForeignKey relationship. This makes it possible to associate each product with its owner and to filter products easily depending on the logged-in user. This design also ensures that if a user is deleted, all of their products are automatically removed, keeping the database consistent.
- For registration, I used Django’s UserCreationForm, which automatically handles validation of standard fields. After a new user registers, I log them in immediately to create a smooth experience. I also set a last_login cookie to record the login time
- For login, I used Django’s AuthenticationForm to check credentials. Before logging the user in, I retrieved the previous last_login value from the database and stored it in a cookie. This way, the user can see the timestamp of their previous login on the homepage. Once the login is confirmed, Django automatically updates the last_login field in the database.
- On the homepage, I implemented a check: if the user is logged in, the page displays their username, their personal products, and the last_login value from the cookie. If the user is not logged in, the page only shows links to the login and registration pages. This logic confirms that products are correctly linked to their owners and that the cookie mechanism is working as intended.
- I created two different user accounts and added a total of six products, named simply Product1 through Product6 to keep them as dummy data. To test image functionality while still using placeholders, I assigned simple placeholder images to the products. I then verified that depending on the active session, each user could only see their own products, which confirms that the “author of a product” feature works correctly.
- Finally, I tested the full workflow step by step: registering a user, logging in, checking the homepage display, logging out, and then logging in with the second account. At each step, I verified that the last_login cookie was properly updated and that only the correct user’s products were displayed.


/////

ASSIGNMENT 5 

- CSS Selector priority : 
In CSS, it is common for the same HTML element to be targeted by several different selectors at once. For example, a paragraph might be affected by a general rule for all <p> elements, by a class applied to it, and also by an ID or even an inline style. Since these rules can overlap, the browser needs a hierarchy to decide which one is applied.

This hierarchy is called specificity and it gives different “weights” to selectors in this order :

1. Inline styles
2. ID selectors
3. Class selectors
4. Element selectors

If two rules have the same specificity, the browser applies the one that is written last in the stylesheet, meaning that the order of the code also matters.

Finally, there is the special case of !important. A declaration with !important overrides all others, except if there is another !important in conflict. In that case, the normal specificity rules are used again.

- Responsive Design : 

• Why is responsive design important in web application development?
Responsive design is very important in web application because we can't predict on wich device the user will open the app. Indeed, the web is available on computers, on tablets, and smartphones, and our design has to be adapted to all of these devices. A web application designed only for computers may be distorded, too small, incovenient and unusable on a mobile phone since the size and orientation of the screen are different. Event the way we interact with the device is different. That's why the concept of responsive apps exists. Elements like layout, images and text are adjusted automatically to the user's device. This provides a consistent and optimized user experience across all devices, leading to better user experience. It also increases website visibility to a wider audience and reduces development and maintenance costs by eliminating the need for separate mobile and desktop versions of a site. 

• Provide examples of applications that have and haven't implemented responsive design & Explain the reasons behind your examples :
An application that has implemented responsive design is Instagram. Its features, such as Stories, adapt automatically to different devices. On a smartphone, Stories are displayed vertically to match the natural way people hold their phones, filling the entire screen for an immersive experience. On a tablet or desktop, the same content is adjusted: the story may not cover the full width, but Instagram centers it and adapts the margins and navigation controls so it remains readable and usable. This ensures that, regardless of the screen size or orientation, the visual quality and user experience stay consistent.

In contrast, during an internship, I developed an internal payroll web application for employees. Because it was intended to be used only on desktop computers, I initially created non-responsive prototypes. At that time, I lacked both the time and the technical knowledge to implement responsive design. However, when I later resized the browser window, I noticed major display issues, which made me realize how indispensable responsive design is, even in applications primarily targeted at desktop users.

- Box Model : 
The difference between margin, border, and padding lies in the way they define spacing in relation to an element and its content.

    - Margin is the space outside an element. It creates distance between the element and surrounding elements on the page. Adjusting the margin does not affect the element’s size but changes its position relative to others.
    - Border is the line drawn around the element. It sits between the margin and the padding and can have different thicknesses, colors, and styles such as solid, dashed, or dotted.
    - Padding is the space inside the element, between the content and the border. Increasing the padding pushes the content inward and makes the element itself larger without affecting the distance to other elements.

<img width=auto alt="css model" src="https://media2.dev.to/dynamic/image/width=800%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fdev-to-uploads.s3.amazonaws.com%2Fuploads%2Farticles%2F18sfy7anxl7uj5soub2i.png" />

To implement them, CSS properties such as margin, border, and padding are used. For example, margin: 20px; adds space around the element, border: 2px solid black; adds a black border around it, and padding: 15px; adds space inside the element between its content and the border.

- Layout Systems : 
Flexbox is a CSS layout system for arranging elements in a single row or column. It allows items to grow, shrink, and wrap to fit the available space, making it ideal for navigation bars or lists. 
Grid layout is used for two-dimensional layouts, controlling both rows and columns at the same time. It is useful for complex structures like dashboards or image galleries. Flexbox is best for one-dimensional, flexible alignment, while Grid provides precise control over both horizontal and vertical placement of elements. 


- Implementation Steps : 

First, I implemented the core functionality, adding the ability to delete and edit products and testing them carefully. For the design, I decided to use Bootstrap instead of Tailwind (used in the tutorial) so I could gain experience with both frameworks. I explored the Bootstrap website to see examples and choose components I liked, aiming for consistency across all pages. I also looked at other websites to draw inspiration for colors, layouts, and card designs, so that the overall application felt coherent and visually appealing. For the product list page, I made it responsive and created custom product cards with Edit and Delete buttons. I also designed a responsive navbar.