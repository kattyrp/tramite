<?php
$manejador="mysql";
$usuario="root";
$clave="";
$servidor="";
$base="";
$cadena="$manejador:host=$servidor;dbname=$base";
$cnx=new PDO ($cadena,$usuario,$clave);
?>
