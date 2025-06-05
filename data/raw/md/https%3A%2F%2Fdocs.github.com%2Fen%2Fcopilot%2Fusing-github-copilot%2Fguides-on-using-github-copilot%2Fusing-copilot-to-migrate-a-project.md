  * [GitHub Copilot](https://docs.github.com/en/copilot "GitHub Copilot")/
  * [Use GitHub Copilot](https://docs.github.com/en/copilot/using-github-copilot "Use GitHub Copilot")/
  * [Guides](https://docs.github.com/en/copilot/using-github-copilot/guides-on-using-github-copilot "Guides")/
  * [Migrate a project](https://docs.github.com/en/copilot/using-github-copilot/guides-on-using-github-copilot/using-copilot-to-migrate-a-project "Migrate a project")


# Using Copilot to migrate a project to another programming language
GitHub Copilot Chat can help you move a project to a different language. This guide describes what's involved in a migration process and gives an example of a PHP to Python migration.
## In this article
  * [Introduction](https://docs.github.com/en/copilot/using-github-copilot/guides-on-using-github-copilot/using-copilot-to-migrate-a-project#introduction)
  * [Principles of migrating a project to a new language](https://docs.github.com/en/copilot/using-github-copilot/guides-on-using-github-copilot/using-copilot-to-migrate-a-project#principles-of-migrating-a-project-to-a-new-language)
  * [Using Copilot to help you migrate a project to a new language](https://docs.github.com/en/copilot/using-github-copilot/guides-on-using-github-copilot/using-copilot-to-migrate-a-project#using-copilot-to-help-you-migrate-a-project-to-a-new-language)
  * [Example: migrating a PHP project to Python](https://docs.github.com/en/copilot/using-github-copilot/guides-on-using-github-copilot/using-copilot-to-migrate-a-project#example-migrating-a-php-project-to-python)


## [Introduction](https://docs.github.com/en/copilot/using-github-copilot/guides-on-using-github-copilot/using-copilot-to-migrate-a-project#introduction)
Migrating a project to a new programming language can be a difficult and time-consuming task. GitHub Copilot can help you with this process by explaining the changes you need to make and suggesting replacement code in the new language.
## [Principles of migrating a project to a new language](https://docs.github.com/en/copilot/using-github-copilot/guides-on-using-github-copilot/using-copilot-to-migrate-a-project#principles-of-migrating-a-project-to-a-new-language)
Consider the points before you start a migration process:
  * **Coding knowledge**
Make sure you have a good understanding of both programming languages. Although Copilot can translate code for you, you need to understand the choices it proposes and decide whether you want to use its suggestions or ask for an alternative suggestion.
  * **Knowledge of the system you are migrating**
Make sure you understand the architecture and logic of the current system, in addition to the functionality and features it provides to users. You must be able to check that the translated code performs all of the same operations as the original code and produces the same results.
  * **Use AI to help you**
If you don't understand a particular part of the code you are about to translate, use Copilot's "explain" feature, either on the whole file, or a selected portion of the code within a file. See [Asking GitHub Copilot questions in your IDE](https://docs.github.com/en/copilot/using-github-copilot/asking-github-copilot-questions-in-your-ide).
  * **Schedule time to complete the migration**
Conversion is a multi-stage process. The larger the project you are converting the greater the number of steps you will need to take. Make sure you allow plenty of time to complete the entire process.
  * **Work iteratively**
Aim to convert discreet parts of your project separately. Make sure you have verified all of the changes you've made before moving on to another part of the project. Write tests for the individual parts of the project as you proceed so that you can confirm that each of the new components works as expected.
  * **Avoid introducing complexity to the process**
Initially you should aim to do a like-for-like conversion. This won't be possible for all of the code in your project. However, to avoid adding complexity to the migration task, you should try to limit the number of new changes you introduce, other than translating the code and using a new framework and the appropriate dependencies.
  * **Benchmark and refactor the translated code**
After you've completed the initial conversion, and you have a working system, you can perform benchmarking to compare the old and new systems. You can now refactor the code in the new language. This is an opportunity to optimize the code and reduce technical debt.


## [Using Copilot to help you migrate a project to a new language](https://docs.github.com/en/copilot/using-github-copilot/guides-on-using-github-copilot/using-copilot-to-migrate-a-project#using-copilot-to-help-you-migrate-a-project-to-a-new-language)
Assuming you've already familiarized yourself with the existing project, a good way to start a migration is to open a branch of the repository in your editor and ask Copilot for help.
  1. In your editor, open the Copilot Chat panel. See [Asking GitHub Copilot questions in your IDE](https://docs.github.com/en/copilot/using-github-copilot/asking-github-copilot-questions-in-your-ide).
  2. Ask Copilot to outline the steps you need to take to migrate the project to the new language.
For example, for a migration from PHP to Python, you could ask:
`@workspace I want to migrate this project from PHP to Python. Give me a high level overview of the steps I need to take. Don't go into detail at this stage.`
The `@workspace` chat participant sets the files in the current workspace as the context for the question you ask.
Copilot will typically come back with a list of steps that you need to take to migrate the project.
  3. Copy Copilot's response and save this somewhere to refer to throughout the process.
  4. Work through each step of the process, asking for detailed help from Copilot as you need it.
Consider each suggestion from Copilot carefully. Make sure you understand the code that it is suggesting and assess whether it's appropriate for your project. If you are not sure, ask Copilot to explain the code to you.
If you think a change suggested by Copilot is not right in some way, ask for an alternative suggestion.
  5. As soon as you've migrated a component to a state that you can run, check that it works as expected. If it generates an error, copy the error into the Copilot Chat view, and ask Copilot to help you fix it.
  6. After you've completed the initial conversion, use Copilot to help you refactor the code in the new language. For more information, see [Refactoring code with GitHub Copilot](https://docs.github.com/en/copilot/using-github-copilot/guides-on-using-github-copilot/refactoring-code-with-github-copilot).


## [Example: migrating a PHP project to Python](https://docs.github.com/en/copilot/using-github-copilot/guides-on-using-github-copilot/using-copilot-to-migrate-a-project#example-migrating-a-php-project-to-python)
The following example describes the migration of a simple web application from PHP to Python. Even if these are not the programming languages you are using for your migration, you may find it helpful to follow along with the steps described here to familiarize yourself with a project migration. The steps will be similar for migrating other small projects from one language to another.
![Screenshot of the 'Simple PHP Website' prior to migration from PHP to Python.](https://docs.github.com/assets/cb-257834/images/help/copilot/migration-original-website.png)
This example assumes:
  * You are working in Visual Studio Code.
  * You have both languages installed: PHP and Python version 3.12 or later.


### [Migrating a simple website project](https://docs.github.com/en/copilot/using-github-copilot/guides-on-using-github-copilot/using-copilot-to-migrate-a-project#migrating-a-simple-website-project)
We are going to migrate the code in this public repository on GitHub: [docs/simple-php-website](https://github.com/docs/simple-php-website).
The repository consists of the following files.
```
.gitignore
.htaccess
LICENSE
content
├── 404.phtml
├── about-us.phtml
├── contact.phtml
├── home.phtml
└── products.phtml
includes
├── config.php
└── functions.php
index.php
readme.md
template
├── style.css
└── template.php

```

This example gives the prompts you can enter into Copilot Chat to complete the migration, and the responses Copilot returned for one instance of this migration. The GPT-4o model was used to generate these responses. Copilot Chat responses are non-deterministic, so you will probably get slightly different responses to the ones shown here.
During a migration process you are likely to get errors that you need to fix before moving ahead. Copilot can help you with this. The example includes some errors and shows how you can get Copilot to help you fix them.
Because the responses you'll get from Copilot Chat are likely to be different to those shown here, you may encounter different errors. You may, therefore, find it easier to step through this example migration using the responses shown here, rather than those you get from Copilot yourself.
After completing this example migration you can then use the same methodology on your own project.
  1. Start by cloning a copy of the repository to your local machine.
  2. Run the application to check it works.
To do this, in a terminal, navigate to the root of the cloned repository and run the following command:
Shell```
 php -S localhost:8000

```
```
 php -S localhost:8000

```

Then in a browser, go to: <http://localhost:8000>.
  3. Click around the website, to get to know it, so that you'll be able to verify that the migration has been successful.
  4. Create a working branch in your repository and open it as a new workspace in Visual Studio Code.
  5. Familiarize yourself with the contents and architecture of the existing project. Copilot can help you with this:
    1. Open the Copilot Chat view.
    2. Enter a prompt such as:
`@workspace Describe this project in detail, explaining what the various components do and how they interact.`
  6. Ask Copilot for a high-level overview of the migration process:
`@workspace I want to migrate this project from PHP to Python. Give me a high level overview of the steps I need to take. Don't go into detail at this stage.`
Copilot will reply with instructions such as:
```
To migrate this project from PHP to Python, follow these high-level steps:

1. Set Up Python Environment:
   - Install Python and set up a virtual environment.
   - Install necessary packages (e.g., Flask for web framework).

2. Convert Configuration:
   - Translate the configuration settings from config.php to a Python configuration file.

3. Rewrite Functions:
   - Convert PHP functions in functions.php to Python functions.

4. Create Flask Application:
   - Set up a Flask application to handle routing and views.
   - Map the routes to corresponding views.

5. Convert Templates:
   - Translate template.php to a Jinja2 template.
   - Update the CSS file path in the template.

6. Convert Content Pages:
   - Convert .phtml content files to HTML or Jinja2 templates.

7. Update .htaccess Rules:
   - Translate .htaccess rewrite rules to Flask route handling.

8. Run and Test:
   - Run the Flask application and test all routes and functionalities.
   - Ensure the site works as expected and fix any issues.

9. Documentation:
   - Update the readme.md with new instructions for running the Python project.

```

  7. Copy Copilot's response and save this somewhere to refer to throughout the remainder of this process. You'll work through each of these steps, asking Copilot for help as you proceed.
  8. If you haven't already decided which Python framework you want to use, you can ask Copilot for advice:
`@workspace What Python frameworks can I use for this project once it is migrated to Python? Give me a selection of options, with a brief summary of the pros and cons of each in relation to this website project. Which framework would you recommend?`
Copilot replies with information about various frameworks, and concludes:
```
For a project like yours - which is a simple, content-driven website - Flask is highly recommended. Its simplicity, flexibility, and ease of use (especially with its templating system that can easily replace your current PHP template structure) make it a great fit.

```

We'll take Copilot's advice and use Flask.
  9. Returning to Copilot's high-level overview, the first step is to set up a Python environment and install the necessary packages. To find out how to do this, in Copilot Chat, enter:
`@workspace I want to use Flask. Tell me how to set up a virtual environment and install the necessary packages.`
Copilot will reply with instructions such as:
```
1. Create a virtual environment:
   - Open a terminal and navigate to your project directory.
   - Run the following command to create a virtual environment:
     python3 -m venv venv

2. Activate the virtual environment:
   - On macOS and Linux:
     source venv/bin/activate

   - On Windows:
     venv\Scripts\activate

3. Install Flask and necessary packages:
   - With the virtual environment activated, run the following command
     to install Flask and other necessary packages:
     pip install Flask

4. Verify the installation:
   - You can verify that Flask is installed by running:
     pip list

```

  10. Follow Copilot's instructions and use `pip list` to verify that Flask is installed.
  11. Returning to Copilot's overview for the migration process, the next step is to convert the configuration. Ask Copilot for help with this. For example:
`@workspace As the first step in migrating this project from PHP to Python, create a Python configuration file by converting the functions in functions.php to Python functions. Tell me where to locate the Python config file in the project.`
Copilot suggests that you create a file called `config.py` in the `includes` directory, containing the following code.
Python```
config = {
   'name': 'Simple Python Website',
   'site_url': '',
   'pretty_uri': False,
   'nav_menu': {
      '': 'Home',
      'about-us': 'About Us',
      'products': 'Products',
      'contact': 'Contact',
   },
  'template_path': 'template',
  'content_path': 'content',
  'version': 'v3.1',
}

def get_config(key=''):
   return config.get(key, None)

def site_name():
   return get_config('name')

def site_url():
   return get_config('site_url')

def site_version():
   return get_config('version')

def nav_menu(sep=' | '):
   nav_menu = ''
   nav_items = get_config('nav_menu')

   for uri, name in nav_items.items():
      query_string = request.args.get('page', '')
      class_active = ' active' if query_string == uri else ''
      url = f"{get_config('site_url')}/{'' if get_config('pretty_uri') or uri == '' else '?page='}{uri}"

      nav_menu += f'<a href="{url}" title="{name}" class="item{class_active}">{name}</a>{sep}'

   return nav_menu.strip(sep)

def page_title():
   page = request.args.get('page', 'Home')
   return ' '.join(word.capitalize() for word in page.split('-'))

def page_content():
   page = request.args.get('page', 'home')
   path = os.path.join(os.getcwd(), get_config('content_path'), f'{page}.phtml')

   if not os.path.exists(path):
      path = os.path.join(os.getcwd(), get_config('content_path'), '404.phtml')

   with open(path, 'r') as file:
      return file.read()

def init():
   template_path = os.path.join(get_config('template_path'), 'template.html')
   with open(template_path, 'r') as file:
      return file.read()

```
```
config = {
   'name': 'Simple Python Website',
   'site_url': '',
   'pretty_uri': False,
   'nav_menu': {
      '': 'Home',
      'about-us': 'About Us',
      'products': 'Products',
      'contact': 'Contact',
   },
  'template_path': 'template',
  'content_path': 'content',
  'version': 'v3.1',
}

def get_config(key=''):
   return config.get(key, None)

def site_name():
   return get_config('name')

def site_url():
   return get_config('site_url')

def site_version():
   return get_config('version')

def nav_menu(sep=' | '):
   nav_menu = ''
   nav_items = get_config('nav_menu')

   for uri, name in nav_items.items():
      query_string = request.args.get('page', '')
      class_active = ' active' if query_string == uri else ''
      url = f"{get_config('site_url')}/{'' if get_config('pretty_uri') or uri == '' else '?page='}{uri}"

      nav_menu += f'<a href="{url}" title="{name}" class="item{class_active}">{name}</a>{sep}'

   return nav_menu.strip(sep)

def page_title():
   page = request.args.get('page', 'Home')
   return ' '.join(word.capitalize() for word in page.split('-'))

def page_content():
   page = request.args.get('page', 'home')
   path = os.path.join(os.getcwd(), get_config('content_path'), f'{page}.phtml')

   if not os.path.exists(path):
      path = os.path.join(os.getcwd(), get_config('content_path'), '404.phtml')

   with open(path, 'r') as file:
      return file.read()

def init():
   template_path = os.path.join(get_config('template_path'), 'template.html')
   with open(template_path, 'r') as file:
      return file.read()

```

  12. Create the `includes/config.py` file and delete the existing `includes/config.php` file.
  13. Returning to the overview again, ask Copilot to help you rewrite the PHP functions.
`@workspace Continuing the migration of this project from PHP to Python, create Python functions to replace the existing PHP functions. Tell me where to locate the Python functions in the project.`
Copilot suggests you create a file called `functions.py` in the `includes` directory, containing the following code.
Python```
import os
from flask import request
from .config import get_config

def site_name():
   return get_config('name')

def site_url():
   return get_config('site_url')

def site_version():
   return get_config('version')

def nav_menu(sep=' | '):
   nav_menu = ''
   nav_items = get_config('nav_menu')

   for uri, name in nav_items.items():
      query_string = request.args.get('page', '')
      class_active = ' active' if query_string == uri else ''
      url = f"{get_config('site_url')}/{'' if get_config('pretty_uri') or uri == '' else '?page='}{uri}"

      nav_menu += f'<a href="{url}" title="{name}" class="item{class_active}">{name}</a>{sep}'

   return nav_menu.strip(sep)

def page_title():
   page = request.args.get('page', 'Home')
   return ' '.join(word.capitalize() for word in page.split('-'))

def page_content():
   page = request.args.get('page', 'home')
   path = os.path.join(os.getcwd(), get_config('content_path'), f'{page}.phtml')

   if not os.path.exists(path):
      path = os.path.join(os.getcwd(), get_config('content_path'), '404.phtml')

   with open(path, 'r') as file:
      return file.read()

def init():
   template_path = os.path.join(get_config('template_path'), 'template.html')
   with open(template_path, 'r') as file:
      return file.read()

```
```
import os
from flask import request
from .config import get_config

def site_name():
   return get_config('name')

def site_url():
   return get_config('site_url')

def site_version():
   return get_config('version')

def nav_menu(sep=' | '):
   nav_menu = ''
   nav_items = get_config('nav_menu')

   for uri, name in nav_items.items():
      query_string = request.args.get('page', '')
      class_active = ' active' if query_string == uri else ''
      url = f"{get_config('site_url')}/{'' if get_config('pretty_uri') or uri == '' else '?page='}{uri}"

      nav_menu += f'<a href="{url}" title="{name}" class="item{class_active}">{name}</a>{sep}'

   return nav_menu.strip(sep)

def page_title():
   page = request.args.get('page', 'Home')
   return ' '.join(word.capitalize() for word in page.split('-'))

def page_content():
   page = request.args.get('page', 'home')
   path = os.path.join(os.getcwd(), get_config('content_path'), f'{page}.phtml')

   if not os.path.exists(path):
      path = os.path.join(os.getcwd(), get_config('content_path'), '404.phtml')

   with open(path, 'r') as file:
      return file.read()

def init():
   template_path = os.path.join(get_config('template_path'), 'template.html')
   with open(template_path, 'r') as file:
      return file.read()

```

  14. Create the `includes/functions.py` file and delete the existing `includes/functions.php` file.
  15. Continuing with the overview, the next step is to create a Flask application. Ask Copilot to help you with this:
`@workspace Set up a Flask application to handle routing and views, and map the routes to corresponding views. Tell me the location of any files that need to be created or changed.`
Copilot suggests you create a file called `app.py` in the root of the project, containing the following code.
Python```
from flask import Flask, render_template, request
import os

app = Flask(__name__)

config = {
   'name': 'Simple Python Website',
   'site_url': '',
   'pretty_uri': False,
   'nav_menu': {
      '': 'Home',
      'about-us': 'About Us',
      'products': 'Products',
      'contact': 'Contact',
   },
   'template_path': 'template',
   'content_path': 'content',
   'version': 'v3.1',
}

def get_config(key=''):
   return config.get(key, None)

@app.route('/')
@app.route('/<page>')
def index(page='home'):
   page_content = get_page_content(page)
   page_title = get_page_title(page)
   nav_menu = get_nav_menu()
   return render_template('template.html', page_title=page_title, page_content=page_content, nav_menu=nav_menu)

def get_page_title(page):
   return ' '.join(word.capitalize() for word in page.split('-'))

def get_page_content(page):
   path = os.path.join(os.getcwd(), get_config('content_path'), f'{page}.phtml')
   if not os.path.exists(path):
      path = os.path.join(os.getcwd(), get_config('content_path'), '404.phtml')
   with open(path, 'r') as file:
      return file.read()

def get_nav_menu(sep=' | '):
   nav_menu = ''
   nav_items = get_config('nav_menu')
   for uri, name in nav_items.items():
      query_string = request.args.get('page', '')
      class_active = ' active' if query_string == uri else ''
      url = f"{get_config('site_url')}/{'' if get_config('pretty_uri') or uri == '' else '?page='}{uri}"
      nav_menu += f'<a href="{url}" title="{name}" class="item{class_active}">{name}</a>{sep}'
   return nav_menu.strip(sep)

if __name__ == '__main__':
   app.run(debug=True)

```
```
from flask import Flask, render_template, request
import os

app = Flask(__name__)

config = {
   'name': 'Simple Python Website',
   'site_url': '',
   'pretty_uri': False,
   'nav_menu': {
      '': 'Home',
      'about-us': 'About Us',
      'products': 'Products',
      'contact': 'Contact',
   },
   'template_path': 'template',
   'content_path': 'content',
   'version': 'v3.1',
}

def get_config(key=''):
   return config.get(key, None)

@app.route('/')
@app.route('/<page>')
def index(page='home'):
   page_content = get_page_content(page)
   page_title = get_page_title(page)
   nav_menu = get_nav_menu()
   return render_template('template.html', page_title=page_title, page_content=page_content, nav_menu=nav_menu)

def get_page_title(page):
   return ' '.join(word.capitalize() for word in page.split('-'))

def get_page_content(page):
   path = os.path.join(os.getcwd(), get_config('content_path'), f'{page}.phtml')
   if not os.path.exists(path):
      path = os.path.join(os.getcwd(), get_config('content_path'), '404.phtml')
   with open(path, 'r') as file:
      return file.read()

def get_nav_menu(sep=' | '):
   nav_menu = ''
   nav_items = get_config('nav_menu')
   for uri, name in nav_items.items():
      query_string = request.args.get('page', '')
      class_active = ' active' if query_string == uri else ''
      url = f"{get_config('site_url')}/{'' if get_config('pretty_uri') or uri == '' else '?page='}{uri}"
      nav_menu += f'<a href="{url}" title="{name}" class="item{class_active}">{name}</a>{sep}'
   return nav_menu.strip(sep)

if __name__ == '__main__':
   app.run(debug=True)

```

Copilot also suggests renaming `template/template.php` to `template/template.html` and updating the file to use Jinja2 templating syntax:
HTML```
<!DOCTYPE html>
<html>
<head>
   <meta charset="utf-8" />
   <meta http-equiv="x-ua-compatible" content="ie=edge"/>
   <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no"/>
   <title>{{ page_title }} | {{ get_config('name') }}</title>
   <link href="{{ get_config('site_url') }}/template/style.css" rel="stylesheet" type="text/css" />
</head>
<body>
<div class="wrap">

   <header>
      <h1>{{ get_config('name') }}</h1>
      <nav class="menu">
         {{ nav_menu|safe }}
      </nav>
   </header>

   <article>
      <h2>{{ page_title }}</h2>
      {{ page_content|safe }}
   </article>

   <footer>
      <small>&copy;{{ get_config('version') }} {{ get_config('name') }}.<br>{{ get_config('version') }}</small>
   </footer>

</div>
</body>
</html>


```
```

<!DOCTYPE html>
<html>
<head>
   <meta charset="utf-8" />
   <meta http-equiv="x-ua-compatible" content="ie=edge"/>
   <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no"/>
   <title>{{ page_title }} | {{ get_config('name') }}</title>
   <link href="{{ get_config('site_url') }}/template/style.css" rel="stylesheet" type="text/css" />
</head>
<body>
<div class="wrap">

   <header>
      <h1>{{ get_config('name') }}</h1>
      <nav class="menu">
         {{ nav_menu|safe }}
      </nav>
   </header>

   <article>
      <h2>{{ page_title }}</h2>
      {{ page_content|safe }}
   </article>

   <footer>
      <small>&copy;{{ get_config('version') }} {{ get_config('name') }}.<br>{{ get_config('version') }}</small>
   </footer>

</div>
</body>
</html>


```

  16. Create the `app.py` and `template/template.html` files as suggested.
  17. Copilot may also suggest that, having created these files, you now run `python app.py` in the terminal, from the root of the repository, and then browse to <http://127.0.0.1:5000>.
Depending on how Python is installed on your computer, you may need to use the command `python3 app.py` instead of `python app.py` to ensure the correct version of Python is used.
When you do this you will see error messages in the browser.
  18. Copy the initial `TemplateNotFound` error message to the Copilot Chat view and ask how you can fix this. For example:
`@workspace When I run `python3 app.py`, I get the following error in the browser: `jinja2.exceptions.TemplateNotFound: template.html`. How can I fix this?`
Copilot replies that the error indicates that Flask is unable to locate the `template.html` file.
It tells you that, by default, Flask looks for templates in a folder named `templates` in the root directory of your project. However, your `template.html` file is located in the `template` directory. To fix this, you need to specify the correct template folder when creating the Flask app. It advises you to update your `app.py` file, changing the assignment `app = Flask(__name__)` to include the `template_folder` parameter:
Python```
app = Flask(__name__, template_folder='template')

```
```
app = Flask(__name__, template_folder='template')

```

  19. Assuming the Flask development server is still running, if you refresh the browser page at <http://127.0.0.1:5000/>, you will now see a new error relating to the `get_config` function.
Copy this error message to the Copilot Chat view and ask for help.
`@workspace When I run `python3 app.py`, I get the following error in the browser: `jinja2.exceptions.UndefinedError: 'get_config' is undefined.` How can I fix this?`
Copilot replies that the error occurs because `get_config` is not available in the Jinja2 template context. It advises you to add the following code to the `app.py` file, directly before the line `@app.route('/')`:
Python```
app.jinja_env.globals.update(get_config=get_config)

```
```
app.jinja_env.globals.update(get_config=get_config)

```

  20. Refresh your browser and you should now see the website.
![Screenshot of the 'Simple Python Website' without CSS styling.](https://docs.github.com/assets/cb-142784/images/help/copilot/migration-no-css-website.png)
However, none of the CSS styles are being applied. We'll fix this next.
  21. Ask Copilot:
`@workspace The deployed website does not use the CSS styles. How can I fix this?`
Copilot tells you that Flask expects your CSS file to be in a directory called `static`. It suggests moving the existing `style.css` file from the `template` directory into a new `static` directory, and then updating the path to the `style.css` file within the `head` portion of the `template.html` file. Change this to:
HTML```
<link rel="stylesheet" href="{{ url_for('static', filename='style.css') }}">


```
```

<link rel="stylesheet" href="{{ url_for('static', filename='style.css') }}">


```

When you refresh the browser, the website should now render correctly.
To complete the initial migration, continue working through the steps in the high-level overview that Copilot gave you, asking for help as you need it.


### [Completing the migration](https://docs.github.com/en/copilot/using-github-copilot/guides-on-using-github-copilot/using-copilot-to-migrate-a-project#completing-the-migration)
Further work to successfully complete the migration process would involve:
  * **Checking** the initial migration thoroughly.
  * **Bug fixing**. For example, at present in the example described here, the page links only work if you set `pretty_uri` to `True` in the `config` section of the `app.py` file. If you want the option of using query string parameters in the page URLs, or if you want to remove this option from the code, you can ask Copilot to help you do this.
  * **Writing tests** for the migrated project.
  * **Cleaning up** the project by removing any files that are no longer needed.
  * **Refactoring** the code in the new language. The migration process has resulted in a Python project whose architecture is based on that of the original PHP project. Having done the initial migration, you can now refactor the code to make best use of features of the Python language and the Flask framework.
  * **Updating the documentation**. The `readme.md` file is now out of date and needs to be rewritten.


