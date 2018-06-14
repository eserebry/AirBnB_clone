## Clone of the AirBnB website
## First step: Command interpreter to manage AirBnB objects.

![Image of Holberton B&B Logo](https://s3.amazonaws.com/intranet-projects-files/holbertonschool-higher-level_programming+/263/HBTN-hbnb-Final.png)

### Description
Create a parent class, called BaseModel, to take care of the initialization, serialization and deserialization of future instances\
Create a simple flow of serialization/deserialization: Instance <-> Dictionary <-> JSON string <-> file\
Create all classes used for AirBnB (User, State, City, Place…) that inherit from BaseModel\
Create the first abstracted storage engine of the project: File storage.\
Create all unittests to validate all our classes and storage engine

### Environment
Interpreter was developed and tested on Ubuntu 14.04 LTS via Vagrant in VirtualBox.

### File Contents
The repository contains the following files:

|   **File**   |   **Description**   |
| -------------- | --------------------- |
|console.py | Command interpreter |
|file_storage.py | Instansens are being serialised to a JSON-string and deserialised back |
|base_model.py | Defines all common attributes/methods for other classes |
|amenity.py | A class Amenity that inherits from BaseModel |
|city.py | A class City that inherits from BaseModel |
|place.py | A class Place that inherits from BaseModel |
|review.py | A class Review that inherits from BaseModel |
|state.py | A class State that inherits from BaseModel |
|user.py | A class User that inherits from BaseModel |
|tests\| Containes Unit Tests for the progect |
|README.md | readme file |
|AUTHORS | autor file |

### Function Descriptions
| **Function** | **Description** |
| -------------- | ----------------- |
|EOF | Exit the program |
|quit | Exit the program |
|help | Help function |
|create | Creates a new instance of BaseModel, saves it and prints the id |
|show | Prints the string representation of an instance based on the class name and id |
|destroy | Deletes an instance based on the class name and id |
|all | Prints all string representation of all instances based or not on the class name |
|update | Updates an instance based on the class name and id by adding or updating attribute |

### Usage and Istallation
Clone the repository
```
git clone https://github.com/Andkeil/AirBnB_clone.git
```

Executable console.py can be run by typing:

```
$ ./console.py
```

### Authors
This progect was created by:\
Andrew Keil: https://github.com/Andkeil \
Elena Serebryakova: https://github.com/eserebry 
