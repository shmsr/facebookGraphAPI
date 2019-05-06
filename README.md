# Facebook-Graph-API

#### About the project
This app leverages from the Facebook's powerful Graph API. Although, with many such restrictions, the app can interact with a facebook app to harvest posts and even post new one.

### Aim of the project
1) Login inside app through Facebook Authentication
2) Store user related data inside a SQL database such as: ID, Access Token, etc.
3) Fetches posts from a manually given access token (long term) of a page and stores them in the database.
4) Post new posts on the facebook page (App Review updated to use this functioanlity, then Graph API will allow it to work)
5) Stores credentials in the current session

### Live running of app's snapshots are included
-   Inside the photos/ folder
-   Named properly
-   [Note] I'm also including a must_read.txt, please read it.

#### Technologies used
-   Flask
-   Python
-   Flask-SQLAlchemy (ORM)
-   SQLite Database (SQL based)
-   Facebook API, Graph API
-   Facebook-SDK for Python (3rd Party)
-   ngrok

### Running the app locally

Before you run it: (Given that, Facebook's Graph API is very complex to use in compare to Twitter's, etc.)
-   You need proper tokens and proper permission to run this app which is needed to be set on Facebook
-   Proper knowledge of access tokens
-   Ready to use example officially given by are available for Javascript, JAVA, etc. but not for Python
-   Used facebook-sdk
-   Generate Page Token @ interval of 2 hours as it expires after every 2 hours. If you don't change the token in config.py it won't run. I have created a longer lasting access token to fetch posts from a page, so it's manually added
-   To automically pick access token for page, code is added but commented as: fbpages = graph.request('me/accounts')
-   I also have hidden out the token, keys with xxxxxxx on Github for security reasons. Please replace it before use, and to run it you can also contact me for tokens and keys, used.
-   Posting is not allowed currently but I've implemented it already. If you use it you will get Graph API error which will work if Facbook accepts the App Review.
-   To be successfully reviewed, you need "terms and conditions", "privacy policy" docs ready specific to your app.
-   So, I have generated privacy policy document but couldn't make the terms and conditons. Hence, app review is awaited.
-   Also, it won't work locally. And facebook enforces to use HTTPS, otherwise it gives error.
-   To address that, ngrok is used to get HTTPS linking to the local deployment @ 127.0.0.1:8000
-   Inside the Facebook app: Due to "Enforce HTTPS" and "Use Strict Mode for Redirect URIs" being set to permanantly true, one can't change it. So, https protocol and Valid OAuth Redirect URIs needed to be provided 


----------

1.  Clone the repo
2.  Go to root directory of the repo cloned
3.  Setup a virtual environment by executing the command venv:

```
python3 -m venv /path/to/new/virtual/environment 
Example: python3 -m venv env
```

4.  Once a virtual environment has been created, it can be “activated” using a script in the virtual environment’s binary directory. The invocation of the script is platform-specific:

| Platform | Shell | Command to activate virtual environment |
|------- | ------- | ----------------------------- |
| POSIX | bash/zsh | `$ source /bin/activate` |
| POSIX |fish | `$ . /bin/activate.fish` |
| POSIX |csh/tcsh | `$ source /bin/activate.csh` |
| Windows |cmd.exe | `C:> \Scripts\activate.bat` |
| Windows | Powershell | `PS C:> \Scripts\Activate.ps1` |

In my case,  **Platform: Ubuntu (POSIX Compliant)**  and  **Shell: zsh**  So,

```
source env/bin/activate
```

5.  Install all the packages from requirements.txt

```
pip install -r requirements.txt
```

6.  Open cofig.py and add they keys and tokens

7.  If you're running locally, you can't connect to Facebook's API. Hence, I used ngrok. Benefit of ngrok is that it gives a short time live domain linking to your local server, and also provides HTTPS link which is required by Facebook's API

```
ngrok http **port**
```

8.  The HTTPS link we get from ngrok linking to **localhost**  :  **port**, we have to add that to Facebook's App on "App Domain List" and in "Valid OAuth Redirect URIs"

9.  Run run.py

```
python run.py
```

10.  Application will start on  **localhost**  :  **port**

Congratulations, you have successfully fired the application up.
