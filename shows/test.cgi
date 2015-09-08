#!/usr/bin/perl -w

use CGI;

$cgi = new CGI();

print $cgi->header();

print '<?xml version="1.0" encoding="UTF-8"?>';

print '<!DOCTYPE html>
<html>
   <head>

      	<title>Perl CGI test</title>
   </head>
   <body>';

print '
      <p>
         Hello world!
      </p>';


print '
   </body>

</html>
';