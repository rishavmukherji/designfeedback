<html>
<!--
<ul>
	<li>Be as specific as possible in your instructions to eliminate ambiguity. For example, when asking workers to extract texts from an image, ask workers to type the texts exactly as shown in the image including capitalization, spaces and punctuations.</li>
	<li>Include an example of a right answer and a wrong answer. Highlight important information where appropriate.</li>
	<li>Clarify what you expect if a HIT is not doable because of missing data or other problems.</li>
</ul>
--!>

<!-- Bootstrap v3.0.3 -->
<link href="https://s3.amazonaws.com/mturk-public/bs30/css/bootstrap.min.css" rel="stylesheet" />
<style type="text/css">.alert{
	font-weight: bold;
	font-size: 16px;
}
.answer{
	margin-left: auto;
	margin-right: 20px;
}

ul {
  overflow: auto;
  list-style-type: none;
}
 
li {
  height: 25px;
  float: left;
  margin-right: 0px;
  padding: 0 20px;
}

h5 {
	font-size: 17px;
}

p {
	font-size: 15;
}
</style>
<section class="container" id="Other" style="margin-bottom:15px; padding: 10px 10px; font-family: Verdana, Geneva, sans-serif; color:#333333; font-size:0.9em;">
<div class="row col-xs-12 col-md-12"><!-- Instructions -->
<div class="panel panel-primary">
<div class="panel-heading"><strong>Instructions</strong></div>

<div class="panel-body">
<p><strong>Before you fill out the survey, please visit the following website : </strong></p>
<a href="$http://www.harvardusindiainitiative.com/" target="_blank">Harvard US-Indian Initiative (www.harvardusindiainitiative.com)</a></div>

<p style="margin-left: 20px;"><strong>And answer the following questions: </strong></p>

<p class="alert">Note that if the majority&nbsp;of your answers to these questions are incorrect, your HIT may not be accepted</p>
Who is the president of the Executive Board?: <input class="answer" id="v1" name="v1" type="text" /><br />
When was the last event organized by this organization?: <input class="answer" id="v2" name="v2" type="text" /><br />
Try and register for the upcoming conference in India. What is the "Form Name" shown when you try to register? (Don't worry, your registrations for the conference won't be accepted): <input class="answer" id="v4" name="v4" type="text" /><br />
<br />
<br />
&nbsp;</div>
<hr/>
<!-- End Instructions -->

<div>
	<p><b>Previous participants have made the following comments about this website. Please tell us whether you think the following comments are helpful for the designer of the website and are good feedback. </b></p>
</div>

<?php
$file = file_get_contents('conference_comments.txt', FILE_USE_INCLUDE_PATH);
// echo $file;
$arr = explode("\n", $file);
// var_dump($arr);
$count = 0;
foreach($arr as $statement) {
	echo("<div><p>\"".$statement."\"</p><ul class=\"likert\"><li class=\"likert\"><label for=\" q".$count."-1\">Not helpful &nbsp;</label><input id=\" q".$count."-1\" name=\" q".$count."\" type=\"radio\" value=\"1\" /></li><li class=\"likert\"><input id=\" q".$count."-5\" name=\" q".$count."\" type=\"radio\" value=\"5\" /><label for=\" q".$count."-5\">&nbsp; &nbsp;Helpful</label></li></ul></div>&nbsp;");
	$count++;
}
?>

<hr/>

<div>
 <p>Please mention any other comments about the design of the website or the survey here.</p> 
<input name="comments" style="height:100px; width:600px;" type="text" /></div>
<br />
<!-- End Content Body -->
</section>
<!-- close container -->
<style type="text/css">fieldset {
    padding: 10px;
    background:#fbfbfb;
    border-radius:5px;
    margin-bottom:5px;
}
</style>

</html>