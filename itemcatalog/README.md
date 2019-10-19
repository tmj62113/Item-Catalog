Item-Catalog-Project
====================
This project is a web application that provides a list of items within a variety of categories and
integrates third party user registration and authentication. 
Authenticated users have the ability to add, edit and delete items. 

The database contains a listing of the top seven nutrient and mineral deficiencies in the United States
and a listing of foods that can counteract those imbalances.

## Set Up Instructions
Follow these instructions to set up the Vagrant Linux Environment and the Item Catalog Project

### Prerequisite Resources
You will need the following Python resources for it to run:
<ul>
  <li>Python 3.5 or above (https://www.python.org/downloads/).
  <li>Git (https://git-scm.com/downloads).
  <li>Vagrant (https://www.vagrantup.com/).
  <li>VirtualBox (https://www.virtualbox.org/wiki/Downloads).
  <li>Sqlalchemy (https://www.sqlalchemy.org/download.html).
</ul>

You will need the following other resources for it to run:
<ul>
  <li>Flask (http://flask.pocoo.org/).
  <li>Httplib2 (https://pypi.python.org/pypi/httplib2/0.10.3).
  <li>Oauth2client (https://pypi.python.org/pypi/oauth2client/).
  <li>Web browser i.e. Chrome (https://www.google.com/chrome/)
</ul>

### Installation

<ul>
  <li>Install Git (https://git-scm.com/downloads) on the local machine
  <li>Install Python 3.5 or above (https://www.python.org/downloads/) on the local machine
  <li>Install VirtualBox (https://www.virtualbox.org/wiki/Downloads) on the local machine
  <li>Install Vagrant (https://www.vagrantup.com/) on the local machine
</ul>

### Preparing the Virtual Machine
<ol>
  <li>Download and save a copy of the zipped folder to your local machine.
  <li>Navigate to the directory on your local machine containing the saved files.
  <li>Run the command 'vagrant up' to download and install the linux operating system.
  <li>Run the command 'vagrant ssh' to log in to the virtual machine.
  <li>Install Flask (http://flask.pocoo.org/) with pip install Flask, if it is not installed already.
  <li>Install Sqlalchemy, Httplib2 and Oauth2client with sudo apt-get install, if they are not installed already.
  <li> CD  /vagrant will provide access to files on virtual machine.
 </ol>

### Create the Database

Navigate to cd item-catalog-project:

Run the command python3 database_setup.py to create the database.

### Populate the Database
Run the command python3 lotsofmenus.py to populate the database.

### Run the Project
Run the command python3 project.py to run the project.
In your browser visit http://localhost:5000.

### Contents of the Project
The application establishes a simple item-catalog database with an ability to add, edit and delete items.

The Item Catalog allows:
<ul>
  <li>Page implements Google Accounts, a third-party authentication & authorization service
  <li> Add, edit and delete a deficiency
  <li>Add, edit and delete a food item
</ul>

## Author
Tiffany Jensen


## Acknowledgments
[Udacity](https://www.udacity.com/) for the resources that helped me develop this.
The findings of this study can be found at: [OregonStateStudy](https://lpi.oregonstate.edu/mic/micronutrient-inadequacies/overview)
Supplemental information was provided by the following resources: Healing Foods by DK [HealingFoods](https://www.penguinrandomhouse.com/books/359817/healing-foods-by-dk-publishing/), Rawsome by Brigitte Mars [Rawesome](https://brigittemars.com/event/herbs-for-womens-health/attachment/rawsome/) and 
The Organic Food Shopper's Guide by Jeff Cox, [OrganicFoodShoppersGuide](http://www.jeffcox.net/)
