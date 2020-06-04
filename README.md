# INSTAGRAM

## Description
This is a clone of the website for Instagram. You can post, comment and view pictures posted on this App just like on Instagram.

### Author: Maureen Wairimu

## User Story

<ul>
<li>Users can view posted projects and their details.</li>
<li>Users can post a project to be rated/reviewed.</li>
<li>Users can rate/ review other users' projects.</li>
<li>Users can search for projects .</li>
<li>Users can view projects overall score.</li>
<li>Users can view my profile page.</li>
</ul>


## Technology & Dependency

<ol>
<li>DJANGO web framework.</li>
<li>HTML ,CSS(Bootstrap, FontAwesome) & JS </li>
<li>PostgreSQL or sqlite</li>
</ol>

### Brief Webpage Overview.

<ul>
<li>Below is the landing page once the web browser is loaded</li>
<img src="/landing.jpg" alt=" Home page" width="1000"/>
<li>Below is the explore page </li>
<img src="/explore .jpg" alt=" Explore page" width="800"/>
</ul>

### Live link : https://igcloneapp.herokuapp.com/


## BDD
<table>
<tr>
<th>Behaviour</th>
<th>Input</th>
<th>Output</th>
</tr>
<tr>
<td>Sign in to start using the app</td>
<td><strong>Click sign in or sign up</strong></td>
<td>A form with username, password and email will be displayed.</td>
</tr>
<tr>
<td>Upload pictures to app</td>
<td><strong>Click onto the upload icon</strong></td>
<td>Images will be uploaded and displayed to landing page</td>
</tr>
<tr>
<td>Follow other users</td>
<td><strong>Click on the follow button in the explore page</strong></td>
<td>Text of the person you follow will be displayed.</td>
</tr>
<tr>
<td>Like and comment as well as message</td>
<td><strong>Click on the like, comment or message button.</strong></td>
<td>Likes, comment or messages will be displayed in the homepage.</td>
</tr>
</table>

## Setup Instructions

<ol>
<li> Clone this repo: git clone <code> </code> </li>
<li> Create a virtual environment aand activate it.
<pre>
<code>
pip install virtualenv
source virtual/bin/activate
</code></pre>
</li>
<li> Install all the requirements <code> pip install -r requirements.txt</code></li>
<li> On your terminal,Create database instagram using the command :<code>CREATE DATABASE instaclone;  </code>
</li>
<li> Migrate the database using the command : <code> python3.6 manage.py migrate </code> </li>
<li> Run <code>python3 manage.py runserver</code></li>
<li> Use the navigation bar menu to navigate and explore the app.</li>
</ol>


## Running the tests
Use the command given below to run automated tests.
<code> python manage.py test insta </code>


## Contact Information

To get in touch E-MAIL me on nimz69509@gmail.com

## License

MIT License
<b>Copyright (c) 2020 maureen28<b>