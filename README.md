# Pizza Flask app using Python

This app is live [here](.herokuapp.com) <br>
It runs a bit slow since it is deployed on Heroku free tier account.



## Milestones achieved

The assignment had to be completed with meeting following requirements:

- Complete the Menu, Adding Items, and Registration/Login/Logout steps.
- Complete the Shopping Cart and Placing an Order steps.
- Complete the Viewing Orders and Personal Touch steps.

## Installation

1. Open terminal using Ctrl+T. Run the following command <br>
`git clone https://github.com/jackson-coder-arch/Pizza-Flask-App.git`

2. Create and active virtual environment using  <br>
` virtualenv -p python3 venv` <br>
` cd venv` <br>
`source bin/activate` <br>
3. `
4. Now you need to install python packages to run the app <br>
`pip3 install -r requiements.txt`
5. Create superuser <br>
 `python manage.py createsuper`
6. Run Django app <br>
`python manage.py runserver`

## Tech Stack

- **Flask**
- **SQLite** SQLite is a relational database management system contained in a C programming library. In contrast to many other database management systems, 
SQLite is not a client–server database engine. Rather, it is embedded into the end program<br>
It comes with Django with itself, no setup required, hence easy to use, but is not recommended for large scale
production application.
- **Bootstrap** Bootstrap is a free and open-source front-end Web framework. It contains HTML and CSS-based design templates for typography, forms, buttons, navigation and other
 interface components as well as optional JavaScript extensions. [Get Bootstrap](getbootstrap.com) <br>
Used for stylising frontend. 


## To do list 
1. Integrate Payment gateway 
2. Authenticate user using Google and Facebook
3. Integrating automatic mailing system to send conformation of order.
4. Improving frontend with better CSS and Javascript implementation 



