# Django Url-Shortener App

## Setting up your Development Environment ##
1. First, fork this repository to your account.

2. Create a virtual environment on your machine. 
    ```
    virtualenv -p python3 your_environment_name
    ```
    We recommend using python3-virtualenv. Any other packages would do fine though.

3. Activate the newly created virtual environment:
    ```
    cd your_environment_name
    source bin/activate
    ```

4. Clone this repository (this would make rebasing easier).
    ```
    git clone https://github.com/modihere/url-shortener.git
    ```
    
5. Install the dependencies for the project.
    ```
    cd url-shortener
    pip3 install -r requirements.txt
    ```

6. Run the following command in the terminal to generate a random key
    ```
    python -c "import string,random;uni=string.ascii_letters+string.digits+'$%&\()*+,-./:;<=>?@[]^_{|}';print(repr(''.join([random.SystemRandom().choice(uni) for i in range(50)])))"
    ```

    Copy the generated random key and assign it to SECRET_KEY variable in shortweb/settings.py.example and save file as settings.py in same directory.

7. Migrate your database.
    ```
    python3 manage.py makemigrations
    python manage.py migrate 
    ``` 

8. Run the live development server on your machine and test it.
    ```
    python3 manage.py runserver
    ```
    
    or 

    ```
    python3 manage.py runserver 8080
    ```
    or

    If you want to change the server’s IP, pass it along with the port. So to listen on all public IPs (useful if you want to show off your work on other computers on your network), use:

    ```
    python manage.py runserver 0.0.0.0:8000
    ```

    Once the server is started, open http://127.0.0.1:8000 or whatever server you are running on in a web browser.
    Everything went well if the webpage loads correctly and you don't see any errors.
    
9. Add a remote to your forked repository. This remote will be needed to push your changes to your repo.
    ```
    git remote add myfork https://github.com/<username>/website.git
    ```
    
10. Find an issue in this repository that you would like to and can fix.
   Start working on an issue. Steps 9 and beyond will guide you in doing this.
   
11. Create a new branch and switch to it. (make sure you are on master before doing this).
    ```
    git branch mybranch
    git checkout mybranch
    ```
    'mybranch' can be replaced by your preferred name for the branch.
    The above to commands are equivalent to the following
    ```
    git checkout -b mybranch
    ```

12. Make your changes and then execute the tests to make sure you didn't break anything.

    ```
    python3 manage.py test
    ```
    Ensure that you follow [PEP8](https://www.python.org/dev/peps/pep-0008/#descriptive-naming-styles) style guide for python code while naming functions or classes.

    Then stage them and commit them.
    Check out Chris Beams's guide to writing good commit messages [here](https://chris.beams.io/posts/git-commit/).

    *A small description of your changes is must in the commit messages.* 

13. After you are done making changes, push the branch to your fork.
    ```
    git push -u myfork mybranch
    ```
    The **-u** option is required only the first time you push the branch.
	**In case you have made multiple commits, you need to squash them into a single commit before pushing.**
    Use
    ```
    git rebase -i HEAD~n
    ```
    `n` is the number of commits to rebase back to.
    You will be given some options such as pick, squash etc. with the commit in front of it, select the commit to squash by adding `squash` or s
    check here for more on [squashing and rebasing](https://www.devroom.io/2011/07/05/git-squash-your-latests-commits-into-one/)

14. Then create a Pull Request from that branch using GitHub.

**What after you have submitted a Pull Request?**

Well, you could wait for it to be reviewed by someone or you could attempt to fix another issue. 

*OR*

You could help us in an even better way! 


### Help us by reviewing others' Pull Requests! ###
If you have the time and the knowledge then you must review others' Pull Requests. This would stop Pull Requests from stacking up and will definitely mean your Pull Request would be reviewed faster.

**Things to keep in mind while reviewing a Pull Request**

If any of the following questions has a **yes** for an answer then the request shall **not** be approved.
* Will the referenced issue **not** be fixed with the Pull Request?
* Are there unnecessary changes?
* Is the commit message **not** good?
* Is a rebase required?
* Is the fix dirty (hacky)?

*Reviewers shall make sure that the reviews are done on a first come first service basis.*
