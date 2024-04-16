# Basic Authentication Project

## Table of Contents
- [Description](#description)
- [Resources](#resources)
- [Learning Objectives](#learning-objectives)
- [Requirements](#requirements)
- [Tasks](#tasks)
  - [Simple-basic-API](#simple-basic-api)
  - [Error handler: Unauthorized](#error-handler-unauthorized)
  - [Error handler: Forbidden](#error-handler-forbidden)
  - [Auth class](#auth-class)
  - [Define which routes don't need authentication](#define-which-routes-dont-need-authentication)
  - [Request validation!](#request-validation)
  - [Basic auth](#basic-auth)
  - [Basic - Base64 part](#basic---base64-part)
  - [Basic - Base64 decode](#basic---base64-decode)
  - [Basic - User credentials](#basic---user-credentials)
  - [Basic - User object](#basic---user-object)
  - [Basic - Overload current_user - and BOOM!](#basic---overload-current_user---and-boom)

## Description
In this project, you will learn about Basic Authentication and its implementation on a simple API. You'll explore various concepts such as authentication mechanisms, Base64 encoding, HTTP headers, and more.

## Resources
Read or watch:
- [REST API Authentication Mechanisms](https://www.youtube.com/watch?v=501dpx2IjGY)
- [Base64 in Python](https://docs.python.org/3.7/library/base64.html)
- [HTTP header Authorization](https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/Authorization)
- [Flask Documentation](https://palletsprojects.com/p/flask/)
- [Base64 - Concept](https://en.wikipedia.org/wiki/Base64)

## Learning Objectives
By the end of this project, you should be able to explain:
- What authentication means
- What Base64 is and how to encode a string in Base64
- What Basic authentication means and how to send the Authorization header

## Requirements
### Python Scripts
- All your files will be interpreted/compiled on Ubuntu 18.04 LTS using python3 (version 3.7)
- All your files should end with a new line
- The first line of all your files should be exactly `#!/usr/bin/env python3`
- A `README.md` file, at the root of the folder of the project, is mandatory
- Your code should use the `pycodestyle` style (version 2.5)
- All your files must be executable
- The length of your files will be tested using `wc`
- All your modules should have documentation
- All your classes should have documentation
- All your functions (inside and outside a class) should have documentation

## Tasks

### Simple-basic-API
- **Objective:** Download and start your project from the provided archive. Setup and start the server.

### Error handler: Unauthorized
- **Objective:** Implement an error handler for HTTP status code 401.

### Error handler: Forbidden
- **Objective:** Implement an error handler for HTTP status code 403.

### Auth class
- **Objective:** Create a class to manage API authentication.

### Define which routes don't need authentication
- **Objective:** Update the Auth class to define routes that don't need authentication.

### Request validation!
- **Objective:** Validate all requests to secure the API.

### Basic auth
- **Objective:** Create a class for Basic Authentication.

### Basic - Base64 part
- **Objective:** Implement methods to handle Base64 encoding in Basic Authentication.

### Basic - Base64 decode
- **Objective:** Implement methods to decode Base64 in Basic Authentication.

### Basic - User credentials
- **Objective:** Implement methods to extract user credentials in Basic Authentication.

### Basic - User object
- **Objective:** Implement a method to get the User object in Basic Authentication.

### Basic - Overload current_user - and BOOM!
- **Objective:** Overload the current_user method to retrieve the User instance for a request in Basic Authentication.

## Copyright
© 2024 ALX. All rights reserved.
