<div align="center">
    <h1>Digital Aristotle</h1>
</div>


&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
[![Version](https://img.shields.io/github/release/Gabighz/Digital-Aristotle/all.svg?label=version)](https://github.com/Gabighz/Digital-Aristotle/releases)


The purpose of this project is to create a chatbot that will augment studying for Computer Science students.

## AIML

Contains AIML files which will be uploaded to the chatbot's brain. This will be done via Program-O's admin area.

## Information Retrieval System

Contains a keyword extractor, a keyphrase extractor, and an AIML generator. 

The AIML generator is used to create AIML files from lecture notes, such as PDF and PPTX files. 

The lecture notes are first converted to XML files for easier extraction of data. At the moment, this is done by manually using any available website which deals with such conversions.

The <b>keyword extractor</b>:
    <ul>
        <li> Reads all the data in the XML files, identifying all words and their XML features. </li>
        <li> Using a custom-made feature selection module, classification features are attached to each word. </li>
        <li> The classification features as summed up to represent data points. </li>
        <li> These data points are fed to a K-means classification system, with a parameter specifying a maximum of two clusters (keywords and non-keywords) </li>
        <li> Finally, each word and its label are written to a text file. </li>
    </ul>
    
The <b>keyphrase extractor</b>:
    <ul>
        <li> Reads all the keywords from the text file produced by the keyword extractor. </li>
        <li> Extracts all sentences which contain keywords from the XML files. </li>
    </ul>

The <b> AIML generator</b>:
    <ul>
        <li> Reads the output of the Keyword Extractor to generate AIML patterns (questions). </li>
        <li> Reads the output of the Keyphrase Extractor to generate AIML templates (answers). </li>
        <li> Writes AIML categories (pairs of patterns and templates) to a text file. </li>
    </ul>

## www

Contains the files necessary for running the chatbot on a website. We integrated Program O as our AIML interpreter and
customised the Graphical User Interface to our needs.

Source of Program-O: https://github.com/Program-O/Program-O
