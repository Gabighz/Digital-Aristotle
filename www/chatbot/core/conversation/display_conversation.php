<?php

/***************************************
 * http://www.program-o.com
 * PROGRAM O
 * Version: 2.6.8
 * FILE: chatbot/core/conversation/display_conversation.php
 * AUTHOR: Elizabeth Perreau and Dave Morton
 * DATE: MAY 17TH 2014
 * DETAILS: this file contains the functions to handle the return of the conversation lines back to the user
 ***************************************/

/**
 * function get_conversation_to_display()
 * This function gets the conversation from the db to display/return to the user
 * @link http://blog.program-o.com/?p=1223
 * @param  array $convoArr - the conversation array
 * @return array $orderedRows - a list of conversation line
 **/
function get_conversation_to_display($convoArr)
{
    global $dbConn, $dbn, $bot_name, $unknown_user;
    $orderedRows = array();

    $user_id = $convoArr['conversation']['user_id'];
    $bot_id = $convoArr['conversation']['bot_id'];
    $user_name = $convoArr['conversation']['user_name'];
    $user_name = (!empty ($user_name)) ? $user_name : $unknown_user;
    $convoArr['conversation']['bot_name'] = $bot_name;

    if (empty ($bot_name))
    {
        /** @noinspection SqlDialectInspection */
        $sql = "SELECT `bot_name` FROM `bots` WHERE `bot_id` = :bot_id limit 1;";
        $params = array(':bot_id' => $convoArr['conversation']['bot_id']);
        $row = db_fetch($sql, $params, __FILE__, __FUNCTION__, __LINE__);
        $bot_name = $row['bot_name'];
    }

    $sql = "SELECT * FROM `$dbn`.`conversation_log` WHERE
        `user_id` = :user_id
        AND `bot_id` = :bot_id
        AND `convo_id` = :convo_id
        ORDER BY id";
    $params = array(
        ':bot_id'   => $convoArr['conversation']['bot_id'],
        ':convo_id' => $convoArr['conversation']['convo_id'],
        ':user_id'  => $convoArr['conversation']['user_id'],
    );

    runDebug(__FILE__, __FUNCTION__, __LINE__, "get_conversation SQL: $sql", 3);
    $debugSQL = db_parseSQL($sql, $params);
    //save_file(_LOG_PATH_ . 'gc2dsql.txt', $debugSQL);

    $result = db_fetchAll($sql, $params, __FILE__, __FUNCTION__, __LINE__);

    if (count($result) > 0)
    {
        foreach ($result as $row)
        {
            $allrows[] = $row;
        }
        $orderedRows = array_reverse($allrows, false);
    }
    else {
        $orderedRows[] = array('id' => NULL, 'input' => "", 'response' => "", 'user_id' => $convoArr['conversation']['user_id'], 'bot_id' => $convoArr['conversation']['bot_id'], 'timestamp' => "");
    }

    runDebug(__FILE__, __FUNCTION__, __LINE__, "Found '" . count($result) . "' lines of conversation", 2);

    return $orderedRows;
}

/**
 * function get_conversation()
 * This function gets the conversation format
 * @link http://blog.program-o.com/?p=1225
 * @param  array $convoArr - the conversation array
 * @return array $convoArr
 **/
function get_conversation($convoArr)
{
    $conversation = get_conversation_to_display($convoArr);
    runDebug(__FILE__, __FUNCTION__, __LINE__, "Processing conversation as " . $convoArr['conversation']['format'], 4);


    $convoArr = get_html($convoArr, $conversation);

    return $convoArr;
}

/**
 * function get_html()
 * This function formats the response as html
 * @link http://blog.program-o.com/?p=1227
 * @param  array $convoArr - the conversation array
 * @param  array $conversation - the conversation lines to format
 * @return array $convoArr
 **/
function get_html($convoArr, $conversation)
{
    if (!is_array($conversation))
    {
        $tmp = $conversation;
        $conversation = array($tmp);
    }
    $show = "";
    $user_name = $convoArr['conversation']['user_name'];
    $bot_name = $convoArr['conversation']['bot_name'];

    foreach ($conversation as $index => $conversation_subarray)
    {
        $show .= "<div class=\"usersay\">$user_name: " . stripslashes($conversation_subarray['input']) . "</div>";
        $show .= "<div class=\"botsay\">$bot_name: " . stripslashes($conversation_subarray['response']) . "</div>";
    }
    $convoArr['send_to_user'] = $show;
    runDebug(__FILE__, __FUNCTION__, __LINE__, "Returning HTML", 4);

    return $convoArr;
}

/**
 * function display_conversation()
 * Displays the output of the conversation if the current format is XML or JSON and updated referenced $display if html
 *
 * @link  http://blog.program-o.com/?p=1233
 * @param (array) $convoArr
 * @return void (void) [return value]
 */
function display_conversation($convoArr)
{
    $display = $convoArr['send_to_user'];

    $display = str_ireplace('<![CDATA[', '', $display);
    $display = str_replace(']]>', '', $display);
}