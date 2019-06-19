<div align="center">
    <h1>Digital Aristotle</h1>
</div>

![Generic badge](https://travis-ci.com/Gabighz/Digital-Aristotle.svg?branch=master)
[![Codacy Badge](https://api.codacy.com/project/badge/Grade/a7600e611e6a4044a3b89c6b80c56cea)](https://www.codacy.com/app/Gabighz/Digital-Aristotle?utm_source=github.com&amp;utm_medium=referral&amp;utm_content=Gabighz/Digital-Aristotle&amp;utm_campaign=Badge_Grade)

The purpose of this project is to create a chatbot that will augment studying for Computer Science students.

## Development Setup
Make sure you have ``python3`` and ``python3-pip`` installed. Then run the following commands
from a directory above this repository's clone:

```
pip3 install virtualenv
virtualenv Digital-Aristotle
cd Digital-Aristotle
source bin/activate
pip install -r requirements.txt
```

To start the Django server:

```
python manage.py migrate
python manage.py runserver
```

If you have issues such as ``database "chatbot" does not exist``:

```
sudo -u postgres psql
postgres=# CREATE DATABASE chatbot;
postgres=# \q
python manage.py createsuperuser
```

## Information Retrieval System

Contains a keyword extractor, a keyphrase extractor, and an AIML generator. 

This system is used to create AIML files from lecture notes, such as PDF and PPTX files. Firstly, the lecture notes
are converted to XML files. 

The <b>keyword extractor</b>:
    <ul>
        <li> Reads all the data in the XML files, identifying all words and their XML features. </li>
        <li> Using a custom-made feature selection module, classification features are attached to each word. </li>
        <li> The classification features as summed up to represent data points. </li>
        <li> These data points are fed to a K-means classification system, with a parameter specifying a maximum of two clusters (keywords and non-keywords) </li>
        <li> Finally, each word and its label are stored. </li>
    </ul>
    
The <b>keyphrase extractor</b>:
    <ul>
        <li> Reads all the keywords from the array produced by the keyword extractor. </li>
        <li> Extracts all sentences which contain keywords from the XML files. </li>
    </ul>

The <b> AIML generator</b>:
    <ul>
        <li> Reads the output of the Keyword Extractor to generate AIML patterns (questions). </li>
        <li> Reads the output of the Keyphrase Extractor to generate AIML templates (answers). </li>
        <li> AIML categories (pairs of patterns and templates) are stored for use on the website. </li>
    </ul>