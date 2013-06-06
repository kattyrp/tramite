<?php
$manejador="mysql";
$usuario="root";
$clave="";
$servidor="localhost";
$base="apuesta";
$cadena="$manejador:host=$servidor;dbname=$base";
$cnx=new PDO ($cadena,$usuario,$clave);
?>
