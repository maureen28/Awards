# AWWARDS

## Description
This project allows users to post their projects for other users to rate according to design, usability and content.

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

### APIs
This application comes with two API Endpoints for Profiles and Projects.

<ul>
<li>Projects API Endpoint - </li>
<li>Profiles API Endpoint - </li>
</ul>

### Brief Webpage Overview.

<ul>
<li>Below is the landing page once the web browser is loaded</li>
<img src="/landing.jpg" alt=" Home page" width="1000"/>
<li>Below is the explore page </li>
<img src="/explore .jpg" alt=" Explore page" width="800"/>
</ul>

### Live link :


## BDD
<table>
<tr>
<th>Behaviour</th>
<th>Input</th>
<th>Output</th>
</tr>
<tr>
<td>Sign in to the app to post projects and review projects.</td>
<td><strong>Click sign in or register</strong></td>
<td>A form with username, password and email will be displayed.</td>
</tr>
<tr>
<td>Users can post a project to be rated.</td>
<td><strong>Click onto the post</strong></td>
<td>Post will be uploaded and displayed to landing page with rate stars</td>
</tr>
<tr>
<td>Users can search for different projects</td>
<td><strong>Enter the search term they want to the search</strong></td>
<td>All results of the searched term will be displayed.</td>
</tr>
</table>

## Setup Instructions

<ol>
<li> Clone this repo: git clone <code> https://github.com/maureen28/Awards.git</code> </li>
<li>The repo comes in a zipped or compressed format. Extract to your prefered location and open it.</li>
<li> Create a virtual environment and activate it.
<pre>
<code>
pip install virtualenv
source virtual/bin/activate
</code></pre>
</li>
<li> Install all the requirements <code> pip install -r requirements.txt</code></li>
<li> On your terminal,Create database aaward using the command :<code>CREATE DATABASE awards; and update settings.py </code>
</li>
<li> Migrate the database using the command : <code> python3.6 manage.py migrate </code> </li>
<li> Run <code>python3 manage.py runserver</code> to serve the app.</li>
<li> Use the navigation bar menu to navigate and explore the app.</li>
</ol>


## Running the tests
Use the command given below to run automated tests.
<code> python manage.py test awwards </code>


## Contact Information

To get in touch E-MAIL me on nimz69509@gmail.com

## License

MIT License
<b>Copyright (c) 2020 maureen28<b>