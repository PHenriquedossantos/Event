<h1>Event Registration Project</h2>
<h2>This project is a web application built using Django, a Python web framework. The project allows users to register and manage events.</h2>

Requirements.txt
To install the required packages, run the following command:
## pip install -r requirements.txt
+ asgiref==3.6.0
+ Django==4.2
+ Pillow==9.5.0
+ sqlparse==0.4.3
+ tzdata==2023.3


Endpoints
<h3>Main app</h3>
+ /admin/ - Django admin site
+ /usuarios/ - App for user registration and login
+ /eventos/ - App for event management
+ /cliente/ - App for client management

App usuarios
+ /usuarios/cadastro/ - Page for user registration
+ /usuarios/login/ - Page for user login
<h3>App eventos</h3>
+ /eventos/novo_evento/ - Page for creating a new event
+ /eventos/gerenciar_evento/ - Page for managing an event
+ /eventos/inscrever_evento/<int:id>/ - Page for registering for an event
+ /eventos/participantes_evento/<int:id>/ - Page for managing participants in an event
+ /eventos/gerar_csv/<int:id>/ - Endpoint for generating a CSV file for an event
+ /eventos/certificados_evento/<int:id>/ - Page for managing certificates for an event
+ /eventos/gerar_certificado/<int:id>/ - Endpoint for generating a certificate for a participant in an event
+ /eventos/procurar_certificado/<int:id>/ - Page for searching for a certificate for a participant in an event

Views
App usuarios
+ cadastro(request)
<p>This function handles the user registration process. It takes in a request object and returns a rendered cadastro.html page or redirects the user to the cadastro page with error messages if there was an issue with the user input.

+ login(request)
<p>This function handles the user login process. It takes in a request object and returns a rendered login.html page or redirects the user to the login page with error messages if there was an issue with the user input.

App eventos
+ novo_evento(request)
<p>This function handles the creation of a new event. It takes in a request object and returns a rendered novo_evento.html page or redirects the user to the novo_evento page with error messages if there was an issue with the user input.

+ gerenciar_evento(request)
<p>This function handles the management of an event. It takes in a request object and returns a rendered gerenciar_evento.html page.

+ inscrever_evento(request, id)
<p>This function handles the registration process for an event. It takes in a request object and the id of the event to register for and returns a rendered inscrever_evento.html page or redirects the user to the inscrever_evento page with error messages if there was an issue with the user input.

+ participantes_evento(request, id)
<p>This function handles the management of participants for an event. It takes in a request object and the id of the event to manage and returns a rendered participantes_evento.html page.

+ gerar_csv(request, id)
This function handles the generation of a CSV file for an event. It takes in a request object and the id of the event to generate the CSV file for and returns the CSV file as a response.

+ certificados_evento(request, id)
<p>This function handles the management of certificates for an event. It takes in a request object and the id of the event to manage and returns a rendered certificados_evento.html page.

+ gerar_certificado(request, id)
This function handles
