<?php
if (($_SERVER["REQUEST_METHOD"] == "POST")) {
    //Para windows el path cambia
    //require __DIR__ . './vendor/autoload.php';

    require __DIR__ . '/vendor/autoload.php';

    // $resend = Resend::client('aqui va la key');
    $resend = Resend::client('');

    $nombre_cliente       = $_POST['nombre_cliente'];
    $email_cliente        = $_POST['email_cliente'];
    $mensaje_cliente      = $_POST['mensaje_cliente'];
    $terminos = $_POST['terminos'] ? 1 : 0;


    try {
        $result = $resend->emails->send([
            'from' => 'PHP <php@resend.dev>',
            'to' => ['urian1213viera@gmail.com'],
            'subject' => 'Hola comunidad WebDeveloper ',
            'html' => '<p>El cliente  <strong>' . $nombre_cliente . '</strong> con email ' . $email_cliente . ' le envia este mensaje </p>
            <strong>' . $mensaje_cliente . '</strong> 🙀',
        ]);
    } catch (\Exception $e) {
        exit('Error: ' . $e->getMessage());
    }

    echo $result->toJson();
    header("Location: index.html");
    die();
}
