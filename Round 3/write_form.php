<?php
$file = file_get_contents('andrew_comments.txt', FILE_USE_INCLUDE_PATH);
// echo $file;
$arr = explode("\n", $file);
var_dump($arr[0]);
?>