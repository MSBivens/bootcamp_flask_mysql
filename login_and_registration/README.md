Instructions for the Login and Registraion assignment:

1. Create a new Flask project
2. Create a new MySQL database with a table and the appropriate fields
3. The root route should display a template with the login and registrations forms
4. Validate the registration input
5. If registration is invalid errors messages should be displayed on the index page
6. If registrations is valid, hash the password and save the user in the database, store the user in session and then redirect to the success page
7. Validate the login input
8. If the login is invalid, display an error message on the index page
9. If login is valid, store the user in session and then redirect to the success page
10. Add a functioning logout button to the success page that clears session
11. After logging out, ensure you cannot reach the success page
12. NINJA Bonus: Add an additional validation on passwords to have a least 1 number and 1 uppercase letter
13. SENSEI Bonus: Add additional input types on the form. Get creative with you validations! (Consider including a date picker, radio buttons and/or checkboxes)