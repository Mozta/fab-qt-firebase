
# Qt-Firebase Interface

This is a project that consists of a graphical interface created in QT Designer, which is converted to a .py file using the pyuic5 command. The generated file is used as the design and imported into another file that contains the program logic. Additionally, the project is integrated with Firebase to send data to Firestore.



## Installation

Before getting started, make sure you have Python 3.x and PyQt5 installed on your system.

1. Clone the repository to your local machine.


```bash
  git clone https://github.com/Mozta/fab-qt-firebase.git
```
    

2. Navigate to the project folder and run the following command to install the necessary dependencies:


```bash
  cd qt-firebase
  pip install -r requirements.txt
```


3. Create an account on Firebase and set up your project. Then, download the configuration file in JSON format and place it in the root of the project with the name "serviceAccountKey.json".

4. Run the main file to start the application.

```bash
  python main.py
```


## Project Structure

The project has the following structure:

```bash
  interfacesFab
│   ├── app.py
│   ├── base_logica.py
│   ├── interfaz.ui
│   ├── requirements.txt
│   ├── serviceAccountKey.json
│   └── ui.py
```