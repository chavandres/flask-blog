# Chapter 3 Web Forms Notes
This chapter implements web forms to accept inputs from users.

## Configuration Variables
You can define configuration variables to be pulled from the OS environment variables. By creating a config module in the project root, create a *Config* class with all the configuration variables that are required by the application. With help of the `os` module, you can load environment variables into your application.

## WTForms and Flask-WTF Extension
In order to build forms in Flask easily, use a combination of the `wtforms` and `flask_wtf` modules. Use the `wtforms` to create a skeleton of the attributes of your form. This allows for better customization of each field. The `flask_wtf` module will build the specified `wtforms` in a proper way for Flask applications.

## Loading fields to templates
Using Jinja, you can load the form's attributes such as the label and field type into the templates. This is achived by passing the form object to the `render_template()` function. <br>
By adding logic to the templates, errors can also be displayed when there are validation errors.

## Flash messages
In Flask an application can show messages to users. These messages can be passed to the `flash()` method, which is part of the `flash` module. An important note is that the flash messages ***need*** to be rendered by the template engine otherwise the users won't be seeing them in their browser.<br>
To display the messages in a webpage, call `get_flashed_messages()` function in the template. Once the messages have been called by the method, the list will get cleared, meaning that messages will only be displayed once. A common practice is to render the messages using a *for* loop.



