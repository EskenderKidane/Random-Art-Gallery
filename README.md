# Random Art Gallery
#### Video Demo:  https://youtu.be/lSsN9PHzKMk
#### Description: A python program that will return a random artwork using Art Institute of Chicago API. The artwork and its details is then displayed in a simple webpage.

&nbsp;

#### Try it:
- Clone this repo
- Install requirements.txt
- Run the command "flask run"

&nbsp;

### Details
#### This project utilizes python backend to make API calls to the Art Institute of Chicago and retrieve relevant data. This is implemented in project.py. The program begins by randomly selecting one out of 500 artwork objects, reads and stores JSON data for that specific artwork. Key libraries used are Random and Requests.

&nbsp;

#### Next, the app.py script helps render the contents in basic HTML/CSS webpage. app.py is a simple part of the project but plays a good role as it uses the Flask Framework to render project.py on a minimal webpage.
