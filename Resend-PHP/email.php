<?php
if (($_SERVER["REQUEST_METHOD"] == "POST")) {
    require __DIR__ . './vendor/autoload.php';
    //$resend = Resend::client('re_gQYDfsg9_DY6dVbrbi1yM6nTHSyuSKNkc');

    $nombre_cliente       = $_POST['nombre_cliente'];
    $email_cliente        = $_POST['email_cliente'];
    $mensaje_cliente      = $_POST['mensaje_cliente'];
    $terminos = $_POST['terminos'] ? 1 : 0;


    $resend->emails->send([
        'from' => 'Acme <onboarding@resend.dev>',
        'to' => ['urian1213vieragmail.com'],
        'subject' => 'hello world',
        'html' => '<strong>it works!</strong>',
    ]);
}
