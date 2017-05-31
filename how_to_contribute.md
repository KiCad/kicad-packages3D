# How to Contribute to KiCad 3d Mode Libraries

1. If you don't have one, create an account on [GitHub](https://github.com/join).

1. Fork this repository under your account. [Read how](https://help.github.com/articles/fork-a-repo/)

1. Clone your newly created fork. [Read how](https://help.github.com/articles/fetching-a-remote/)

1. Create a new branch with a meaningful name
    ```
    git commit -b branch-name
    git push --set-upstream origin branch-name
    ```

1. Add the files you changed.
    * If you did not add new files
        ```
        git add -u
        git commit -m "place your commit message here"
        ```
    * If you added new files to the repository
        ```
        git add directory-name
        ```
        1. Make sure that you only add the 3d model files to the repository.
            * You can use a local .gitignore file to exclude unwanted files.
            * Or add each file separately
            * If you added a file accidentally remove it with
                ```
                git rm --cached
                ```
        1. Check that you added only the correct files before committing
            ```
            git status
            ```
1. Commit your changes to your local repository
    ```
    git commit -m "A meaningful commit message"
    ```
1. Push to your branch:
    ```
    git push
    ```

1. Create a pull request. [Read how](https://help.github.com/articles/about-pull-requests/)

1. Include your references, for example a datasheet, in the comments.

1. Include a screenshot of the 3d model that showcases how your model will look like when used inside KiCad.
    1. Make sure your 3d model files are at the appropriate location for KiCad to find them.
    1. Make a pcb_new file using the footprints for which your models are designed for.
    1. Open the 3d viewer.
    1. Create a screenshot.

1. Wait until a librarian approves your work. Discussion and corrections might be needed.
