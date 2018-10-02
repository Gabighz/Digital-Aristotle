# Digital-Aristotle

The purpose of this project is to create a chatbot that will augment studying for Computer Science students.

## AIML

Contains AIML files which will be uploaded to the chatbot's brain. This will be done via Program-O's admin area.

## Information Retrieval System

Contains a keyword extractor, a keyphrase extractor, and an AIML generator. 

The AIML generator is used to create AIML files from lecture notes, such as PDF and PPTX files.

Within the AIML generator:
<ul>
    <li><b>Keyword extractor:</b> is used to generate AIML questions ("patterns")</li>
    <li><b>Keyphrase extractor:</b> is used to generate corresponding AIML answers ("templates")</li>
</ul>

## www

Contains the files necessary for running the chatbot on a website. We integrated Program O as our AIML interpreter and
customised the Graphical User Interface to our needs.
