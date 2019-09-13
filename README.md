<div align="center">
    <h1>Digital Aristotle</h1>
</div>

![Generic badge](https://travis-ci.com/Gabighz/Digital-Aristotle.svg?branch=master)
[![Codacy Badge](https://api.codacy.com/project/badge/Grade/a7600e611e6a4044a3b89c6b80c56cea)](https://www.codacy.com/app/Gabighz/Digital-Aristotle?utm_source=github.com&amp;utm_medium=referral&amp;utm_content=Gabighz/Digital-Aristotle&amp;utm_campaign=Badge_Grade)

The purpose of this project is to create a chatbot that will augment studying for Computer Science students.

## Development Setup
Assuming a completely clean/fresh installation or lack of development tools, run the following commands
from a directory above your clone of this repository:

```
sudo apt install python3 python3-pip libpq-dev python3-dev -y
sudo apt install postgresql
sudo service postgresql start
pip3 install virtualenv
virtualenv Digital-Aristotle
cd Digital-Aristotle
source bin/activate
pip install psycopg2
pip install psycopg2-binary
pip install -r requirements.txt
python download_nltk_data.py
```

To start the Django server for the first time (which uses PostgreSQL):

```
sudo -u postgres psql
postgres=# CREATE DATABASE chatbot;
postgres=# CREATE USER admin WITH PASSWORD 'password';
postgres=# ALTER USER admin CREATEDB;
postgres=# \q
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
```

If you choose to install new packages via `pip install` and generate a new requirements file, you can avoid issues with Python2 packages
in the <i>lib</i> directory of your virtual environment with:

```
pipreqs . --force --ignore lib
```

<h3> Troubleshooting </h3>

If you have issues cloning the repository such as ``RPC failed`` or ``Early EOF``:

```
git clone <Repository URL> --depth 1
cd <repo>
git fetch --unshallow
```
If this does not solve the issue, follow github's steps to form a ssh key and clone the repository via the URI:
https://help.github.com/en/articles/generating-a-new-ssh-key-and-adding-it-to-the-ssh-agent

## Information Retrieval System

Contains a keyword extractor, a keyphrase extractor, and an AIML generator. 

This system is used to create AIML files from lecture notes, such as PDF and PPTX files. Firstly, the lecture notes
are converted to XML files. This happens automatically when the website's administrator uploads a PDF or PPTX file. 

The <b>keyword extractor</b>:
    <ul>
        <li> Reads all the data in the XML files, identifying all words and their XML features. </li>
        <li> Using a custom-made feature selection module, classification features are attached to each word. </li>
        <li> The classification features as summed up to represent data points. </li>
        <li> These data points are fed to a K-means classification system, with a parameter specifying a maximum of two clusters (keywords and non-keywords) </li>
        <li> Every keyword is stored in a list for further use in the keyphrase extractor. </li>
    </ul>
    
The <b>keyphrase extractor</b>:
    <ul>
        <li> Reads all the keywords from the array produced by the keyword extractor. </li>
        <li> Extracts all sentences which contain keywords from the XML files. </li>
        <li> For each keyword, every phrase that contains it is ranked. The highest-ranking phrase is then considered a
         keyphrase. </li>
        <li> Every keyword-keyphrase pair is stored in a list for further use in the AIML generator. </li>
    </ul>

The <b> AIML generator</b>:
    <ul>
        <li> Reads the output of the Keyword Extractor to generate AIML patterns (questions). </li>
        <li> Reads the output of the Keyphrase Extractor to generate AIML templates (answers). </li>
        <li> AIML categories (pairs of patterns and templates) are stored for use on the website. </li>
    </ul>

## Contributing

1. Fork it
2. Create your feature branch: `git checkout -b my-new-feature`
3. Commit your changes: `git commit -m 'Add some feature'`
4. Push to the branch: `git push origin my-new-feature`
5. Submit a pull request

## Support

Please [open an issue](https://github.com/Gabighz/Digital-Aristotle/issues/new/) for support.

## License

[General Public License, Version 3](https://www.gnu.org/licenses/gpl-3.0.en.html)