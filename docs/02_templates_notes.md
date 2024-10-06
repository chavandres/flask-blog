# Chapter 2 Templates Notes
This chapter covers using dynamic templates in Flask using Jinja.

## Templates
By creating a folder named *templates* you can have reusable pieces of HTML code that you can render.

## The render_template() function
By calling `render_template()` you can invoke the Jinja template engine to render the template along with the dynamic logic in the template.

## Jinja Template Engine
Part of the benefits of using Jinja is being able to create dynamic pages with special code blocks.<br>

`{{ ... }}` can be used to render values that where passed to the `render_template()` function.<br>

The block `{% ... %}` can be used for conditional and loop statements. The functionality is also extended to defining blocks within the templates, so that you can inject code from one template to another. For example:<br>
*base.html*
```
<body>
    <div>Blog: <a href="/index">Home</a></div>
    <hr>
    {% block content %}{% endblock %}
</body>
```
*index.html*
```
{% block content %}
    <h1>Hello, {{ user.username }}!</h1>
    {% for post in posts %}
    <div><p>{{ post.author.username }} says: <b>{{ post.body }}</b></p></div>
    {% endfor %}
{% endblock %}
```
The block's names must be unique as it is how the engine identifies how to merge the templates together.
