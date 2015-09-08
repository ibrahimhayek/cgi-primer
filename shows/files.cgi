#!/usr/bin/perl

$query = $ENV{'QUERY_STRING'};
@list = split( /\&/, $query);
my %getRequest=();
foreach (@list) {
    ($var, $val) = split(/=/);
    $val =~ s/\'//g;
    $val =~ s/\+/ /g;
    $val =~ s/%(\w\w)/sprintf("%c", hex($1))/ge;
    $getRequest[$var]=$val;
}
if (index($getRequest['file'], '.js') != -1) {
    print "Content-Type: text/javascript\n\n";
}
if (index($getRequest['file'], '.css') != -1) {
    print "Content-Type: text/css\n\n";
}
if (index($getRequest['file'], '.jpg') != -1) {
    print "Content-Type: image/jpg\n\n";
}
if (index($getRequest['file'], '.jpeg') != -1) {
    print "Content-Type: image/jpeg\n\n";
}
if (index($getRequest['file'], '.png') != -1) {
    print "Content-Type: image/png\n\n";
}
open (MYFILE,  $getRequest['file']);
while (<MYFILE>) {
    chomp;
    print "$_\n";
}
close (MYFILE);
