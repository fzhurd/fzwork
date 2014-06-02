<?php

//*****************************************************verification
require_once('recaptchalib.php');
$privatekey = "6LerBtISAAAAAA_jd693HeeCkc02ONeEHKh-H06D";
$resp = recaptcha_check_answer ($privatekey,
                         $_SERVER["REMOTE_ADDR"],
              $_POST["recaptcha_challenge_field"],
              $_POST["recaptcha_response_field"]);

if (!$resp->is_valid) {
	// What happens when the CAPTCHA was entered incorrectly
	die ("The reCAPTCHA wasn't entered correctly. Go back and try it again." .
	     "(reCAPTCHA said: " . $resp->error . ")");
} else {
	echo "you succeed";
}

?>