# Fussy Pussy Cat Blog
![FussyPussy responsiveness screenshot](https://github.com/wayne-AF/fussy-pussy-cat-blog/blob/main/documentation/screenshots/responsive%20screenshot.png?raw=true)

The live project can be viewed [here](https://fussy-pussy-cat-blog.herokuapp.com/)
## Table of Contents
1. [User Experience](https://github.com/wayne-AF/fussy-pussy-cat-blog/edit/main/README.md#user-experience)
	- [Project Goals](https://github.com/wayne-AF/fussy-pussy-cat-blog/edit/main/README.md#project-goals)
	- [Project Planning](https://github.com/wayne-AF/fussy-pussy-cat-blog/edit/main/README.md#project-planning)
		+ [User Stories](https://github.com/wayne-AF/fussy-pussy-cat-blog/edit/main/README.md#user-stories)
	- [Features](https://github.com/wayne-AF/fussy-pussy-cat-blog/edit/main/README.md#features)
		+ [Navigation bar](https://github.com/wayne-AF/fussy-pussy-cat-blog/edit/main/README.md#navigation-bar)
		+ [Footer](https://github.com/wayne-AF/fussy-pussy-cat-blog/edit/main/README.md#footer)
		+ [Home page](https://github.com/wayne-AF/fussy-pussy-cat-blog/edit/main/README.md#home-page)
		+ [Post detail page](https://github.com/wayne-AF/fussy-pussy-cat-blog/edit/main/README.md#post-detail-page)
		+ [Contact page](https://github.com/wayne-AF/fussy-pussy-cat-blog/edit/main/README.md#contact-page)
		+ [Register page](https://github.com/wayne-AF/fussy-pussy-cat-blog/edit/main/README.md#register-page)
		+ [Log in page](https://github.com/wayne-AF/fussy-pussy-cat-blog/edit/main/README.md#log-in-page)
		+ [Log out page](https://github.com/wayne-AF/fussy-pussy-cat-blog/edit/main/README.md#log-out-page)
		+ [Add post page](https://github.com/wayne-AF/fussy-pussy-cat-blog/edit/main/README.md#add-post-page)
		+ [Update post page](https://github.com/wayne-AF/fussy-pussy-cat-blog/edit/main/README.md#update-post-page)
		+ [Delete post page](https://github.com/wayne-AF/fussy-pussy-cat-blog/edit/main/README.md#delete-post-page)
		+ [Profile page](https://github.com/wayne-AF/fussy-pussy-cat-blog/edit/main/README.md#profile-page)
		+ [Edit profile](https://github.com/wayne-AF/fussy-pussy-cat-blog/edit/main/README.md#edit-profile)
		+ [Edit settings](https://github.com/wayne-AF/fussy-pussy-cat-blog/edit/main/README.md#edit-settings)
		+ [Django admin panel](https://github.com/wayne-AF/fussy-pussy-cat-blog/edit/main/README.md#django-admin-panel)
2. [Design](https://github.com/wayne-AF/fussy-pussy-cat-blog/edit/main/README.md#design)
	- [Wireframes](https://github.com/wayne-AF/fussy-pussy-cat-blog/edit/main/README.md#wireframes)
		+ [Home page wireframe](https://github.com/wayne-AF/fussy-pussy-cat-blog/edit/main/README.md#home-page-wireframe)
		+ [Post detail wireframe](https://github.com/wayne-AF/fussy-pussy-cat-blog/edit/main/README.md#post-detail-wireframe)
		+ [Add/update post wireframe](https://github.com/wayne-AF/fussy-pussy-cat-blog/edit/main/README.md#add/update-post-wireframe)
		+ [Profile wireframe](https://github.com/wayne-AF/fussy-pussy-cat-blog/edit/main/README.md#profile-wireframe)
		+ [Edit profile wireframe](https://github.com/wayne-AF/fussy-pussy-cat-blog/edit/main/README.md#edit-profile-wireframe)
		+ [Contact wireframe](https://github.com/wayne-AF/fussy-pussy-cat-blog/edit/main/README.md#contact-wireframe)
		+ [Register wireframe](https://github.com/wayne-AF/fussy-pussy-cat-blog/edit/main/README.md#register-wireframe)
	- [Colours](https://github.com/wayne-AF/fussy-pussy-cat-blog/edit/main/README.md#colors)
	- [Fonts](https://github.com/wayne-AF/fussy-pussy-cat-blog/edit/main/README.md#fonts)
	- [Imagery](https://github.com/wayne-AF/fussy-pussy-cat-blog/edit/main/README.md#imagery)
3. [Technologies Used](https://github.com/wayne-AF/fussy-pussy-cat-blog/edit/main/README.md#technologies-used)
	- [Languages](https://github.com/wayne-AF/fussy-pussy-cat-blog/edit/main/README.md#languages)
	- [Frameworks and Libraries](https://github.com/wayne-AF/fussy-pussy-cat-blog/edit/main/README.md#frameworks-and-libraries)
	- [Software and Web Applications](https://github.com/wayne-AF/fussy-pussy-cat-blog/edit/main/README.md#software-and-web-applications)
4. [Testing](https://github.com/wayne-AF/fussy-pussy-cat-blog/edit/main/README.md#testing)
	- [Browser testing](https://github.com/wayne-AF/fussy-pussy-cat-blog/edit/main/README.md#browser-testing)
	- [OS compatibility](https://github.com/wayne-AF/fussy-pussy-cat-blog/edit/main/README.md#os-compatibility)
	- [Validation testing](https://github.com/wayne-AF/fussy-pussy-cat-blog/edit/main/README.md#-validation-testing)
		+ [HTML validation](https://github.com/wayne-AF/fussy-pussy-cat-blog/edit/main/README.md#html-validation)
		+ [CSS validation](https://github.com/wayne-AF/fussy-pussy-cat-blog/edit/main/README.md#css-validation)
		+ [Python validation](https://github.com/wayne-AF/fussy-pussy-cat-blog/edit/main/README.md#python-validation)
	- [Functionality](https://github.com/wayne-AF/fussy-pussy-cat-blog/edit/main/README.md#functionality)
	- [Testing user stories](https://github.com/wayne-AF/fussy-pussy-cat-blog/edit/main/README.md#testing-user-stories)
	- [Known issues](https://github.com/wayne-AF/fussy-pussy-cat-blog/edit/main/README.md#known-issues)
		+ [Default profile picture display](https://github.com/wayne-AF/fussy-pussy-cat-blog/edit/main/README.md#default-profile-picture-display)
5. [Deployment](https://github.com/wayne-AF/fussy-pussy-cat-blog/edit/main/README.md#deployment)
## User Experience
### Project Goals:
The primary goal of this project is to create a blog for cats with full CRUD functionality for registered users so they can create, read, update and delete any posts they have made. Registered users can also make comments on posts. Registered users also have profiles they have update with details in various specified categories, as well as uploading a profile photo to display on their profile page and in the byline of any posts they publish on the blog site. 
### Project Planning
I used an Agile methodology for planning this project, implemented using a Kanban board in Github Project with linked issues.
View the Kanban board [here](https://github.com/users/wayne-AF/projects/7).
#### User Stories
In planning, I decided upon 23 user stories I wanted to focus on during development. 
1.  As an unregistered user, I want the ability to read posts and comments.
2. As an unregistered user, I want the ability to send a message to the website owner.
3. As an unregistered user, I want the ability to register with the website.
4.  As a user, I want the ability to log in and log out.
5.  As a user, I want the ability to create a profile.
6. As a user, I want the ability to edit my profile.
7. As a user, I want the ability to upload a photo to my profile.
8. As a user, I want the ability to update my username
9. As a user, I want the ability to update my email address
10. As a user, I want the ability to update my password
11. As a user, I want the ability to delete my profile and account.
12. As a user, I want the ability to comment on a post.
13. As a user,  I want the ability to like a post.
14. As a user, I want the ability to unlike a post.
15.  As a user, I want the ability to write a post and upload it to the site.
16. As a user, I want the ability to edit a post I have written
17. As a user, I want the ability to delete a post I have written
18. As a user, I want the ability to submit a photo along with a blog post.
19. As a user, I want the ability to view a post author’s profile by clicking their username
20. As an admin, I want the ability to approve comments before they appear on the website
21. As an admin, I want the ability to delete a post or comment
22. As an admin, I want the ability to delete a user  
23. As an admin I want the ability to create, read, update, and delete posts from the admin panel     

### Features
#### Navigation bar
The navigation bar is visible on all pages of the site. The logo is on the left side of the bar, with clickable options on the right. When the user is not logged in, the navbar is visible as:
![navbar-logged-out](https://github.com/wayne-AF/fussy-pussy-cat-blog/blob/main/documentation/screenshots/navbar%20-%20logged%20out.png?raw=true)
![navbar-logged-out-dropdown](https://github.com/wayne-AF/fussy-pussy-cat-blog/blob/main/documentation/screenshots/dropdown-not-logged-in.png?raw=true)
When the user is logged in, the navbar has the user's username as a dropdown menu:
![navbar-logged-in](https://github.com/wayne-AF/fussy-pussy-cat-blog/blob/main/documentation/screenshots/navbar-logged-in.png?raw=true)
![navbar-logged-in-dropdown](https://github.com/wayne-AF/fussy-pussy-cat-blog/blob/main/documentation/screenshots/dropdown-logged-in.png?raw=true)
#### Footer
The footer contains social links and a link for the contact page.
![footer](https://github.com/wayne-AF/fussy-pussy-cat-blog/blob/main/documentation/screenshots/footer.png?raw=true)

#### Home page
The home page displays up to six of the most recent posts. If there are less than six, the posts in the second row will expand to fill empty space.
![home page](https://github.com/wayne-AF/fussy-pussy-cat-blog/blob/main/documentation/screenshots/home%20page.png?raw=true)
#### Post detail page
The post detail page contains the post title and image, and the author with link to their profile.
![post detail page-logged out](https://github.com/wayne-AF/fussy-pussy-cat-blog/blob/main/documentation/screenshots/post-not-logged-in.png?raw=true)
When a logged-in user navigates to the post detail page of a post they wrote, they are able to select to edit or delete.
![post detail page-logged in](https://github.com/wayne-AF/fussy-pussy-cat-blog/blob/main/documentation/screenshots/post-logged-in.png?raw=true)
#### Contact page
The contact page contains a form to send a message to the website's email address using the EmailJS service.
![contact page](https://github.com/wayne-AF/fussy-pussy-cat-blog/blob/main/documentation/screenshots/contact.png?raw=true)
#### Register page
The register page contains a form for a user to sign up to the website. Username and email are both required. A link is at the bottom for the user to login if they already have an account.
![register page](https://github.com/wayne-AF/fussy-pussy-cat-blog/blob/main/documentation/screenshots/sign-up.png?raw=true)
#### Login page
The login form requires that user uses their email rather than a username. 
![login page](https://github.com/wayne-AF/fussy-pussy-cat-blog/blob/main/documentation/screenshots/login.png?raw=true)
#### Logout page
Clicking 'log out' in the username dropdown menu takes the user to the logout confirmation page.
![logout page](https://github.com/wayne-AF/fussy-pussy-cat-blog/blob/main/documentation/screenshots/logout-confirm.png?raw=true)
#### Add post page
The add post page, accessed from the 'Write post' link in the username dropdown menu takes the user to this page where they can give the post a title and create the content using the Summernote editor. The user can also upload an image to display with the title of the post. If no image is selected, the default image is uploaded instead. 
![add post page](https://github.com/wayne-AF/fussy-pussy-cat-blog/blob/main/documentation/screenshots/add-post.png?raw=true)

#### Update post page
When the author of a post looks at the post detail page of the post they wrote, the options to edit and delete are displayed beneath the post title. Clicking 'edit post' takes the user to this page where they can update the post. It will then be republished on the home page as the most recently published post. 
![update post page](https://github.com/wayne-AF/fussy-pussy-cat-blog/blob/main/documentation/screenshots/update-post.png?raw=true)
#### Delete post page
When the post author clicks 'delete post', they'll be taken to the post deletion confirmation page where they must confirm if they wish to delete the post. 
![delete post confirm](https://github.com/wayne-AF/fussy-pussy-cat-blog/blob/main/documentation/screenshots/post-delete-confirm.png?raw=true)

#### Profile page
All users have a profile page created automatically when they sign up. (Please see Known issues below for elaboration on the issue of default profile pictures not displaying correctly). Registered users can see each other's profiles by clicking on the author's name on any post they have written. If a user has not written a post, there is no available link to click to view their profile. While the initial plan was to enable users to click on comment authors to view profile pages, this functionality was not included in the project due to time constraints during development.
![profile page](https://github.com/wayne-AF/fussy-pussy-cat-blog/blob/main/documentation/screenshots/profile.png?raw=true)
#### Edit profile page
All profile fields are initially blank and the user must make an entry into each field. Uploading a picture is optional as a default display picture should display instead. (As mentioned above, please see Known issues below for elaboration on the issue of default profile pictures not displaying correctly). 
![edit profile page](https://github.com/wayne-AF/fussy-pussy-cat-blog/blob/main/documentation/screenshots/edit-profile.png?raw=true)
#### Edit settings page
The edit settings page allows the user to update their username and email and provides a link to change their password.
![edit settings page](https://github.com/wayne-AF/fussy-pussy-cat-blog/blob/main/documentation/screenshots/edit-settings.png?raw=true)
#### Django admin panel
The admin panel allows for the admin/superuser to edit and delete posts and comments, edit user details (excluding passwords), and delete users. The superuser can also create, read, update and delete posts from here and publish them to the website. 
![django admin page](https://github.com/wayne-AF/fussy-pussy-cat-blog/blob/main/documentation/screenshots/admin-panel.png?raw=true)
## Design
### Wireframes
#### Home page wireframe
![home page wireframe](https://github.com/wayne-AF/fussy-pussy-cat-blog/blob/main/documentation/wireframes/homepage_wireframe.png?raw=true)
#### Post detail wireframe
![post detail wireframe](https://github.com/wayne-AF/fussy-pussy-cat-blog/blob/main/documentation/wireframes/post_detail_wireframe.png?raw=true)
#### Add/update post wireframe
![add/update post wireframe](https://github.com/wayne-AF/fussy-pussy-cat-blog/blob/main/documentation/wireframes/add_post_wireframe.png?raw=true)
#### Profile wireframe
![profile wireframe](https://github.com/wayne-AF/fussy-pussy-cat-blog/blob/main/documentation/wireframes/profile_wireframe.png?raw=true)
#### Edit profile wireframe
![edit profile wireframe](https://github.com/wayne-AF/fussy-pussy-cat-blog/blob/main/documentation/wireframes/edit_profile_wireframe.png?raw=true)
#### Contact wireframe
![contact wireframe](https://github.com/wayne-AF/fussy-pussy-cat-blog/blob/main/documentation/wireframes/contact_wireframe.png?raw=true)
#### Register wireframe
![register wireframe](https://github.com/wayne-AF/fussy-pussy-cat-blog/blob/main/documentation/wireframes/register_wireframe.png?raw=true)
### Colours
I wanted the site to feel light and comfortable to look at for extended periods of time, to match the lighthearted premise and content. I used the orange and dark green for accent colours to draw attention to hover effects, headings, and text.
![colour palette](https://github.com/wayne-AF/fussy-pussy-cat-blog/blob/main/documentation/screenshots/color-palette.png?raw=true)
### Fonts
I used 'Berkshire Swash' for the navbar brand as it looks somewhat elegant but playful, tying in with the title of the blog 'Fussy Pussy', suggesting someone who has humorously 'elevated tastes'. The rest of the site uses the simple 'Open Sans' font for readability.
### Imagery
The default images for the post titles is a cat drawing I purchased for commercial use, depicting the eponymous Fussy who has created the blog, and edited for colour matching with the site's colour palette.
![fussy cat image](https://github.com/wayne-AF/fussy-pussy-cat-blog/blob/main/documentation/screenshots/placeholder_featured_image.png?raw=true)

The image for the default profile photo was also purchased for commercial use, depicting the outline of a cat's head. I used dark green, intended to contrast with the orange and light green backgrounds where it would appear on the site.
![default profile pic](https://github.com/wayne-AF/fussy-pussy-cat-blog/blob/main/documentation/screenshots/placeholder_profile_image.png?raw=true)
The background was also purchased for commercial use, and edited to change the colours to match the chosen colour palette. The images depicted are stereotypical cat iconography such as balls of yarn, paw prints, and fish.
![background](https://github.com/wayne-AF/fussy-pussy-cat-blog/blob/main/documentation/screenshots/background-image-25.png?raw=true)
I used a paw-print icon from Font Awesome in place of a heart for the like option on the post detail page. 
![paw icon](https://github.com/wayne-AF/fussy-pussy-cat-blog/blob/main/documentation/screenshots/paw-like-icon.png?raw=true)
## Technologies Used
### Languages used:
- HTML5
- CSS3
- JavaScript
- Python
### Frameworks and Libraries used:
- [Bootstrap](https://getbootstrap.com/) - Used for styling and responsive web pages
- [Django](https://www.djangoproject.com/) - Python framework used in development
- [Django Allauth](https://django-allauth.readthedocs.io/en/latest/index.html) - Used for user authentication and account registration
- [Django Crispy Forms:](https://django-crispy-forms.readthedocs.io/en/latest/)  Used for simplified rendering of Django forms
- [dj_database_url](https://pypi.org/project/dj-database-url/) - Used for database urls 
- [Gunicorn:](https://gunicorn.org/) - Used as the Web Server to run Django on Heroku
- [psycopg2:](https://pypi.org/project/psycopg2/) - Used PostgreSQL as database adapter.
- [Summernote:](https://github.com/summernote/django-summernote) - Used in the frontend and in the admin panel as a text editor for creating posts

### Software and Web Applications used:
- [AppUIzard](https://app.uizard.io/prototypes) - Used for wireframe creation
- [Cloudinary](https://cloudinary.com/) - Used for static and media file storage
- [ColorHunt](https://colorhunt.co/) - Used for choosing colour palette
- [EmailJS](https://www.emailjs.com) - Used for sending email from contact form
- [Font Awesome:](https://fontawesome.com/) - Used as a resource for icons
- [Git](https://git-scm.com/) - Used for version control by committing to Git and pushing to GitHub
- [GitHub](https://github.com/) - Used to store the code pushed from Git
- [Google Fonts:](https://fonts.google.com/) - Used as a source for fonts across the site
- [Heroku](https://heroku.com/) - Used to deploy and run the Python application
-  [Heroku PostgreSQL](https://www.heroku.com/postgres) - Used as the database for this project
- [HTML Validator:](https://validator.w3.org/) - Used for HTML validation
- [JSHint:](https://jshint.com/) - Used for JavaScript validation
- [MiniPaint](https://viliusle.github.io/miniPaint/) - Used for image editing to create the background and the placeholder images
- [MiniWebTool](https://miniwebtool.com/django-secret-key-generator/) - Used to generate Django secret key
- [PythonChecker](https://pythonchecker.com/) - Used for PEP8 Python validation
- [SimpleImageResizer](https://www.simpleimageresizer.com/) - Used for image editing for the background and placeholder images
- [StackEdit](https://stackedit.io/) - Used for markdown editing
- [Vectorstock](vectorstock.com) - Used as a source for the background and placeholder images
- [Website Mockup Generator](https://websitemockupgenerator.com/) - Used for capturing responsiveness screenshots
- [W3C](https://validator.w3.org/) - Used for HTML validation
- [W3 CSS Validator](https://jigsaw.w3.org/css-validator/) - Used for CSS validation
## Testing
### Browser testing
(Tested using MacOS Ventura Version 13.1 on iMac desktop)
- Chrome Version 108.0.5359.124: Website performed as expected. 
- Firefox Version 109.0: Website performed as expected. 
- Safari Version 16.2: Website performed as expected. 
### OS compatibility
- Android 11 Oxygen 11.1.2.2 (Chrome 109.0.5414.85): Website performed as expected. 

### Validation testing
#### W3C HTML validation
All HTML was pasted into the HTML check with base.html code and special Django-use characters such as {%%} removed.
base.html
![base.html code validation](https://github.com/wayne-AF/fussy-pussy-cat-blog/blob/main/documentation/code%20testing/base.html%20check.png?raw=true)
contact.html
![contact.html code validation](https://github.com/wayne-AF/fussy-pussy-cat-blog/blob/main/documentation/code%20testing/contact.html%20check.png?raw=true)
index.html
![index.html code validation](https://github.com/wayne-AF/fussy-pussy-cat-blog/blob/main/documentation/code%20testing/index.html%20check.png?raw=true)
login.html
![login.html code validation](https://github.com/wayne-AF/fussy-pussy-cat-blog/blob/main/documentation/code%20testing/login.html%20check.png?raw=true)
post_detail.html
![post_detail.html code validation](https://github.com/wayne-AF/fussy-pussy-cat-blog/blob/main/documentation/code%20testing/post_detail.html%20check.png?raw=true)
signup.html
![signup.html code validation](https://github.com/wayne-AF/fussy-pussy-cat-blog/blob/main/documentation/code%20testing/signup.html%20check.png?raw=true)
user_profile.html
![user_profile.html code validation](https://github.com/wayne-AF/fussy-pussy-cat-blog/blob/main/documentation/code%20testing/user_profile.html%20check.png?raw=true)
#### W3C CSS validation
![css validation](https://github.com/wayne-AF/fussy-pussy-cat-blog/blob/main/documentation/code%20testing/css%20check.png?raw=true)
#### PEP8 Python validation
The PythonChecker that I used suggested that all operators have a space on either side. When I implemented this in my code, the IDE threw up red lines everywhere. Therefore, I left out the spaces suggested around many of the operators, and the below results are what I received.
forms.py
![forms.py validation](https://github.com/wayne-AF/fussy-pussy-cat-blog/blob/main/documentation/python%20testing/forms.py%20check.png?raw=true)
models.py
![models.py validation](https://github.com/wayne-AF/fussy-pussy-cat-blog/blob/main/documentation/python%20testing/models.py%20check.png?raw=true)
views.py
![views.py validation](https://github.com/wayne-AF/fussy-pussy-cat-blog/blob/main/documentation/python%20testing/views.py%20check.png?raw=true)
### Functionality (manual testing)
![testing chart 1](https://github.com/wayne-AF/fussy-pussy-cat-blog/blob/main/documentation/testing%20chart/p4-test-chart-1.png?raw=true)
![testing chart 2](https://github.com/wayne-AF/fussy-pussy-cat-blog/blob/main/documentation/testing%20chart/p4-test-chart-2.png?raw=true)
![testing chart 3](https://github.com/wayne-AF/fussy-pussy-cat-blog/blob/main/documentation/testing%20chart/p4-test-chart-3.png?raw=true)
![testing chart 4](https://github.com/wayne-AF/fussy-pussy-cat-blog/blob/main/documentation/testing%20chart/p4-test-chart-4.png?raw=true)
### Testing user stories
- _As an unregistered user, I want the ability to read posts and comments._
	+ Any user can read the posts and comments by clicking on an individual blog card from the main page
	__Test result: SUCCESS__
- _As an unregistered user, I want the ability to send a message to the website owner._
	+ From the 'Contact' link in the navbar, any user can send a message to the website email 
	__Test result: SUCCESS__
- _As an unregistered user, I want the ability to register with the website._
	+ From the 'Account' dropdown menu in the navbar, a user can select the 'Register' link, and create an account on the website by entering a username, email, and password. 
	__Test result: SUCCESS__
- _As a user, I want the ability to log in and log out._
	+ For a user to log in, they can select the 'Log in' link from the 'Account' dropdown menu in the navbar and log in with their email and password. For a user to log out, they can select the 'Log out' link from the same menu and confirm they wish to log out.
	__Test result: SUCCESS__
- _As a user, I want the ability to create a profile._
	+ A profile is automatically created when a user signs up to the website.
	__Test result: SUCCESS__
- _As a user, I want the ability to edit my profile._
	+ When the user is logged in, they can click the 'Edit profile' link from the username dropdown menu and they'll be taken to the edit profile page where they can update any of the predetermined fields: 'favourite quote', 'breed', 'likes', 'dislikes', and 'about' and the changes will be reflected on their user profile which is visible to other users. 
	__Test result: SUCCESS__
- _As a user, I want the ability to upload a photo to my profile._
	+ Users can upload a profile photo on the same 'Edit profile' page as mentioned above.
	__Test result: SUCCESS__
- _As a user, I want the ability to update my username._
	+ When the user is logged in, they can click the 'Edit settings' link from the username dropdown menu and they'll be taken to the edit settings page where they can update their username.
	__Test result: SUCCESS__
- _As a user, I want the ability to update my email address._
	+ When the user is logged in, they can click the 'Edit settings' link from the username dropdown menu and they'll be taken to the edit settings page where they can update their email address.
	__Test result: SUCCESS__
- _As a user, I want the ability to update my password._
	+ When the user is logged in, they can click the 'Edit settings' link from the username dropdown menu and they'll be taken to the edit settings page. From here, they can click the link to update their password, and they'll be taken to a page where they can do so.
	__Test result: SUCCESS__
- _As a user, I want the ability to delete my profile and account._
	+ Currently, there is no method for a user to delete their own profile and account. However, they can send a message to the website's admin who can then delete their account from the admin panel once their authenticity has been confirmed by receiving a message from the email registered to the account. 
	__Test result: PARTIAL SUCCESS__
- _As a user, I want the ability to comment on a post._
	 + When a user is logged in, they can type in the comment text box on each post detail page and click the submit button. When the comment is approved by the admin, it will appear in the comments list beneath the post. 
 __Test result: SUCCESS__
- _As a user,  I want the ability to like a post._
	+ When a user is logged in, they can click on the paw icon beneath the post on the post detail page and the paw icon will be highlighted to indicate they have liked the post.
	__Test result: SUCCESS__
- _As a user, I want the ability to unlike a post._
	+ When a user is logged in and have already liked the post (they can see the paw icon is highlighted), they can click on the paw icon beneath the post on the post detail page and the paw icon will be unhighlighted to indicate they have unliked the post.
	__Test result: SUCCESS__
- _As a user, I want the ability to write a post and upload it to the site._
	 + When the user is logged in, they can click the 'Write post' link from the username dropdown menu and they'll be taken to the add post creation page where they can give the post a title and write its content using a text editor. When they submit the post, it will appear immediately on the home page as the most recently published post.
 __Test result: SUCCESS__
- _As a user, I want the ability to edit a post I have written._
	 + When the user is logged in, they can navigate to the post detail page of a post they have written, and underneath the post title, click on the 'edit post' link. They'll be taken to the 'edit post' page where they can rename the post and change its body content. When they click submit, the updated post will appear immediately on the home page as the most recently published post.
 __Test result: SUCCESS__
- _As a user, I want the ability to delete a post I have written._
	+ When the user is logged in, they can navigate to the post detail page of a post they have written, and underneath the post title, click on the 'delete post' link. They will be asked to confirm if they wish to delete the post and if they do so, the post will be deleted from the home page.
	__Test result: SUCCESS__
- _As a user, I want the ability to submit a photo along with a blog post._
	+ When the user is logged in, they can click the 'Write post' link from the username dropdown menu and they'll be taken to the add post creation page where they can select an image to upload with the post. If no image is chosen, the placeholder image will be displayed instead on the home page and post detail page.
	__Test result: SUCCESS__
- _As a user, I want the ability to view a post author’s profile by clicking their username._
	+ When the user is logged in, they can navigate to the post detail page of a post, and underneath the post title, click on the name of the author and they will be taken to the author's profile page.
	__Test result: SUCCESS__
- _As an admin, I want the ability to approve comments before they appear on the website._
	+ Comments must be approved by the admin before they appear on the site. To approve comments, access the admin panel with valid credentials and under the 'Blog' heading, select comments. Comments are marked as approved or unapproved and by selecting the relevant comments and selecting 'Approve comments' in the dropdown 'Action' menu and clicking 'Go', comments will be approved and visible under their posts.
	__Test result: SUCCESS__
- _As an admin, I want the ability to delete a post or comment._
	+ Comments can be deleted by following the above process and instead selecting 'Delete selected comments' in the dropdown Action menu.
	__Test result: SUCCESS__
	+ Posts can be deleted by selecting 'Posts' under the 'Blog' heading, selecting the desired posts to delete, selecting 'Delete selected posts' from the dropdown 'Action' menu and clicking 'Go'. 
	__Test result: SUCCESS__
- _As an admin, I want the ability to delete a user._
	 + Access the admin panel with valid credentials and click 'Users' under 'the Authentication and Authorization' heading. Select the desired users to delete, select 'Delete selected users' from the dropdown 'Action' menu and click 'Go'.
 __Test result: SUCCESS__
- _As an admin I want the ability to create, read, update, and delete posts from the admin panel._
	+ Access the admin panel with valid credentials. To create a post, click 'Add' beside 'Posts' under the 'Blog' heading and the 'Add post' page will appear where a post can be created and uploaded to the site. To read a post, click on 'Posts' under the 'Blog' heading and click on the title of a post to read it. On this same page, a post can be edited and deleted.
	__Test result: SUCCESS__
### Known Issues
#### Default profile picture display
If a user does not uploading a profile picture to their profile, a default profile picture should be displayed on the post_detail, edit_profile, and profile pages of the site. In the same way that if a user does not upload an image to accompany a post they have written, a default placeholder image will be used, the default profile picture should function in the same way. 
To utilise the default profile picture, I tried to use if/else statements on the relevant pages in the same way if/else statements were used to display default post pictures. While if/else statements were successful in displaying default post pictures, I was unable to achieve the same success using this method for default profile pictures. Even when no picture was uploaded by the user, in when used with if/else statements, the app perceived that the user had uploaded a photo and attempted to display it. After numerous attempts at resolving this issue and spending a considerable amount of time speaking with tutor support trying to find a solution, I was not able to fix this bug before project submission.
## Deployment
Heroku was used as the deployment platform for this project. Deployment steps are as follows.
- Log in to Heroku and navigate to the dashboard.
- Click on 'new' and 'create new app'.
- Choose a unique name for the application, choose location, and click 'create app'.
- After it has been created, navigate to the 'resources' tab.
- In the 'add-ons' search bar, search for 'Heroku postgres' and select it.
- In the pop-up window, choose the 'Hobby Dev - Free' plan.
- Click on submit.
- Navigate to the 'settings' tab and click 'reveal config vars'.
- Copy the DATABASE_URL value.
- In the project IDE, create an env.py file in the top level directory
- In the env.py file:
	+ enter os.environ["DATABASE_URL"] = "copied DATABASE_URL here"
	+ enter os.environ["SECRET_KEY"] = "created secret key value here"
- Navigate to the 'reveal config vars' in Heroku settings tabs and add the SECRET_KEY key and the previously created secret key value
- In settings.py:
	+ replace the secret key and replace with SECRET_KEY = os.environ.get("SECRET_KEY")
	+ update the DATABASE_URL with dj_database_url.parse(is.environ.get("DATABASE_URL")
- Save and make migrations using 'python3 manage.py migrate' in the terminal
- Log in to Cloudinary and copy the CLOUDINARY_URL API environment variable
- In the env.py file:
	+ enter os.environ["CLOUDINARY_URL"] = "cloudinary://copied variable"
- Back to the config vars section in Heroku, and add the CLOUDINARY_URL key and the copied variable value
- Add 'DISABLE_COLLECTSTATIC' key with a value of 1 to the config vars panel, which must be removed before final deployment
- In settings.py:
	+ Add the Cloudinary libraries to the installed apps list in the order of 'cloudinary_storage', 'django.contrib.staticfiles', 'cloudinary'
	+ Below STATIC_URL = '/static/', enter:
		* STATICFILES_STORAGE = ’cloudinary_storage.storage.StaticHashedCloudinaryStorage'
		* STATIC_ROOT = os.path.join(BASE_DIR, ’staticfiles')
		* MEDIA_URL = '/media/'
		* DEFAULT_FILE_STORAGE = 'cloudinary_storage.storage.MediaCloudinaryStorage'
	+ Link to the templates directory in Heroku by entering: TEMPLATES_DIR = os.path.join(BASE_DIR, ’templates')
	+ Change the templates directory to: TEMPLATES_DIR: 'DIRS': [TEMPLATES_DIR],
	+ ALLOWED_HOSTS: ALLOWED_HOSTS = [”Your_Project_name.herokuapp.com”, ”localhost”]
- In the top level directory of the project IDE, create folders: media, static, templates
- In the top level directory, create a Procfile
- In the Procfile, enter:
	+ web: gunicorn project_name.wsgi
- In the terminal, use git commands to commit and push
- In Heroku in the deploy tab, click on 'deploy branch'
- Once the build has complete, click on 'open app' to view the live site 
