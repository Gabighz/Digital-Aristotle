<?php

/***************************************
 * http://www.program-o.com
 * PROGRAM O
 * Version: 2.6.8
 * FILE: gui/plain/index.php
 * AUTHOR: Elizabeth Perreau and Dave Morton
 * DATE: MAY 17TH 2014
 * DETAILS: simple example gui
 * Modified by: Gabriel Ghiuzan (gghiuzan1@sheffield.ac.uk)
 ***************************************/
$display = "";
$thisFile = __FILE__;

if (!file_exists('../../config/global_config.php'))
{
    header('Location: ../../install/install_programo.php');
}

/** @noinspection PhpIncludeInspection */
require_once('../../config/global_config.php');
/** @noinspection PhpIncludeInspection */
require_once('../../chatbot/conversation_start.php');
$debug_div = '';
$hideSP = '';
$get_vars = (!empty($_GET)) ? filter_input_array(INPUT_GET) : array();
$post_vars = (!empty($_POST)) ? filter_input_array(INPUT_POST) : array();
$form_vars = array_merge($post_vars, $get_vars); // POST overrides and overwrites GET
$bot_id = (!empty($form_vars['bot_id'])) ? $form_vars['bot_id'] : 1;
$say = (!empty($form_vars['say'])) ? $form_vars['say'] : '';
$convo_id = session_id();
$format = (!empty($form_vars['format'])) ? _strtolower($form_vars['format']) : 'html';

if (ERROR_DEBUGGING)
{
    $convo_id = 'DEBUG';
    $debug_content = (!empty($form_vars)) ? file_get_contents(_DEBUG_PATH_ . "{$convo_id}.txt") : '';
    $debug_div = <<<endDebugDiv

<div id="debugDiv" placeholder="debug content">Current Debug File:\n\n$debug_content</div>
endDebugDiv;
    $hideSP = 'display: none;';
}
?>

<!DOCTYPE html>

<html>

    <!-- Head section -->
	<head>

		<link href="/css/bootstrap.min.css" rel="stylesheet"/>
		<link href="/css/bootstrap-theme.min.css" rel="stylesheet"/>
		<link href="/css/styles.css" rel="stylesheet"/> <!-- Main CSS file -->
        <link rel="icon" href="/img/favicon.ico?" type="image/x-icon">

        <meta charset="UTF-8">
        <title>Swansea University Chatbot</title>

        <!-- After the page is refreshed or a message is sent, focus will remain on the input box -->
        <script>
            document.getElementById(window.name==='reload'?'reload':'say').focus();
            window.name='reload';
        </script>

	</head>

    <!-- Body section-->
    <body onload="document.getElementById('say').focus()">

        <!-- Container which displays the conversation history -->
        <div id="responses">
            <?php echo $display . '<div id="end">&nbsp;</div>' . PHP_EOL ?>
        </div>
        <?php echo $debug_div ?>

        <!-- Input box. The user can send information to the chatbot from here -->
        <form name="chatform" method="post" action="index.php#end"
            onsubmit="if(document.getElementById('say').value == '') return false;">

            <!-- Sends the user message, the conversation ID and the bot's ID to the SQL database -->
            <div id="input">
                <label for="say">Say:</label>
                <input type="text" name="say" id="say" size="70"/>
                <input type="submit" name="submit" id="btn_say" value="say"/>
                <input type="hidden" name="convo_id" id="convo_id" value="<?php echo $convo_id; ?>"/>
                <input type="hidden" name="bot_id" id="bot_id" value="<?php echo $bot_id; ?>"/>
                <input type="hidden" name="format" id="format" value="<?php echo $format; ?>"/>
            </div>

        </form>

        <!--
        The user can use this to refresh the page and, thus, clear the display of the conversation history.
        There is one issue with this feature: a new conversation ID and log will be created by refreshing the page.
        -->
        <div id="clearhistory">
            <a href="index.php"> Clear conversation history </a>
        </div>

    <!-- Copyright notice -->
    <div id="bottom">
	    Copyright &#169; 2018 Ghiuzan Gabriel<br>All rights reserved.
    </div>


</body>
</html>
