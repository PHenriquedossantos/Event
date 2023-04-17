<h1>Event Registration System</h1>
<p>This is a Django-based project for event registration. It allows users to sign up and login, create new events, participate in events, and retrieve participation certificates.</p>

Installation
To run the project, first, clone the repository:

bash
Copy code
git clone https://github.com/your-username/event-registration-system.git
Then, navigate to the project's directory:

bash
Copy code
cd event-registration-system
Setting up a virtual environment
It's recommended to use a virtual environment to manage dependencies for this project. To set up a virtual environment, you can use the following command:

bash
Copy code
python3 -m venv env
Activate the virtual environment:

bash
Copy code
source env/bin/activate
Installing dependencies
To install the project's dependencies, use the following command:

bash
Copy code
pip install -r requirements.txt
Running the application
To run the project, navigate to the project's directory and activate the virtual environment (if using one), then run the following command:

bash
Copy code
python manage.py runserver
Endpoints
Main App Endpoints
The main app's endpoints are:

+ /admin/: Django's admin site
+ /usuarios/: Users app
+ /eventos/: Events app
+ /cliente/: Client app
Users App Endpoints
The users app's endpoints are:

+ /usuarios/cadastro/: User registration
+ /usuarios/login/: User login
Events App Endpoints
The events app's endpoints are:

+ /eventos/novo_evento/: Create a new event
+ /eventos/gerenciar_evento/: Manage an event
+ /eventos/inscrever_evento/<int:id>/: Register for an event
+ /eventos/participantes_evento/<int:id>/: Get the list of participants for an event
+ /eventos/gerar_csv/<int:id>/: Generate a CSV file for an event
+ /eventos/certificados_evento/<int:id>/: Get the list of certificates for an event
+ /eventos/gerar_certificado/<int:id>/: Generate a certificate for an event
+ /eventos/procurar_certificado/<int:id>/: Search for a certificate for an event
Certificates App Endpoints
The certificates app's endpoints are:

+ /certificados/meus_certificados/: Get a list of the user's certificates.
