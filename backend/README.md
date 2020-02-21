# Backend

## Setup:
I terminalen:
- Kjør `pip install pipenv`
- Kjør `pipenv shell`
- Kjør `pipenv install` 
- cd til "backend"
- Kjør `python manage.py migrate` (oppdaterer databasen)

## Kjøre server
I terminalen:
- cd til "backend"
- Kjør `python manage.py runsever`


##Problem med server/migrations:
- Slett migrations-mappen i marketplace og slett databasefilen db.sqlite3
- Kjør `python manage.py makemigrations` og `python manage.py migrate`

## Hvordan gjøre http requests
Forsikre deg om at databasen er oppdatert med å kjøre `python manage.py migrate`
## Med postman:
-Last ned postman fra https://www.postman.com/downloads/
#### Opprette en bruker
- Skriv inn URL http://localhost:8000/marketplace/users/
- Velg "POST"
- I "Headers" velg key = Content-Type og Value = application/json
- I "Body" skriv 
```json
{ 

    "username": "bruker",
    "phone": "12345678",
    "first_name": "F_navn",
    "last_name": "E_navn",
    "email": "din@mail.no",
    "password": "passord123",
    "re_password": "passord123"

}
```

Dersom alt gikk som det skal, får du 
````json
{
    "username": "bruker",
    "phone": "12345678",
    "first_name": "F_navn",
    "last_name": "E_navn",
    "email": "din@mail.no",
    "id": 1
}
````
Og en http melding `201 Created`

#### Logge inn / lage en token
- Skriv inn URL http://localhost:8000/marketplace/token/login/
- Velg "POST"
- I "Headers" velg key = Content-Type og Value = application/json
- I "Body" skriv 
```json
{
	"email": "din@email.no",
	"password": "passord"
}
```
Dersom alt gikk som det skal, får du en token

```json
{
    "token": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VyX2lkIjozLCJ1c2VybmFtZSI6Impvc3RlaWh0IiwiZXhwIjoxNTgyMTA5OTU5LCJlbWFpbCI6IiJ9.J6uuTxUnDPfMDSd-xW2AYAdImzC9OXV0_5IWogSzXco"
}
```

#### Logge ut / fjerne token fra databasen
- Skriv inn URL http://localhost:8000/marketplace/token/logout/
- I "Headers" velg key = Authorization og Value = Token  *Lim inn token* 
- for eksempel Value = Token 5deb22977408dab3c92204bfafb2bca88c11a986
- Send POST request
- Nå skal Token være slettet, kan sjekke på http://127.0.0.1:8000/admin/authtoken/token/ om man er logget inn som admin (superuser) på serveren.

## I nettleseren:
#### Opprette en bruker
- Gå til http://127.0.0.1:8000/marketplace/users/
- Fyll inn i HTML-formen
- Trykk POST

#### Få tak i Token
- Gå til http://127.0.0.1:8000/marketplace/token/login/
- Skriv inn email og passord
- Trykk POST

#### Logge ut / slette token
- Ikke sikker, bruk postman


