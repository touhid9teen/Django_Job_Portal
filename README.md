# Django Job Portal

A powerful and user-friendly **Job Portal** application API designed to connect candidates and employers. This platform provides essential features for job management, application tracking, and subscription services, making the hiring process seamless and efficient.

## 📚 Table of Contents
- [Django Job Portal](#django-job-portal)
  - [📚 Table of Contents](#-table-of-contents)
  - [🛠️ Introduction](#️-introduction)
  - [🏗️ Project Architecture](#️-project-architecture)
  - [🔒 Authentication and Authorization](#-authentication-and-authorization)
  - [✨ Features](#-features)
    - [Candidate Features](#candidate-features)
    - [Employer Features](#employer-features)
    - [Job Management](#job-management)
    - [Applications Management](#applications-management)
    - [Subscription Management](#subscription-management)
  - [⚙️ Installation](#️-installation)
  - [🚀 Usage](#-usage)
  - [🤝 Contributing](#-contributing)
  - [📄 License](#-license)

## 🛠️ Introduction
The **Django Job Portal** is a robust application API designed to streamline the recruitment process. It provides separate, tailored interfaces for candidates and employers, enabling job searching, posting, and application management. With subscription-based enhancements, this platform scales to meet diverse hiring needs.

## 🏗️ Project Architecture
The project is modular and organized for scalability:
- **Accounts**: Handles user authentication and profile management.
- **Candidates**: Features for job seekers, including profile creation and application tracking.
- **Employers**: Tools for employers to manage job postings and applications.
- **Jobs**: Comprehensive job management functionalities.
- **Applications**: Tracks job applications and candidate statuses.
- **Subscriptions**: Manages plans and benefits for premium features.



## Authentication and Authorization

### Authentication

Authentication is the process of verifying the identity of a user or system. It ensures that someone trying to access a system or perform an action is indeed who they claim to be. This Job Portal uses custom JWT authentication to verify identities.

#### What are JSON Web Tokens?

JWTs (JSON Web Tokens) are small, secure ways to share information between two parties. They act like digital ID cards for users, holding encoded details about who the user is and what they are allowed to do. Because JWTs contain all necessary information within them, they are well-suited for stateless authentication, meaning web apps don’t need to store extra data about users on the server.

#### Structure of a JWT

A JSON Web Token (JWT) comprises three main parts: a header, a payload, and a signature. These segments are Base64Url-encoded and concatenated with periods (.) to form the complete JWT.

- **Header**: The header is a JSON object that usually contains two fields: a token type (commonly JWT) and a signing algorithm (e.g., RS256 for RSA SHA-256). It provides details about how the JWT is encoded and secured.
- **Payload**: The payload is a JSON object containing claims and information about the user and other relevant data. Claims are key-value pairs and can be registered, public, or private.

     Common keys within JWT claims include:
     - `iss` (Issuer) — identifies the entity that issued the JWT.
     - `sub` (Subject) — identifies the user the token is for by storing the user’s unique identifier.
     - `aud` (Audience) — specifies the recipients allowed to process the token.
     - `exp` (Expiration Time) — defines when the token expires, in seconds since the Unix epoch.
     - `nbf` (Not Before) — defines the earliest time the token can be considered valid, in seconds since the Unix epoch.
     - `iat` (Issued At) — indicates when the token was issued in seconds since the Unix epoch.

- **Signature**: The signature is a cryptographic hash created using the encoded header, payload, and a secret key. It ensures the token’s integrity and authenticity. The encoded header and payload are concatenated with a period (.) and then hashed with the secret key, using a specified algorithm to generate the signature.

     Example of signature creation with RSA SHA-256:
     ```plaintext
     RSASHA256(
               base64UrlEncode(header) + "." +
               base64UrlEncode(payload),
               private_key
     )
     ```

What is Custom JWT Authentication? 
# Django Custom JWT Authentication

Custom JWT authentication means creating a personalized way of using JWTs (JSON Web Tokens) to fit the specific needs of a project. Instead of using ready-made tools (like `django-rest-framework-simplejwt`), we build our own methods for:

- **Creating tokens**: Choosing what information to include, setting custom expiration times, or using specific security algorithms (e.g., RSA for stronger security).
- **Checking tokens**: Writing our own methods to verify tokens to match special security needs or add extra checks.
- **Connecting with user data**: Adding specific user details or roles that fit the business logic of the project.

## Extending BaseAuthentication

Extending `BaseAuthentication` and overriding the `.authenticate(self, request)` method. The method should return a two-tuple of `(user, auth)` if authentication succeeds, or `None` otherwise. In some circumstances, instead of returning `None`, we may want to raise an `AuthenticationFailed` exception from the `.authenticate()` method.

### Reasons for Using Django Custom JWT Authentication

- **Flexibility**: Define token payload and structure according to our application's needs.
- **Enhanced Security**: Use custom algorithms, rotate signing keys, or implement more advanced claim verification.
- **Custom Claims**: Include project-specific claims like user roles, permissions, or other contextual data.
- **Integration with Microservices**: Implement JWTs with custom claims to manage multi-service authentication seamlessly.

## Authorization

Authorization in the context of software and web applications refers to the rights or access levels given to users that determine what actions they can perform within the system. Permissions are used to enforce security and control over who can read, write, update, or delete data.

- **Custom User-Based Permissions**: Permissions are handled based on the user type (candidate or employer), with role-based access to different resources. Used extending `BasePermission` class and override `has_permission` method.
- **Custom User Model**: The user model extends Django’s `AbstractUser`, managed by a custom `BaseUserManager` class to handle user registration, login, and profile management.
- **Email and Phone Login**: Allows users to log in using either email or phone number via a custom authentication backend.


## ✨ Features

### Candidate Features
- Profile creation and management.
- Search and apply for jobs.
- Track application statuses.

### Employer Features
- Post, edit, and manage job listings.
- Review candidate applications.
- Subscription-based access to premium tools.

### Job Management
- Advanced job filtering and searching.
- Secure job posting with detailed descriptions.

### Applications Management
- Centralized application tracking.
- Notifications for application updates.

### Subscription Management
- Multiple subscription tiers with premium benefits.
- Easy upgrades and secure payments.


## Account Management

### Custom User Model

Firstly, a custom Users model is created by extending Django's built-in `AbstractUser` class. A custom model manager, `UserManager`, is also created to handle user creation and superuser creation.

#### Why Custom User Model

- **Custom Fields**: We can add extra fields (e.g., phone number, address) to our user model.
- **Custom Logic**: We can implement custom behavior for user management (e.g., overriding user methods or validation rules).
- **Future Flexibility**: We can future-proof our project by having a more flexible user model that can be extended or modified easily.
- **Avoiding Migration Issues**: Starting with `AbstractUser` or a custom user model helps us avoid complex migration issues later if we decide to customize the default User model.

#### Why Model Manager

- **Custom Query Methods**: We can define custom query methods to encapsulate complex or reusable logic, making our code cleaner and more maintainable.
- **Enhanced Code Reusability**: We can centralize database queries within the manager, making it easy to reuse these methods across different parts of the project.
- **Separation of Concerns**: By moving query logic into a model manager, we keep the model itself focused on representing data, and improving code readability and organization.
- **Creating Custom Object Creation Methods**: We can override, extend default methods like `create_user()` or `create_superuser()` to customize how model instances are created.
- **Custom QuerySets**: We can attach custom `QuerySet` methods to provide a fluent and chainable interface for querying data.

## Base URL

The base URL for all API requests is: `https://127.0.0.1:8000` is defined as `{{base_url}}`.

### Basic Information

- **Authorization**: Bearer Token
- **Request and response type**: JSON

## User Registration

### Endpoint

`POST {{base_url}}/account/register/`

### Authentication

None (No authentication required for user registration)

### Function

Registers a new user by serializing the provided data and saving the user instance. After saving the user, a welcome email with an OTP is sent asynchronously using Celery.

### Query

Fetches the user data using the following PostgreSQL query:

```sql
INSERT INTO user (id, email, contract_number, user_type, password, otp) VALUES (id_value, email_value, contract_number_value, user_type_value, password_value, otp_value);
```

### Serialization

The `UserSerializer` is used to validate and serialize the incoming registration data. If the data is valid, the user is saved, and the OTP is generated. After successful registration, the OTP is sent via email asynchronously using Celery.

#### Validation inside serializer

- **Custom Field Validation**: Methods like `validate_email` and `validate_contract_number` are used for custom validation logic specific to each field.
- **Uniqueness Check**: Both the email and contract number are checked against the Users model to ensure they are unique before saving, preventing duplicates.
- **Password Validation**: The password field is marked as `write_only=True` (not returned in responses) and uses Django's built-in `validate_password` function to ensure the password meets Django's default password validation rules (such as length, complexity, etc.).
- **Format and Length Check**: For `contract_number`, additional checks are performed to ensure it has the correct length (11 digits) and proper format (digits only, with country code handling).
- **Error Handling**: If any validation rule fails, a `serializer.ValidationError` is raised with an appropriate error message, which will be returned in the response to the client.

### What is Celery?

Celery is an asynchronous task queue system used for managing background tasks. It allows applications to offload time-consuming operations to worker processes, improving performance and responsiveness.

#### Why Use Celery Here?

- **Asynchronous Processing**: Sending emails can take time, and handling it asynchronously prevents delays in the user registration API response.
- **Scalability**: Celery ensures that tasks like sending OTPs can scale efficiently, even under heavy traffic.
- **Reliability**: By leveraging Celery with a message broker like Redis, tasks can be queued and retried if failures occur.

### Request Body

The body of the POST request should include the necessary data for registering a user, typically containing fields such as `id`, `email`, `contract_number`, `user_type`, and `password`, as required by the custom user model.

```json
{
     "email": "user1@gmail.com",
     "contract_number": "017111111111",
     "user_type": "candidate",
     "password": "1234"
}
```

### Response 201 (Created)

Returns a success message with the generated OTP.

```json
{
   "status": "OTP has been generated",
   "otp": "755745"
}
```

### Response 400 (Bad Request)

Returns errors if the provided registration data is invalid.

```json
{
   "contract_number": [
        "Contract number must contain 11 digits (e.g., 01XXXXXXXXX)."
   ],
   "password": [
        "This password is too short. It must contain at least 8 characters.",
        "This password is too common.",
        "This password is entirely numeric."
   ]
}
```

# OTP Verification Process

## Endpoint
**POST** `{{base_url}}/account/verify_otp/`

## Function
Verifies the OTP and email combination for the user during registration. If valid, the user is marked as verified, and the registration process is completed.

## Request Body
The body of the POST request should include the `otp` and `email` fields.

## Query
The query fetches the user by matching the provided OTP and email from the database:
```sql
SELECT * FROM user WHERE email = request.data['email'] AND otp = request.data['otp'];
```

## Serialization
The request data is validated using the `OtpVerificationSerializer`. The serializer ensures the OTP is a 6-digit numeric value and that both the OTP and email exist in the database.

## Detailed Process

### User Registration
When a user completes the registration process, an OTP is generated automatically. The OTP is created inside the `save` method of the `Users` model using the `generate_otp()` function, which generates a random OTP of a specified length.

### OTP Generation
The `generate_otp()` function uses Python's `random.choice()` to generate a string of digits of length defined by `OTP_LENGTH`. This OTP is saved to the user model’s `otp` field.

### Celery Task for Sending OTP
After the OTP is generated and saved to the model, a Celery task (`send_welcome_email`) is triggered to send the OTP to the user’s email. This is done asynchronously using Celery, with Redis as the message broker. The task sends an email containing the OTP to the user.

### Celery Configuration
Celery is configured with Redis as the broker and result backend. The email backend is set up to use Gmail's SMTP server for sending OTP emails.

### OTP Verification
When the user submits the OTP (via the `ValidatedOtpView` API endpoint), the `OtpVerificationSerializer` is used to validate the OTP and email provided. If the OTP and email match the records in the database, the user’s `is_verified` field is set to `True`, and the OTP is marked as verified. A success message is then returned to confirm registration.

### Error Handling
If the OTP or email doesn’t match, or any error occurs during validation, appropriate error responses are returned. Additionally, if an exception occurs in the OTP validation process, an internal server error message is sent.

### Signals

#### Signal Definition
A custom signal `otp_verified` is defined using `Signal()` to handle actions after OTP verification.

#### Signal Triggering
The signal is triggered with `otp_verified.send(sender=user.__class__, instance=user)` after successfully verifying the OTP in the `ValidatedOtpView`.

#### Receiver Function
The `create_user_profile` function, decorated with `@receiver(otp_verified)`, listens for the signal and is triggered when the signal is sent.

#### Profile Creation
Inside the receiver function, based on the `user_type` ('candidate' or 'employer'), either a `CandidateProfile` or `EmployerProfile` is created and linked to the user.

#### Outcome
The signal ensures automatic profile creation for the user after successful OTP verification.

### Example Request Body
```json
{
     "otp": "765146",
     "email": "user1@gmail.com"
}
```

### Response 200 (OK)
Returns the success message if the OTP and email are valid and the user is successfully verified.
```json
{
     "status": "Registration successful"
}
```

### Response 400 (Bad Request)
Returns validation errors if the OTP or email combination is incorrect.
```json
{
     "otp": [
           "OTP does not exist."
     ],
     "email": [
           "Email does not exist."
     ]
}
```

### Response 500 (Internal Server Error)
Returns a generic error message if an unexpected error occurs during the OTP validation process.

---

# User Login

## Endpoint
**POST** `{{base_url}}/login/`

## Function
This view is used for logging in users with either their email or phone number and password. Upon successful login, a token is generated for the user.

## Query
The query fetches the user based on the provided `email_or_phone` value, matching it with either the `email` or `contract_number` field in the database:
```sql
SELECT * FROM user WHERE email = request.data['email_or_phone'] OR contract_number = request.data['email_or_phone'];
```

## Serialization
The request data is validated using the `LoginSerializer`. This serializer first checks whether the `email_or_phone` value is a valid email or phone number. It then ensures the provided credentials (password) match the authenticated user and that the user has been verified.

## Custom Login Process Using Email or Phone Authentication

### Custom Authentication Backend
A custom authentication backend called `EmailOrPhoneBackend` extends `ModelBackend` to allow users to log in using either an email or phone number.

### Username Check
The `authenticate` method checks if the username contains an '@' symbol to differentiate between email and phone number.

### User Retrieval
Depending on the input type, the method queries the `Users` model using either the `email` field or the `contract_number` field.

### Password Validation
The method verifies the provided password using the `user.check_password()` function.

### Return User
If the user exists and the password is valid, the user instance is returned; otherwise, `None` is returned.

### Configuration
Added `EmailOrPhoneBackend` to `AUTHENTICATION_BACKENDS` in Django settings to enable the custom authentication method.

## Custom Login Validation and Integration

### Fields Setup
A `LoginSerializer` class is created with fields `email_or_phone` and `password`. The `password` field is set to `write_only=True` for security.

### Custom Identifier Validation
In the `validate_identifier` method, an `EmailValidator()` is used to check if the input is an email. If validation fails, the input is checked if it’s an 11-digit number to verify if it’s a valid phone number. If neither check passes, a `ValidationError` is raised with a message prompting for a valid email or phone number.

### Context Flag Setting
Depending on the input type, flags are set in `self.context` as `is_email` or `is_phone` to use later during the authentication process. This helps determine how the `EmailOrPhoneBackend` should handle the input.

### Overall Validation Logic
In the `validate` method, `email_or_phone` and `password` are retrieved from the data dictionary.

### Dynamic Authentication Preparation
`auth_kwargs` is set up with `username` and `password` by default. If the input is identified as a phone number, `auth_kwargs` is adjusted to use `phone` instead of `username`. This step aligns with how the `EmailOrPhoneBackend` checks whether the input is an email or phone number for authentication.

### User Authentication
The `authenticate()` function is called using `auth_kwargs`, which interacts with the `EmailOrPhoneBackend`. This backend processes the input type accordingly and returns the user if authentication is successful. If `authenticate()` returns `None`, a `ValidationError` is raised for invalid credentials.

### Account Verification Check
If the user is found but not verified, a `ValidationError` is raised prompting the user to complete OTP verification.

### Final Return
If validation is successful, the user object is added to the data dictionary and returned for further processing.

## Custom Token Generation in Login Process

### Token Creation Function
A `token_generation` function is implemented to handle the creation of JWT tokens for authenticated users.

### Token Expiry Setup
An expiration time (`exp`) for the token is set to 30 minutes from the current time to ensure session security.

### Payload Structure
The token payload includes essential user information: `id`, `email`, `user_type`, and `contact_number` to support user identification and role-based logic.

### JWT Encoding
The `jwt.encode()` method is used with the payload, a `SECRET_KEY` for encryption, and the `HS256` algorithm to generate a secure token.

### Integration with Login
After successful user retrieval and validation in the `LoginView`, the `token_generation` function is called to create the token and include it in the response.

### Response Handling
The generated token is returned as an `access_token`, which the client can use for subsequent authenticated requests.

## Request Body
The body of the POST request should include `email_or_phone` (either email or phone number) and `password`.
```json
{
     "email_or_phone" : "user1@gmail.com",
     "password" : "qwer0987"
}
```

## Response 200 (OK)
Returns the generated access token if the user credentials are valid and the user is verified.
```json
{
     "access_token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpZCI6MTkzNCwiZW1haWwiOiJ1c2VyNzBAZ21haWwuY29tIiwidXNlcl90eXBlIjoiY2FuZGlkYXRlIiwiY29udGFjdF9udW1iZXIiOiIwMTcxMTExMTE3MCIsImV4cCI6MTczMTQ5NjI0OX0.jmR5bg3HXFMOIcMx3GhudjgkEo4dgKub18zxjj8atH4"
}
```

## Response 400 (Bad Request)
Returns validation errors if the input is invalid or the credentials do not match.
```json
{
     "error": "Token generation failed: Users matching query does not exist."
}
```

## Response 500 (Internal Server Error)
Returns a generic error message if an unexpected error occurs during the token generation process.



# API Documentation

## Get all User Profile Information

### Endpoint:
```
GET {{base_url}}/account/user_info/?page=1
```

### Parameters:
- `page_no`: The page number to retrieve. Optional, default is 1.
- `page_size`: The number of records per page. Optional, default is 2.

### Permission:
Open to all authenticated users.

### Function:
Fetches a list of users, including their details, paginated.

### Query:
Fetches all users from the user table, with pagination, using the following SQL query:
```sql
SELECT * FROM user LIMIT 10 OFFSET {page_offset};
```

### Serialization:
The users are serialized using the `UserDetailsProfileSerializer`, which includes a nested serializer for `user_details`. The `user_details` field fetches additional details based on the user's type (either candidate or employer), serialized using the `CandidateDetailsProfileSerializer` or `EmployerDetailsProfileSerializer` accordingly.

### Pagination:
- **Pagination Setup**: In the `UserInfoView`, the `PageNumberPagination` class handles pagination for the list of users.
- **Page Size**: Defined as 10 using `paginator.page_size = 10`.
- **Pagination Query**: Applied using `paginator.paginate_queryset(users, request)`.
- **Serializer**: The paginated queryset is passed to the `UserDetailsProfileSerializer` with `many=True`.
- **Returning Paginated Response**: Returned using `paginator.get_paginated_response(serializer.data)`.
- **Error Handling**: Wrapped in a try-except block to handle potential errors.

### UserInfoView with Nested Serializer:
- **View Setup**: Protected by custom authentication (`CustomAuthentication`).
- **Nested Serialization**: Uses `SerializerMethodField` for `user_details`:
     - If the user is a "candidate", retrieves and serializes using `CandidateSerializer`.
     - If the user is an "employer", retrieves and serializes using `EmployerProfileSerializer`.
     - Returns `None` if the associated profile is not found.
- **Error Handling**: Wrapped in a try-except block to catch unexpected errors.

### Response 200 (OK):
Returns a paginated list of user data, including their profile details.
```json
{
      "count": 4,
      "next": "http://127.0.0.1:8000/account/user_info/?page=2",
      "previous": null,
      "results": [
                {
                          "id": 2,
                          "email": "user2@gmail.com",
                          "contract_number": "017111111112",
                          "user_type": "employer",
                          "user_details": {
                                    "id": 1,
                                    "first_name": "Alice",
                                    "last_name": "Smith",
                                    "address": "456 Elm St, Chittagong, Bangladesh",
                                    "website": "https://www.alicesmithco.com",
                                    "company_name": "Alice Smith Solutions",
                                    "profile_picture": null,
                                    "user": 2
                          }
                },
                {
                          "id": 3,
                          "email": "user1@gmail.com",
                          "contract_number": "01711111111",
                          "user_type": "candidate",
                          "user_details": {
                                    "id": 1,
                                    "profile_details": {
                                              "id": 1,
                                              "resume": "/documents/resumes/Profile.pdf",
                                              "education": [
                                                        "Bachelor of Science in Computer Science - University of Springfield",
                                                        "Master of Science in Software Engineering - Tech University"
                                              ],
                                              "experience": [
                                                        "Software Developer at ABC Corp (2018-2021)",
                                                        "Lead Developer at XYZ Ltd (2021-Present)"
                                              ],
                                              "skills": [
                                                        "Python",
                                                        "Django",
                                                        "SQL"
                                              ],
                                              "languages": [
                                                        "English",
                                                        "Bangla"
                                              ],
                                              "projects": [
                                                        "E-commerce website development",
                                                        "Inventory management system"
                                              ],
                                              "certificate": [
                                                        "Certified Python Developer",
                                                        "AWS Certified Solutions Architect"
                                              ],
                                              "awards": [
                                                        "Employee of the Year 2020",
                                                        "Best Innovation Award 2021"
                                              ],
                                              "club_and_committee": [
                                                        "Tech Club President",
                                                        "Open Source Committee Member"
                                              ],
                                              "Competitive_exams": [
                                                        "GRE - Score: 320",
                                                        "TOEFL - Score: 110"
                                              ],
                                              "candidate": 1
                                    },
                                    "first_name": "Mr",
                                    "last_name": "Abc",
                                    "address": "123 Main St, Springfield, USA",
                                    "profile_pic": "/documents/profile_pictures/8.jpeg",
                                    "bio": "A highly motivated software engineer with a passion for developing innovative programs.",
                                    "social_links": [
                                              "https://linkedin.com/in/johndoe",
                                              "https://github.com/johndoe"
                                    ],
                                    "gender": "male",
                                    "birth_date": "1995-06-15",
                                    "user": 3
                          }
                }
      ]
}
```

## Get Login User Info

### Endpoint:
```
GET {{base_url}}/account/login-user-info/
```

### Permission:
Open to all authenticated users.

### Function:
Fetches the authenticated user's profile based on their `user_type` (either 'candidate' or 'employer').

### Query:
Fetches the user profile from the user table by using the user's ID, as provided by `request.user.id`, using the following SQL query:
```sql
SELECT * FROM user WHERE id = {request.user.id};
```

### Serialization:
The profile is serialized using either the `CandidateDetailsProfileSerializer` or `EmployerDetailsProfileSerializer`, depending on the `user_type`.

### Response 200 (OK):
Returns the authenticated user's profile data, including relevant details based on their `user_type`.
```json
{
      "data": {
                "id": 3,
                "email": "user1@gmail.com",
                "contract_number": "01711111111",
                "user_type": "candidate",
                "candidate": {
                          "id": 1,
                          "profile_details": {
                                    "id": 1,
                                    "resume": "/documents/resumes/Profile.pdf",
                                    "education": [
                                              "Bachelor of Science in Computer Science - University of Springfield",
                                              "Master of Science in Software Engineering - Tech University"
                                    ],
                                    "experience": [
                                              "Software Developer at ABC Corp (2018-2021)",
                                              "Lead Developer at XYZ Ltd (2021-Present)"
                                    ],
                                    "skills": [
                                              "Python",
                                              "Django",
                                              "SQL"
                                    ],
                                    "languages": [
                                              "English",
                                              "Bangla"
                                    ],
                                    "projects": [
                                              "E-commerce website development",
                                              "Inventory management system"
                                    ],
                                    "certificate": [
                                              "Certified Python Developer",
                                              "AWS Certified Solutions Architect"
                                    ],
                                    "awards": [
                                              "Employee of the Year 2020",
                                              "Best Innovation Award 2021"
                                    ],
                                    "club_and_committee": [
                                              "Tech Club President",
                                              "Open Source Committee Member"
                                    ],
                                    "Competitive_exams": [
                                              "GRE - Score: 320",
                                              "TOEFL - Score: 110"
                                    ],
                                    "candidate": 1
                          },
                          "first_name": "Mr",
                          "last_name": "Abc",
                          "address": "123 Main St, Springfield, USA",
                          "profile_pic": "/documents/profile_pictures/8.jpeg",
                          "bio": "A highly motivated software engineer with a passion for developing innovative programs.",
                          "social_links": [
                                    "https://linkedin.com/in/johndoe",
                                    "https://github.com/johndoe"
                          ],
                          "gender": "male",
                          "birth_date": "1995-06-15",
                          "user": 3
                }
      }
}
```

### Response 2:
```json
{
      "data": {
                "id": 2,
                "email": "user2@gmail.com",
                "contract_number": "017111111112",
                "user_type": "employer",
                "employer": {
                          "id": 1,
                          "first_name": "Alice",
                          "last_name": "Smith",
                          "address": "456 Elm St, Chittagong, Bangladesh",
                          "website": "https://www.alicesmithco.com",
                          "company_name": "Alice Smith Solutions",
                          "profile_picture": null,
                          "user": 2
                }
      }
}
```

### Response 404 (Not Found):
If the user is not found or there is an error, a 404 Not Found response is returned, with the error message.

## Update Password

### Endpoint:
```
PATCH {{base_url}}/account/update-password/
```

### Permission:
Open to authenticated users.

### Function:
Allows the authenticated user to change their password by providing the old password and new password.

### Query:
The password is updated by validating the old password and checking if the new password matches the confirmation. The query involves checking the current password of the user with the old password and then updating the password with the new one.
SQL query for updating the password:
```sql
UPDATE users
SET password = {new_password}
WHERE id = {request.user.id} AND password = {old_password};
```

### Serialization:
The `ChangePasswordSerializer` is used for validating the following fields:
- **Validation Logic**:
     - Check if the password and `confirm_password` match.
     - Validates `old_password` to ensure it matches the current password.
- **Password Update**:
     - `update()` sets the new password using `set_password()` and saves the user instance.
- **Success & Error Responses**:
     - Returns 200 OK on successful change with a success message.
     - Returns 400 BAD REQUEST if validation fails with detailed errors.

### Request Body:
```json
{
      "old_password": "1234",
      "password": "qwer0987",
      "confirm_password": "qwer0987"
}
```

### Response 200 (OK):
Returns a success message if the password change is successful.
```json
{
      "detail": "Password Change Successfully"
}
```

### Response 400 (Bad Request):
Returns validation errors if any of the fields are invalid.
```json
{
      "old_password": {
                "old_password": "Old password is incorrect"
      }
}
```
```json
{
      "password": [
                "Password field does not match"
      ]
}
```



Candidate Features

# Update Candidate Skills

**Endpoint:**  
`POST {{base_url}}/candidate/profile/`

**Permission:**  
Only accessible by candidates; restricted by the `IsCandidate` permission class.

**Function:**  
Updates the candidate profile based on the provided data. The profile is identified by the authenticated user's ID.

**Query:**  
Fetches the `CandidateProfile` for the authenticated user using the following PostgreSQL query:
```sql
SELECT * FROM candidate_profile WHERE user_id = request.user.id;
```

**Serialization:**  
The provided data is deserialized into a `CandidateProfile` instance using the `CandidateSerializer`.

**Request Body:**  
The request body should contain the fields to update the candidate profile:
```json
{
     "candidate": 1,
     "resume": "/documents/resumes/Profile.pdf",
     "education": [
           "Bachelor of Science in Computer Science - University of Springfield",
           "Master of Science in Software Engineering - Tech University"
     ],
     "experience": [
           "Software Developer at ABC Corp (2018-2021)",
           "Lead Developer at XYZ Ltd (2021-Present)"
     ],
     "skills": [
           "Python",
           "Django",
           "SQL"
     ],
     "languages": [
           "English",
           "Bangla"
     ],
     "projects": [
           "E-commerce website development",
           "Inventory management system"
     ],
     "certificate": [
           "Certified Python Developer",
           "AWS Certified Solutions Architect"
     ],
     "awards": [
           "Employee of the Year 2020",
           "Best Innovation Award 2021"
     ],
     "club_and_committee": [
           "Tech Club President",
           "Open Source Committee Member"
     ],
     "Competitive_exams": [
           "GRE - Score: 320",
           "TOEFL - Score: 110"
     ]
}
```

**Response 200 (OK):**  
Returns the updated candidate profile data if the update is successful.
```json
{
     "id": 1,
     "resume": "/documents/resumes/Profile.pdf",
     "education": [
           "Bachelor of Science in Computer Science - University of Springfield",
           "Master of Science in Software Engineering - Tech University"
     ],
     "experience": [
           "Software Developer at ABC Corp (2018-2021)",
           "Lead Developer at XYZ Ltd (2021-Present)"
     ],
     "skills": [
           "Python",
           "Django",
           "SQL"
     ],
     "languages": [
           "English",
           "Bangla"
     ],
     "projects": [
           "E-commerce website development",
           "Inventory management system"
     ],
     "certificate": [
           "Certified Python Developer",
           "AWS Certified Solutions Architect"
     ],
     "awards": [
           "Employee of the Year 2020",
           "Best Innovation Award 2021"
     ],
     "club_and_committee": [
           "Tech Club President",
           "Open Source Committee Member"
     ],
     "Competitive_exams": [
           "GRE - Score: 320",
           "TOEFL - Score: 110"
     ],
     "candidate": 1
}
```

**Response 400 (Bad Request):**  
Returns validation errors if the provided data is invalid.

**Response 404 (Not Found):**  
Returns an error message if the candidate profile for the authenticated user is not found.

**Response 500 (Internal Server Error):**  
Catches unexpected errors and returns a generic error message.

---

# Get All Candidate User Profiles

**Endpoint:**  
`GET {{base_url}}/candidate/profiles/`

**Authentication:**  
Custom authentication handled by `CustomAuthentication`.

**Permission:**  
Open to all users; no permission restrictions.

**Function:**  
Fetches all candidate profiles.

**Query:**  
Fetches all candidate profiles using the following PostgreSQL query:
```sql
SELECT * FROM candidate_profile;
```

**Serialization:**  
The candidate profiles are serialized using the `CandidateSerializer`, which includes a nested `CandidateSkillsSerializer` to handle the serialization of the skills associated with each candidate.

**Response 200 (OK):**  
Returns the list of all candidate profiles.
```json
[
     {
           "id": 3,
           "email": "user1@gmail.com",
           "contract_number": "01711111111",
           "user_type": "candidate",
           "candidate": {
                 "id": 1,
                 "profile_details": {
                         "id": 1,
                         "resume": "/documents/resumes/Profile.pdf",
                         "education": [
                               "Bachelor of Science in Computer Science - University of Springfield",
                               "Master of Science in Software Engineering - Tech University"
                         ],
                         "experience": [
                               "Software Developer at ABC Corp (2018-2021)",
                               "Lead Developer at XYZ Ltd (2021-Present)"
                         ],
                         "skills": [
                               "Python",
                               "Django",
                               "SQL"
                         ],
                         "languages": [
                               "English",
                               "Bangla"
                         ],
                         "projects": [
                               "E-commerce website development",
                               "Inventory management system"
                         ],
                         "certificate": [
                               "Certified Python Developer",
                               "AWS Certified Solutions Architect"
                         ],
                         "awards": [
                               "Employee of the Year 2020",
                               "Best Innovation Award 2021"
                         ],
                         "club_and_committee": [
                               "Tech Club President",
                               "Open Source Committee Member"
                         ],
                         "Competitive_exams": [
                               "GRE - Score: 320",
                               "TOEFL - Score: 110"
                         ],
                         "candidate": 1
                 },
                 "first_name": "Mr",
                 "last_name": "Abc",
                 "address": "123 Main St, Springfield, USA",
                 "profile_pic": "/documents/profile_pictures/8.jpeg",
                 "bio": "A highly motivated software engineer with a passion for developing innovative programs.",
                 "social_links": [
                         "https://linkedin.com/in/johndoe",
                         "https://github.com/johndoe"
                 ],
                 "gender": "male",
                 "birth_date": "1995-06-15",
                 "user": 3
           }
     },
     {
           "id": 4,
           "email": "user3@gmail.com",
           "contract_number": "01711111113",
           "user_type": "candidate",
           "candidate": {
                 "id": 2,
                 "profile_details": null,
                 "first_name": null,
                 "last_name": null,
                 "address": null,
                 "profile_pic": null,
                 "bio": null,
                 "social_links": null,
                 "gender": null,
                 "birth_date": null,
                 "user": 4
           }
     },
     {
           "id": 5,
           "email": "user4@gmail.com",
           "contract_number": "01711111114",
           "user_type": "candidate",
           "candidate": {
                 "id": 3,
                 "profile_details": null,
                 "first_name": null,
                 "last_name": null,
                 "address": null,
                 "profile_pic": null,
                 "bio": null,
                 "social_links": null,
                 "gender": null,
                 "birth_date": null,
                 "user": 5
           }
     }
]
```

**Response 400 (Bad Request):**  
Returns an error message if an unexpected error occurs.

---

# Get a Candidate User Profile

**Endpoint:**  
`GET {{base_url}}/candidate/profile/{candidate_id}/`

**Permission:**  
Open to all authenticated users.

**Function:**  
Fetches the candidate profile based on the provided `candidate_id`.

**Query:**  
Fetches the `CandidateProfile` by `candidate_id` using the following PostgreSQL query:
```sql
SELECT * FROM candidate_profile WHERE id = candidate_id;
```

**Serialization:**  
The candidate profile is serialized using the `CandidateSerializer`, which includes a nested `CandidateSkillsSerializer` for the skills field.

**Response 200 (OK):**  
Returns the candidate profile data if found.
```json
{
     "id": 3,
     "email": "user1@gmail.com",
     "contract_number": "01711111111",
     "user_type": "candidate",
     "candidate": {
           "id": 1,
           "profile_details": {
                 "id": 1,
                 "resume": "/documents/resumes/Profile.pdf",
                 "education": [
                         "Bachelor of Science in Computer Science - University of Springfield",
                         "Master of Science in Software Engineering - Tech University"
                 ],
                 "experience": [
                         "Software Developer at ABC Corp (2018-2021)",
                         "Lead Developer at XYZ Ltd (2021-Present)"
                 ],
                 "skills": [
                         "Python",
                         "Django",
                         "SQL"
                 ],
                 "languages": [
                         "English",
                         "Bangla"
                 ],
                 "projects": [
                         "E-commerce website development",
                         "Inventory management system"
                 ],
                 "certificate": [
                         "Certified Python Developer",
                         "AWS Certified Solutions Architect"
                 ],
                 "awards": [
                         "Employee of the Year 2020",
                         "Best Innovation Award 2021"
                 ],
                 "club_and_committee": [
                         "Tech Club President",
                         "Open Source Committee Member"
                 ],
                 "Competitive_exams": [
                         "GRE - Score: 320",
                         "TOEFL - Score: 110"
                 ],
                 "candidate": 1
           },
           "first_name": "Mr",
           "last_name": "Abc",
           "address": "123 Main St, Springfield, USA",
           "profile_pic": "/documents/profile_pictures/8.jpeg",
           "bio": "A highly motivated software engineer with a passion for developing innovative programs.",
           "social_links": [
                 "https://linkedin.com/in/johndoe",
                 "https://github.com/johndoe"
           ],
           "gender": "male",
           "birth_date": "1995-06-15",
           "user": 3
     }
}
```

**Response 404 (Not Found):**  
Returns an error message if the profile does not exist.

**Response 500 (Internal Server Error):**  
Catches unexpected errors and returns a generic error message.




# View Candidate Job Applications

### Endpoint:
`GET {{base_url}}/candidate/application/list/`

### Permission:
Restricted to authenticated candidates, enforced by `IsCandidate` permission class.

### Function:
Fetches the total number of job applications submitted by the authenticated candidate and returns the application data.

### Query:
Fetches job applications for the authenticated candidate using the following PostgreSQL query:
```sql
SELECT * FROM job_application WHERE candidate_id = request.user.candidate.id;
```
`request.user.candidate.id` refers to the id of the `CandidateProfile` associated with the currently authenticated user.

### Serialization:
The job applications are serialized using the `JobApplicationSerializer`.

### Response 200 (OK):
Returns the total number of applications and the data for each application submitted by the candidate.
```json
{
     "Total_Application": 3,
     "data": [
           {
                 "id": 1,
                 "application_date": "2024-11-09T15:33:42.201652Z",
                 "status": "applied",
                 "cover_letter": "I am very excited to apply for the Software Engineer role. I believe my skills and experience align perfectly with the requirements for this position.",
                 "resume": null,
                 "expected_salary": 75000.0,
                 "notice_period": "1 month",
                 "job": 3,
                 "candidate": 1
           },
           {
                 "id": 2,
                 "application_date": "2024-11-09T15:56:28.409689Z",
                 "status": "applied",
                 "cover_letter": "I am very excited to apply for the Software Engineer role. I believe my skills and experience align perfectly with the requirements for this position.",
                 "resume": null,
                 "expected_salary": 75000.0,
                 "notice_period": "1 month",
                 "job": 4,
                 "candidate": 1
           },
           {
                 "id": 3,
                 "application_date": "2024-11-09T16:02:09.322095Z",
                 "status": "applied",
                 "cover_letter": "I am very excited to apply for the Software Engineer role. I believe my skills and experience align perfectly with the requirements for this position.",
                 "resume": null,
                 "expected_salary": 75000.0,
                 "notice_period": "1 month",
                 "job": 5,
                 "candidate": 1
           }
     ]
}
```

### Response 400 (Bad Request):
Returns validation errors or any issues with the request.

### Response 500 (Internal Server Error):
Catches unexpected errors and returns a generic error message.

---

# Employer Features

## Get an Employer Profile by ID

### Endpoint:
`GET {{base_url}}/employer/profile/{employer_id}/`

### Permission:
Open to all users; no permission restrictions.

### Function:
Fetches the employer profile based on the provided `employer_id`.

### Query:
Fetches the `EmployerProfile` by `employer_id` using the following PostgreSQL query:
```sql
SELECT * FROM employer_profile WHERE id = employer_id;
```

### Serialization:
Converts the `EmployerProfile` instance into JSON format using the `EmployerProfileSerializer`.

### Response 200 (OK):
Returns the employer profile data if found.
```json
{
     "id": 2,
     "first_name": "Mr.",
     "last_name": "KKD",
     "address": "Dhaka, Bangladesh",
     "website": "https://www.kkd.ltd.com",
     "company_name": "Kazi & Kong Solutions Ltd",
     "profile_picture": null,
     "user": 6
}
```

### Response 404 (Not Found):
Returns an error message if the profile does not exist.

### Response 500 (Internal Server Error):
Catches unexpected errors and returns a generic error message.

---

## Get all Employer Profiles

### Endpoint:
`GET {{base_url}}/employer/profiles/`

### Permission:
Open to all users; no permission restrictions.

### Function:
Fetches all employer profiles.

### Query:
Fetches all `EmployerProfiles` using the following PostgreSQL query:
```sql
SELECT * FROM employer_profile;
```

### Serialization:
Converts the `EmployerProfile` instances into JSON format using the `EmployerProfileSerializer`.

### Response 200 (OK):
Returns a list of employer profile data.
```json
[
     {
           "id": 1,
           "first_name": "Alice",
           "last_name": "Smith",
           "address": "456 Elm St, Chittagong, Bangladesh",
           "website": "https://www.alicesmithco.com",
           "company_name": "Alice Smith Solutions",
           "profile_picture": null,
           "user": 2
     },
     {
           "id": 2,
           "first_name": "Mr.",
           "last_name": "KKD",
           "address": "Dhaka, Bangladesh",
           "website": "https://www.kkd.ltd.com",
           "company_name": "Kazi & Kong Solutions Ltd",
           "profile_picture": null,
           "user": 6
     }
]
```

### Response 404 (Not Found):
Returns an error message if the profile does not exist.

### Response 500 (Internal Server Error):
Catches unexpected errors and returns a generic error message.

---

## Update Profile

### Endpoint:
`PUT {{base_url}}/employer/profile/`

### Permission:
Only accessible by employers; restricted by the `IsEmployer` permission class.

### Function:
Updates the employer profile based on the provided data. The profile is identified by the authenticated user's ID.

### Query:
Fetches the `EmployerProfile` for the authenticated user using the following PostgreSQL query:
```sql
SELECT * FROM employer_profile WHERE user_id = request.user.id;
```

### Serialization:
Converts the provided data into an `EmployerProfile` instance and updates the profile using the `EmployerProfileSerializer`.

### Request Body:
The request body should contain the following fields to update the employer profile:
```json
{
     "user": 6,
     "first_name": "Mr.",
     "last_name": "KKD",
     "address": "Gulshan, Dhaka, Bangladesh",
     "website": "https://www.kkd.ltd.com",
     "company_name": "Kazi & Kong Solutions Ltd"
}
```

### Response 200 (OK):
Returns the updated employer profile data if the update is successful.
```json
{
     "id": 2,
     "first_name": "Mr.",
     "last_name": "KKD",
     "address": "Gulshan, Dhaka, Bangladesh",
     "website": "https://www.kkd.ltd.com",
     "company_name": "Kazi & Kong Solutions Ltd",
     "profile_picture": null,
     "user": 6
}
```

### Response 400 (Bad Request):
Returns validation errors if the provided data is invalid.

### Response 404 (Not Found):
Returns an error message if the employer profile for the authenticated user is not found.

### Response 500 (Internal Server Error):
Catches unexpected errors and returns a generic error message.

---

# Job Management

## Post a Job

### Endpoint:
`POST {{base_url}}/job/manage/`

### Permission:
Only accessible by employers; restricted by the `IsEmployer` permission class.

### Function:
Creates a new job using the provided data. The request is authenticated and validated before creating the job.

### Query:
Inserts a new job into the database using the following PostgreSQL query:
```sql
INSERT INTO job (employer_id, title, description, job_type, job_subtype, experience_level, company_name, location, salary_range, posted_at, deadline, application_link, application_email, is_deleted) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, NOW(), %s, %s, %s, %s);
```

### Serialization:
The provided data is deserialized into a `Job` instance using the `JobCreateSerializer`.

### Request Body:
The request body should contain the following fields to create a job:
```json
{
     "employer": 2,
     "title": "Software Engineer",
     "description": "Develop and maintain web applications.",
     "job_type": "Private",
     "job_subtype": "Full-time",
     "experience_level": "Mid",
     "company_name": "Tech Solutions Ltd.",
     "location": "New York, NY",
     "salary_range": "70,000 - 90,000 USD",
     "deadline": "2024-12-31T23:59:59",
     "application_link": "https://techsolutions.com/careers/software-engineer",
     "application_email": "jobs@techsolutions.com"
}
```

### Response 201 (Created):
Returns the created job data if the creation is successful.

### Response 400 (Bad Request):
Returns validation errors if the provided data is invalid.

### Response 500 (Internal Server Error):
Catches unexpected errors and returns a generic error message.

---

## Update a Job

### Endpoint:
`PATCH {{base_url}}/jobs/manage/{job_id}/`

### Permission:
Only accessible by employers; restricted by the `IsEmployer` permission class.

### Function:
Updates the details of an existing job using the provided data. The job is identified by `job_id` and is restricted to the authenticated employer.

### Query:
Fetches the job to update using the following PostgreSQL query:
```sql
SELECT * FROM job WHERE id = {job_id} AND employer_id = (SELECT id FROM employer_profile WHERE user_id = {request.user.id});
```

### Serialization:
The provided data is deserialized into the `Job` instance using the `JobSerializer`.

### Request Body:
The request body should contain the fields to update the job:
```json
{
     "title": "Sir Software Engineer",
     "description": "Develop.",
     "job_type": "Private",
     "job_subtype": "Full-time",
     "experience_level": "Senior",
     "company_name": "Tech Solutions Ltd.",
     "location": "New York, NY",
     "salary_range": "70,000 - 90,000 USD",
     "deadline": "2024-12-31T23:59:59",
     "application_link": "https://techsolutions.com/careers/software-engineer",
     "application_email": "jobs@techsolutions.com"
}
```

### Response 200 (OK):
Returns the updated job data if the update is successful.
```json
{
     "id": 10,
     "title": "Sir Software Engineer",
     "description": "Develop.",
     "job_type": "Private",
     "job_subtype": "Full-time",
     "experience_level": "Senior",
     "company_name": "Tech Solutions Ltd.",
     "location": "New York, NY",
     "salary_range": "70,000 - 90,000 USD",
     "posted_at": "2024-11-16T15:53:28.423515Z",
     "deadline": "2024-12-31T23:59:59Z",
     "application_link": "https://techsolutions.com/careers/software-engineer",
     "application_email": "jobs@techsolutions.com",
     "is_deleted": false,
     "employer": 2
}
```

### Response 400 (Bad Request):
Returns validation errors if the provided data is invalid.

### Response 404 (Not Found):
Returns an error message if the job with the given `job_id` for the authenticated employer is not found.

### Response 500 (Internal Server Error):
Catches unexpected errors and returns a generic error message.




# Delete a Job

**Endpoint**  
PUT `{{base_url}}/job/job_id/`

**Permission**  
Only accessible by employers; restricted by the `IsEmployer` permission class.

**Function**  
Deletes an existing job by marking it as deleted (`is_deleted = True`). The job is identified by `job_id` and must belong to the authenticated employer.

**Query**  
Fetches the job to delete using the following PostgreSQL query:
```sql
SELECT * FROM job WHERE id = {job_id} AND employer_id = (SELECT id FROM employer_profile WHERE user_id = {request.user.id});
```

**Response 200 (OK)**  
Indicates that the job has been successfully marked as deleted.
```json
{
     "error": "Job is deleted.",
     "data": {
           "id": 8,
           "title": "Software Engineer",
           "description": "Develop and maintain web applications.",
           "job_type": "Private",
           "job_subtype": "Full-time",
           "experience_level": "Mid",
           "company_name": "Tech Solutions Ltd.",
           "location": "New York, NY",
           "salary_range": "70,000 - 90,000 USD",
           "posted_at": "2024-11-16T15:42:41.738041Z",
           "deadline": "2024-12-31T23:59:59Z",
           "application_link": "https://techsolutions.com/careers/software-engineer",
           "application_email": "jobs@techsolutions.com",
           "is_deleted": true,
           "employer": 2
     }
}
```

**Response 400 (Bad Request)**  
Returns an error message if the job is already marked as deleted or if the authenticated user is not authorized to delete the job.

**Response 404 (Not Found)**  
Returns an error message if the job with the given `job_id` for the authenticated employer is not found.

**Response 500 (Internal Server Error)**  
Catches unexpected errors and returns a generic error message.

# Get a Job Post

**Endpoint**  
GET `{{base_url}}/job/`

**Permission**  
Only accessible by employers; restricted by the `IsEmployer` permission class.

**Function**  
Fetches all active jobs (`is_deleted = False`) created by the authenticated employer.

**Query**  
Retrieves the employer's jobs using the following PostgreSQL query:
```sql
SELECT * FROM job WHERE is_deleted = FALSE AND employer_id = (SELECT id FROM employer_profile WHERE user_id = {request.user.id});
```

**Serialization**  
The retrieved Job instances are serialized into JSON format using the `JobSerializer`. This serializer includes a nested `EmployerProfileSerializer`, which retrieves and includes information about the employer (the user who created the job).

**Response 200 (OK)**  
Returns the total number of jobs and a list of job details if jobs are found.
```json
{
     "id": 3,
     "employer": {
           "id": 1,
           "first_name": "Alice",
           "last_name": "Smith",
           "address": "456 Elm St, Chittagong, Bangladesh",
           "website": "https://www.alicesmithco.com",
           "company_name": "Alice Smith Solutions",
           "profile_picture": null,
           "user": 2
     },
     "total_applications": 1,
     "title": "Software Engineer",
     "description": "Develop and maintain web applications.",
     "job_type": "Private",
     "job_subtype": "Full-time",
     "experience_level": "Mid",
     "company_name": "Tech Solutions Ltd.",
     "location": "New York, NY",
     "salary_range": "70,000 - 90,000 USD",
     "posted_at": "2024-11-09T14:33:14.149197Z",
     "deadline": "2024-12-31T23:59:59Z",
     "application_link": "https://techsolutions.com/careers/software-engineer",
     "application_email": "jobs@techsolutions.com",
     "is_deleted": false
}
```

**Response 404 (Not Found)**  
Returns an error message if no jobs are found for the authenticated employer.

**Response 500 (Internal Server Error)**  
Catches unexpected errors and returns a generic error message.

# Search Job

## Job Filtering and Search Implementation

**Endpoint**  
GET `{{base_url}}/job/search/?title=Software Engineer`

**Permission**  
Requires authentication via the `CustomAuthentication` class. Accessible by authorized users with the appropriate permissions.

**Function**  
Filters and retrieves job listings. Applies the filtering logic using `DjangoFilterBackend` and custom filter logic defined in the `JobFilter`.

**Query**  
Fetches jobs using the following query:
```sql
SELECT * FROM job WHERE is_deleted = FALSE;
```
Then, applies additional filtering based on the query parameters, such as job type, experience level, etc. This is done by the `filter_queryset` method in the `DjangoFilterBackend` class.

**Serialization**  
The retrieved Job instances are serialized into JSON format using the `JobDetailSerializer`. The serializer includes details about the employer who created the job and the total number of applications for each job.

## Job Filtering and Pagination

- **Utilize Django Filters**: Set up `DjangoFilterBackend` and defined a `JobFilter` class with customizable filters for fields like title, job_type, job_subtype, experience_level, and location for flexible search options.
- **Filter Application**: Applied filtering logic in the `get()` method by using `DjangoFilterBackend().filter_queryset()` to refine job listings based on user queries.
- **Implement Pagination**: Used `PageNumberPagination` with a `page_size` of 10, allowing segmented data retrieval and improving load times for users.
- **Serialize Paginated Data**: Used `JobDetailSerializer` to convert paginated job data into JSON format for the response, making the data easily consumable.
- **Handle No Results Gracefully**: Added error handling to return a 404 response when no jobs match the filter criteria.
- **Modular and Configurable Settings**: Configured `REST_FRAMEWORK` settings to include the default authentication and filter backends, as well as pagination, enabling consistency and code modularity.

**Response 200 (OK)**  
Returns a list of jobs with pagination and the total number of jobs after applying the filters.
```json
{
     "total_jobs": 2,
     "data": [
           {
                 "id": 3,
                 "employer": {
                         "id": 1,
                         "first_name": "Alice",
                         "last_name": "Smith",
                         "address": "456 Elm St, Chittagong, Bangladesh",
                         "website": "https://www.alicesmithco.com",
                         "company_name": "Alice Smith Solutions",
                         "profile_picture": null,
                         "user": 2
                 },
                 "total_applications": 1,
                 "title": "Software Engineer",
                 "description": "Develop and maintain web applications.",
                 "job_type": "Private",
                 "job_subtype": "Full-time",
                 "experience_level": "Mid",
                 "company_name": "Tech Solutions Ltd.",
                 "location": "New York, NY",
                 "salary_range": "70,000 - 90,000 USD",
                 "posted_at": "2024-11-09T14:33:14.149197Z",
                 "deadline": "2024-12-31T23:59:59Z",
                 "application_link": "https://techsolutions.com/careers/software-engineer",
                 "application_email": "jobs@techsolutions.com",
                 "is_deleted": false
           },
           {
                 "id": 9,
                 "employer": {
                         "id": 1,
                         "first_name": "Alice",
                         "last_name": "Smith",
                         "address": "456 Elm St, Chittagong, Bangladesh",
                         "website": "https://www.alicesmithco.com",
                         "company_name": "Alice Smith Solutions",
                         "profile_picture": null,
                         "user": 2
                 },
                 "total_applications": 0,
                 "title": "Software Engineer",
                 "description": "Develop and maintain web applications.",
                 "job_type": "Private",
                 "job_subtype": "Full-time",
                 "experience_level": "Mid",
                 "company_name": "Tech Solutions Ltd.",
                 "location": "New York, NY",
                 "salary_range": "70,000 - 90,000 USD",
                 "posted_at": "2024-11-16T15:44:41.140585Z",
                 "deadline": "2024-12-31T23:59:59Z",
                 "application_link": "https://techsolutions.com/careers/software-engineer",
                 "application_email": "jobs@techsolutions.com",
                 "is_deleted": false
           }
     ]
}
```

**Response 400 (Bad Request)**  
Returns validation errors if the request contains invalid or missing parameters.

**Response 404 (Not Found)**  
Returns an error message if no jobs are found matching the criteria.

**Response 500 (Internal Server Error)**  
Catches unexpected errors and returns a generic error message.

# Get Logged-In User’s Jobs

**Endpoints**  
GET `{{base_url}}/job/`  
GET `{{base_url}}/job/{job_id}/`

**Permission**  
Only accessible by authenticated users with proper permissions, as determined by the `CustomAuthentication` class.

**Function**  
Fetches details of a specific job by its ID. The job's details are serialized, and the total number of applications for the job is calculated.

**Query**  
Fetches the job details using the following query:
```sql
SELECT * FROM job WHERE id = job_id AND is_deleted = FALSE;
```
Then, it uses the `JobDetailSerializer` to serialize the job data and also includes the total number of applications for the job.

**Serialization**  
The retrieved Job instance is serialized into JSON format using the `JobDetailSerializer`. This includes the job details and the total number of applications for that job, calculated by the `get_total_applications` method.

**Response 200 (OK)**  
Returns the detailed job data along with the total number of applications for the job.
```json
{
     "Total Job": 2,
     "jobs": [
           {
                 "id": 8,
                 "title": "Software Engineer",
                 "description": "Develop and maintain web applications.",
                 "job_type": "Private",
                 "job_subtype": "Full-time",
                 "experience_level": "Mid",
                 "company_name": "Tech Solutions Ltd.",
                 "location": "New York, NY",
                 "salary_range": "70,000 - 90,000 USD",
                 "posted_at": "2024-11-16T15:42:41.738041Z",
                 "deadline": "2024-12-31T23:59:59Z",
                 "application_link": "https://techsolutions.com/careers/software-engineer",
                 "application_email": "jobs@techsolutions.com",
                 "is_deleted": false,
                 "employer": 2
           },
           {
                 "id": 10,
                 "title": "Sir Software Engineer",
                 "description": "Develop.",
                 "job_type": "Private",
                 "job_subtype": "Full-time",
                 "experience_level": "Senior",
                 "company_name": "Tech Solutions Ltd.",
                 "location": "New York, NY",
                 "salary_range": "70,000 - 90,000 USD",
                 "posted_at": "2024-11-16T15:53:28.423515Z",
                 "deadline": "2024-12-31T23:59:59Z",
                 "application_link": "https://techsolutions.com/careers/software-engineer",
                 "application_email": "jobs@techsolutions.com",
                 "is_deleted": false,
                 "employer": 2
           }
     ]
}
```

**Response 400 (Bad Request)**  
If the request contains invalid data, this response is returned.

**Response 404 (Not Found)**  
If no job is found for the given job ID, this error is returned.

**Response 500 (Internal Server Error)**  
Catches unexpected errors and returns a generic error message.


 Applications Management

# Django Job Portal API Documentation

## View All Applications for a Job

### Endpoint
`GET {{base_url}}/application/all/3/`

### Permission
Only accessible by authenticated employers who created the job, as determined by the `IsEmployer` permission class.

### Function
Fetches all job applications for a specific job and provides the job application details, including job and candidate information. It uses caching to improve performance.

### Query
Fetches job applications using the query:
```sql
SELECT * FROM job_application WHERE job_id = job_id AND is_deleted = FALSE;
```

### Caching
The response data is cached with a cache key formatted as `job_applications_{job_id}`. If the job applications are already cached, the cached data is returned immediately, improving response times. If the job applications are not cached, they are fetched from the database, serialized, and cached for future use.

### Serialization
The retrieved job applications are serialized into JSON format using the `JobApplicationCandidateDetailsSerializer`. This serializer includes nested serializers to provide detailed information about the job and candidate.

- The `job` field uses the `JobSerializer` to include details about the job that was applied for.
- The `candidate` field uses the `CandidateSerializer` to include information about the candidate who applied.

### Request Body
No request body is required for this endpoint as it retrieves job applications.

### Response 200 (OK)
Returns the list of job applications for the given job. If the data is cached, it is returned directly from the cache. If not cached, the applications are retrieved from the database, serialized, and cached.

```json
{
     "data": [
           {
                 "id": 1,
                 "job": {
                         "id": 3,
                         "title": "Software Engineer",
                         "description": "Develop and maintain web applications.",
                         "job_type": "Private",
                         "job_subtype": "Full-time",
                         "experience_level": "Mid",
                         "company_name": "Tech Solutions Ltd.",
                         "location": "New York, NY",
                         "salary_range": "70,000 - 90,000 USD",
                         "posted_at": "2024-11-09T14:33:14.149197Z",
                         "deadline": "2024-12-31T23:59:59Z",
                         "application_link": "https://techsolutions.com/careers/software-engineer",
                         "application_email": "jobs@techsolutions.com",
                         "is_deleted": false,
                         "employer": 1
                 },
                 "candidate": {
                         "id": 1,
                         "profile_details": {
                               "id": 1,
                               "resume": "/documents/resumes/Profile.pdf",
                               "education": [
                                     "Bachelor of Science in Computer Science - University of Springfield",
                                     "Master of Science in Software Engineering - Tech University"
                               ],
                               "experience": [
                                     "Software Developer at ABC Corp (2018-2021)",
                                     "Lead Developer at XYZ Ltd (2021-Present)"
                               ],
                               "skills": [
                                     "Python",
                                     "Django",
                                     "SQL"
                               ],
                               "languages": [
                                     "English",
                                     "Bangla"
                               ],
                               "projects": [
                                     "E-commerce website development",
                                     "Inventory management system"
                               ],
                               "certificate": [
                                     "Certified Python Developer",
                                     "AWS Certified Solutions Architect"
                               ],
                               "awards": [
                                     "Employee of the Year 2020",
                                     "Best Innovation Award 2021"
                               ],
                               "club_and_committee": [
                                     "Tech Club President",
                                     "Open Source Committee Member"
                               ],
                               "Competitive_exams": [
                                     "GRE - Score: 320",
                                     "TOEFL - Score: 110"
                               ],
                               "candidate": 1
                         },
                         "first_name": "Mr",
                         "last_name": "Abc",
                         "address": "123 Main St, Springfield, USA",
                         "profile_pic": "/documents/profile_pictures/8_1u3Sq8J.jpeg",
                         "bio": "A highly motivated software engineer with a passion for developing innovative programs.",
                         "social_links": [
                               "https://linkedin.com/in/johndoe",
                               "https://github.com/johndoe"
                         ],
                         "gender": "male",
                         "birth_date": "1995-06-15",
                         "user": 3
                 },
                 "application_date": "2024-11-09T15:33:42.201652Z",
                 "status": "applied",
                 "cover_letter": "I am very excited to apply for the Software Engineer role. I believe my skills and experience align perfectly with the requirements for this position.",
                 "resume": null,
                 "expected_salary": 75000.0,
                 "notice_period": "1 month"
           },
           {
                 "id": 4,
                 "job": {
                         "id": 3,
                         "title": "Software Engineer",
                         "description": "Develop and maintain web applications.",
                         "job_type": "Private",
                         "job_subtype": "Full-time",
                         "experience_level": "Mid",
                         "company_name": "Tech Solutions Ltd.",
                         "location": "New York, NY",
                         "salary_range": "70,000 - 90,000 USD",
                         "posted_at": "2024-11-09T14:33:14.149197Z",
                         "deadline": "2024-12-31T23:59:59Z",
                         "application_link": "https://techsolutions.com/careers/software-engineer",
                         "application_email": "jobs@techsolutions.com",
                         "is_deleted": false,
                         "employer": 1
                 },
                 "candidate": {
                         "id": 2,
                         "profile_details": null,
                         "first_name": null,
                         "last_name": null,
                         "address": null,
                         "profile_pic": null,
                         "bio": null,
                         "social_links": null,
                         "gender": null,
                         "birth_date": null,
                         "user": 4
                 },
                 "application_date": "2024-11-16T16:44:48.978237Z",
                 "status": "applied",
                 "cover_letter": "I am very excited to apply for the Software Engineer role. I believe my skills and experience align perfectly with the requirements for this position.",
                 "resume": "/documents/resumes/Profile_u2RvErU.pdf",
                 "expected_salary": 75000.0,
                 "notice_period": "1 month"
           },
           {
                 "id": 5,
                 "job": {
                         "id": 3,
                         "title": "Software Engineer",
                         "description": "Develop and maintain web applications.",
                         "job_type": "Private",
                         "job_subtype": "Full-time",
                         "experience_level": "Mid",
                         "company_name": "Tech Solutions Ltd.",
                         "location": "New York, NY",
                         "salary_range": "70,000 - 90,000 USD",
                         "posted_at": "2024-11-09T14:33:14.149197Z",
                         "deadline": "2024-12-31T23:59:59Z",
                         "application_link": "https://techsolutions.com/careers/software-engineer",
                         "application_email": "jobs@techsolutions.com",
                         "is_deleted": false,
                         "employer": 1
                 },
                 "candidate": {
                         "id": 2,
                         "profile_details": null,
                         "first_name": null,
                         "last_name": null,
                         "address": null,
                         "profile_pic": null,
                         "bio": null,
                         "social_links": null,
                         "gender": null,
                         "birth_date": null,
                         "user": 4
                 },
                 "application_date": "2024-11-16T16:46:44.704249Z",
                 "status": "applied",
                 "cover_letter": "I am very excited to apply for the Software Engineer role. I believe my skills and experience align perfectly with the requirements for this position.",
                 "resume": "/documents/resumes/Profile_nhQlDo2.pdf",
                 "expected_salary": 75000.0,
                 "notice_period": "1 month"
           }
     ]
}
```

### Response 400 (Bad Request)
If the user is not authorized to view the job applications or the request is invalid, this response is returned.

### Response 404 (Not Found)
If no job application data is found for the given job ID, this error is returned.

### Response 500 (Internal Server Error)
Catches unexpected errors and returns a generic error message.

---

## Submit a Job Application

### Endpoint
`POST {{base_url}}/application/job_id/`

### Permission
Only accessible by authenticated candidates, as determined by the `IsCandidate` permission class.

### Function
This endpoint allows candidates to apply for a job. Before creating a new application, the system checks if the candidate has already applied for the same job by querying the cache. If a cached result is found indicating the candidate has already applied, a response with the status "Already Applied" is returned. If no cached result is found, the system checks the database for any existing application. If the candidate has already applied, the result is cached, and the "Already Applied" response is returned. Otherwise, a new application is created, and the data is serialized and saved.

### Query
The query checks if the candidate has already applied to the job:
```sql
SELECT * FROM job_application WHERE candidate_id = {user_id} AND job_id = {job_id};
```

### Caching
The result of the application check is cached using the key `job_application_{user_id}_{job_id}`. If the candidate has already applied, the cache will store the response, and subsequent requests will return the cached result. If the candidate has not applied, a new job application is created, and the result is cached for future requests.

### Serialization
The data is serialized into JSON format using the `JobApplicationSerializer`. This serializer includes all relevant job application details, such as candidate and job information.

### Request Body
The request body must include the necessary details to create a job application. It typically includes information about the candidate and the job they are applying for.

```json
{
 "job": 3,
 "candidate": 2,
 "status": "applied",
 "cover_letter": "I am very excited to apply for the Software Engineer role. I believe my skills and experience align perfectly with the requirements for this position.",
 "resume": "path/to/resume.pdf",
 "expected_salary": 75000.00,
 "notice_period": "1 month"
}
```

### Response 200 (OK)
If the candidate has already applied for the job, a response with the following message is returned:
```json
{
     "status": "Already Applied"
}
```

### Response 201 (Created)
If the job application is successfully created, the response contains the serialized data of the new job application.
```json
{
     "id": 4,
     "application_date": "2024-11-16T16:44:48.978237Z",
     "status": "applied",
     "cover_letter": "I am very excited to apply for the Software Engineer role. I believe my skills and experience align perfectly with the requirements for this position.",
     "resume": "/documents/resumes/Profile_u2RvErU.pdf",
     "expected_salary": 75000.0,
     "notice_period": "1 month",
     "job": 3,
     "candidate": 2
}
```

### Response 400 (Bad Request)
If the request data is invalid or the job application fails validation, this response returns the serializer's validation errors.

### Response 404 (Not Found)
If the job ID does not exist in the database, this error will be returned with a message indicating that the job could not be found.

### Response 500 (Internal Server Error)
Catches unexpected errors and returns a generic error message.

---

## Update Application Status

### Endpoint
`PATCH {{base_url}}/application/status/application_id/`

### Permission
Only accessible by authenticated employers who created the job, as determined by the `IsEmployer` permission class.

### Function
Updates the status of a specific job application. This view ensures that only the employer who posted the job can update the application status. The status choices are limited to predefined options: "applied", "selected", "interviewed", "offered", and "rejected". Caching is used to optimize future requests for the same application status.

### Query
The query to update the application status in the database is:
```sql
UPDATE job_application 
SET status = {new_status} 
WHERE id = {application_id} 
AND job_id = {job_id};
```

The status field is updated based on the new value provided in the request. The allowed values for status are drawn from the `STATUS_CHOICES` field: 'applied', 'selected', 'interviewed', 'offered', and 'rejected'.

### Update Function
When the employer updates the status:
- The application is retrieved from the database using the `application_id`.
- The employer's identity is verified to ensure they created the job for which the application was submitted.
- The status of the job application is updated based on the provided status in the request data, and the change is saved to the database.

### Caching
The response data is cached with a cache key formatted as `job_application_status_{application_id}`. If the status is updated, the new status is saved and cached for future use. If a cached status exists, it is updated to reflect the latest change.

### Serialization
The status update process focuses only on the status field, so no full serialization of the job application is required. The status is validated against `STATUS_CHOICES`.

### Request Body
The request body should contain the status to be updated. The allowed values are:
- "applied"
- "selected"
- "interviewed"
- "offered"
- "rejected"

```json
{
     "status": "selected"
}
```

### Response 200 (OK)
Returns a success message indicating that the job application's status was successfully updated. The new status is also cached for future requests.
```json
{
     "message": "Job Application's Status is updated."
}
```

### Response 400 (Bad Request)
If the employer is not authorized to update the job application status or if the status provided is invalid (not one of the `STATUS_CHOICES`), this response is returned with a message indicating that the update is not allowed.

### Response 404 (Not Found)
If no job application is found with the given `application_id`, this error is returned with an error message.

### Response 500 (Internal Server Error)
Catches unexpected errors and returns a generic error message.


# View a Job Application

## Endpoints
**GET** `{{base_url}}/application/status/application_id/`

### Permission
Only accessible by authenticated employers who created the job, as determined by the `IsEmployer` permission class.

### Function
Fetches all job applications for a specific job and provides the details of each job application, including job and candidate information. Caching is utilized to improve performance and reduce the database load for repeated requests.

### Query
The query to fetch the job applications from the database:
```sql
SELECT * FROM job_application WHERE job_id = {job_id};
```
The query retrieves all job applications for the specific job identified by `job_id`.

### Caching
The response data is cached with a cache key formatted as `job_applications_{job_id}`. If the job applications are already cached, the cached data is returned immediately to improve response time. If the job applications are not cached, they are fetched from the database, serialized, and then cached for future requests.

### Serialization
The job applications are serialized into JSON format using the `JobApplicationCandidateDetailsSerializer`. This includes job details, candidate information, and any other application-related data.

### Response 200 (OK)
Returns a list of job applications for the specified job. The data is either returned from the cache if it exists or fetched from the database and cached for future use.
```json
{
     "data": {
           "id": 1,
           "job": {
                 "id": 1140,
                 "employer": {
                         "id": 1255,
                         "first_name": "Alice",
                         "last_name": "Smith",
                         "address": "456 Elm St, Chittagong, Bangladesh",
                         "website": "https://www.alicesmithco.com",
                         "company_name": "Alice Smith Solutions",
                         "profile_picture": null,
                         "user": 1833
                 },
                 "title": "full-stack Developer",
                 "description": "Design and implement user interface components for web applications.",
                 "job_type": "Private",
                 "job_subtype": "Contract",
                 "experience_level": "Entry",
                 "company_name": "Creative Code Inc.",
                 "location": "San Francisco, CA",
                 "salary_range": "5500000.0",
                 "posted_at": "2024-10-28T08:35:46.569199Z",
                 "deadline": "2024-11-15T23:59:59Z",
                 "application_link": "https://creativecode.com/careers/frontend-developer",
                 "application_email": "careers@creativecode.com",
                 "is_deleted": false
           },
           "candidate": {
                 "id": 1,
                 "skills": {
                         "id": 1,
                         "resume": null,
                         "education": [
                               "Bachelor of Science in Computer Science from XYZ University",
                               "High School Diploma from ABC High School"
                         ],
                         "experience": [
                               "Software Engineer at Tech Solutions Ltd. (2 years)",
                               "Intern at Web Innovators Inc. (6 months)"
                         ],
                         "skills": [
                               "Python",
                               "Django",
                               "REST APIs",
                               "JavaScript",
                               "React.js",
                               "SQL"
                         ],
                         "languages": [
                               "English",
                               "Spanish"
                         ],
                         "projects": [
                               "Developed an E-commerce website using Django and React",
                               "Built a microservices architecture for a financial application"
                         ],
                         "certificate": [
                               "Certified AWS Solutions Architect",
                               "Microsoft Certified Azure Developer"
                         ],
                         "awards": [
                               "Employee of the Month at Tech Solutions Ltd.",
                               "Dean's List at XYZ University"
                         ],
                         "club_and_committee": [
                               "Member of the Coding Club at XYZ University",
                               "Volunteer at Local Community Center"
                         ],
                         "Competitive_exams": [
                               "GRE with a score of 320",
                               "TOEFL with a score of 110"
                         ],
                         "candidate": 1
                 },
                 "first_name": "Mr",
                 "last_name": "Ten",
                 "address": "Dhaka, Bangladesh",
                 "profile_pic": "/documents/profile_pictures/images_NIMZ6NU.jpeg",
                 "bio": "Software engineer with 2 years of experience in full-stack development.",
                 "social_links": [
                         "https://www.linkedin.com/in/mrten",
                         "https://github.com/mrten"
                 ],
                 "gender": "male",
                 "birth_date": "1999-01-19",
                 "user": 1837
           },
           "application_date": "2024-10-28T09:23:31.506082Z",
           "status": "Selected",
           "cover_letter": "I am excited to apply for this position as I believe my skills match the job requirements.",
           "resume": null,
           "accepted_salary": null,
           "notice_period": null
     }
}
```

### Response 400 (Bad Request)
If the user is not authorized to view the job applications or if the request is invalid, this response is returned.

### Response 404 (Not Found)
If no job application data is found for the given job ID, this error is returned.

### Response 500 (Internal Server Error)
Catches unexpected errors and returns a generic error message.

---

# Subscription Management

## Add a Subscription Plan

### Endpoints
**POST** `{{base_url}}/subscription/plan/`

### Permission
Only accessible by authenticated admins, as determined by the `IsAdmin` permission class.

### Function
Creates a new subscription plan by accepting the subscription data in the request body. If the data is valid, it is saved, and the subscription plan is created. If the data is invalid, it returns the corresponding error message.

### Query
The subscription data is inserted into the database with a query like:
```sql
INSERT INTO subscription_plan (plan_name, duration, price, features) 
VALUES ({plan_name}, {duration}, {price}, {features});
```

### Serialization
The request data is serialized using the `SubscriptionSerializer`, which ensures that the incoming data matches the structure of the `SubscriptionPlan` model.

### Request Body
The body of the request should contain the subscription plan details. This is validated by the `SubscriptionSerializer`.
```json
{
     "id": 7,
     "name": "free",
     "price": "0.00",
     "description": "Free plan with basic access to job portal features.",
     "features": "Limited job applications, No priority support, No career coaching",
     "duration": "00:00:00",
     "max_job_applications_per_day": 5,
     "priority_support": false,
     "career_coaching": false,
     "create_at": "2024-11-10T12:00:00Z",
     "update_at": "2024-11-10T07:54:38.517365Z"
}
```

### Response 201 (Created)
If the subscription plan is successfully created, a response containing the newly created subscription plan data is returned with a 201 Created status.
```json
{
     "detail": "Password Change Successfully"
}
```

### Response 400 (Bad Request)
If the request data is invalid or does not meet the model’s requirements, a 400 Bad Request response with the validation errors is returned.

---

## View all Subscription Plans

### Endpoints
**GET** `{{base_url}}/subscription/plan/`

### Permission
Accessible by authenticated users (permissions can be adjusted as needed, based on the use case).

### Function
Fetches and returns all subscription plans from the database. It retrieves the subscription data and serializes it for the response.

### Query
The query to fetch all subscription plans from the database:
```sql
SELECT * FROM subscription_plan;
```

### Serialization
The retrieved subscription plans are serialized into JSON format using the `SubscriptionSerializer`.

### Response 200 (OK)
Returns the list of all subscription plans in the database, serialized in JSON format.
```json
[
     {
           "id": 7,
           "name": "free",
           "price": "0.00",
           "description": "Free plan with basic access to job portal features.",
           "features": "Limited job applications, No priority support, No career coaching",
           "duration": "00:00:00",
           "max_job_applications_per_day": 5,
           "priority_support": false,
           "career_coaching": false,
           "create_at": "2024-11-10T12:00:00Z",
           "update_at": "2024-11-10T07:54:38.517365Z"
     },
     {
           "id": 8,
           "name": "basic",
           "price": "9.99",
           "description": "Basic plan with access to essential features.",
           "features": "10 job applications per day, No priority support, No career coaching",
           "duration": "30 00:00:00",
           "max_job_applications_per_day": 10,
           "priority_support": false,
           "career_coaching": false,
           "create_at": "2024-11-10T12:00:00Z",
           "update_at": "2024-11-10T07:54:50.480339Z"
     },
     {
           "id": 9,
           "name": "professional",
           "price": "49.99",
           "description": "Professional plan with advanced features.",
           "features": "20 job applications per day, Priority support, Career coaching",
           "duration": "30 00:00:00",
           "max_job_applications_per_day": 20,
           "priority_support": true,
           "career_coaching": true,
           "create_at": "2024-11-10T12:00:00Z",
           "update_at": "2024-11-10T07:55:02.362213Z"
     },
     {
           "id": 10,
           "name": "premium",
           "price": "99.99",
           "description": "Premium plan with exclusive features.",
           "features": "50 job applications per day, Priority support, Career coaching, Resume review",
           "duration": "30 00:00:00",
           "max_job_applications_per_day": 50,
           "priority_support": true,
           "career_coaching": true,
           "create_at": "2024-11-10T12:00:00Z",
           "update_at": "2024-11-10T07:55:13.833878Z"
     },
     {
           "id": 11,
           "name": "enterprise",
           "price": "199.99",
           "description": "Enterprise plan for large organizations with all-inclusive features.",
           "features": "Unlimited job applications per day, 24/7 priority support, Career coaching, Resume review, Analytics",
           "duration": "30 00:00:00",
           "max_job_applications_per_day": 100,
           "priority_support": true,
           "career_coaching": true,
           "create_at": "2024-11-10T12:00:00Z",
           "update_at": "2024-11-10T07:55:23.958759Z"
     }
]
```

### Response 400 (Bad Request)
In case of an unexpected error (such as a database error or general failure), this response is returned with an error message.

---

# Apply A Subscription Plan

## Endpoints
**POST** `{{base_url}}/subscription/add/plan/`

### Permission
Accessible by authenticated users (the `CustomAuthentication` class is used for authentication).

### Function
Allows users to choose a subscription plan and save it in the database. The subscription details are validated and stored for the user.

### Validating Subscription
The method checks if the plan is provided and the `trial_start_date` is not set.

### Setting Trial Start Date
If the conditions are met, it calculates the `trial_start_date` by adding the plan's duration to the `start_date` field.

### Saving Data
After the necessary validation and modification, the method saves the subscription details to the database by calling `super().save()`.

### Query
The query to insert the chosen subscription plan into the database (assuming it's stored in a `UserSubscription` model):
```sql
INSERT INTO user_subscription (user_id, subscription_plan_id, start_date, end_date, status) 
VALUES ({user_id}, {subscription_plan_id}, {start_date}, {end_date}, {status});
```

### Serialization
The provided subscription data is serialized into the `UserSubscription` model using the `SubscriptionPlanSerializer`.

### Request Body
The request body should contain the subscription details to be saved, including the subscription plan ID, start date, end date, and any other necessary data.
```json
{
     "user": 1837,
     "plan": 8
}
```

### Response 201 (Created)
Returns the data of the newly created subscription in JSON format.
```json
{
     "id": 3,
     "start_date": "2024-11-19T09:06:02.359796Z",
     "auto_renew": true,
     "has_expired": false,
     "is_active": true,
     "trial_start_date": "2024-12-19T09:06:02.359796Z",
     "created_at": "2024-11-19T09:06:02.359957Z",
     "updated_at": "2024-11-19T09:06:02.359963Z",
     "user": 1837,
     "plan": 8
}
```

### Response 400 (Bad Request)
If the data is invalid or the subscription cannot be saved, this response will include error details.

---

# Update a Subscription Plan

## Endpoints
**PUT** `{{base_url}}/subscription/plan/{plan_id}/`

### Permission
Only accessible by authenticated admins, as determined by the `IsAdmin` permission class.

### Function
Updates an existing subscription plan with the provided data in the request body. If the data is valid, the subscription plan is updated in the database. If the data is invalid, it returns the corresponding error message.

### Query
The query to update the subscription plan in the database:
```sql
UPDATE subscription_plan SET plan_name = {plan_name}, duration = {duration}, price = {price}, features = {features} WHERE id = {plan_id};
```

### Serialization
The request data is serialized using the `SubscriptionSerializer`, which ensures that the incoming data matches the structure of the `SubscriptionPlan` model.

### Request Body
The body of the request should contain the updated subscription plan details. This is validated by the `SubscriptionSerializer`.
```json
{
     "name": "premium",
     "price": "99.99",
     "description": "Premium plan with exclusive features.",
     "features": "50 job applications per day, Priority support, Career coaching, Resume review",
     "duration": "30 00:00:00",
     "max_job_applications_per_day": 50,
     "priority_support": true,
     "career_coaching": true
}
```

### Response 200 (OK)
If the subscription plan is successfully updated, a response containing the updated subscription plan data is returned with a 200 OK status.

### Response 400 (Bad Request)
If the request data is invalid or does not meet the model’s requirements, a 400 Bad Request response with the validation errors is returned.

### Response 404 (Not Found)
If the subscription plan with the specified ID does not exist, a 404 Not Found response is returned.

---

# What is a Cron Job?

A cron job is a time-based job scheduler in Unix-like operating systems, which I use to run tasks automatically at specified intervals or times.

## How Does It Work in Django?
I use `django-cron`, a third-party package, to integrate cron jobs into my Django project. I define the logic for the job in a class that inherits from `CronJobBase`, and I specify a schedule (like every 10 minutes). The `do()` method contains the code I want to run when the cron job executes.

### Example Breakdown
In the cron job example, it runs every 10 minutes (`Schedule(run_every_mins=10)`). It checks all active subscriptions (`UserSubscription.objects.filter(is_active=True)`).

- If the trial date has passed and auto_renew is enabled:
  - I update the `start_date` and `trial_start_date`.
- If auto_renew is disabled:
  - I mark the subscription as expired (`has_expired = True`) and inactive (`is_active = False`).

### Key Benefits
- I can automate recurring tasks.
- It saves me time and resources by handling background processes for me.
- I can customize the intervals (e.g., minutes, hours, days) to fit my needs.


## ⚙️ Installation
Follow these steps to set up the project locally:

1. **Clone the repository**:
      ```bash
      https://github.com/touhid9teen/JobPortal
      ```
2. **Navigate to the project directory**:
      ```bash
      cd Django_Job_Portal
      ```
3. **Create a virtual environment**:
      ```bash
      python3 -m venv env
      ```
4. **Activate the virtual environment**:
      - On Windows:
           ```bash
           .\env\Scripts\activate
           ```
      - On macOS/Linux:
           ```bash
           source env/bin/activate
           ```
5. **Install the required dependencies**:
      ```bash
      pip install -r requirements.txt
      ```
6. **Apply the migrations**:
      ```bash
      python manage.py migrate
      ```
7. **Create a superuser**:
      ```bash
      python manage.py createsuperuser
      ```
8. **Run the development server**:
      ```bash
      python manage.py runserver
      ```

## 🚀 Usage
Open your browser and visit:
```arduino
http://127.0.0.1:8000/
```
Log in using the superuser credentials created during setup. Explore the features of the Django Job Portal.

## 🤝 Contributing
We welcome contributions! To get started:

1. **Fork the repository**.
2. **Create a new branch**:
      ```bash
      git checkout -b feature-branch
      ```
3. **Make your changes and commit them**:
      ```bash
      git commit -m "Description of your changes"
      ```
4. **Push your changes to the branch**:
      ```bash
      git push origin feature-branch
      ```
5. **Open a pull request for review**.

## 📄 License
This project is licensed under the MIT License. See the LICENSE file for details.
