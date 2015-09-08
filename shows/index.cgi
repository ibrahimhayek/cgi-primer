#!/usr/bin/perl

# This is used for json encode and decode
use JSON qw( decode_json );

# this is used for checking if image url exists or not
use LWP::Simple;

# this is content type of output that script generates
print "Content-Type: text/html\n\n";


# this is done for converted the query string into array named getRequest
$query = $ENV{'QUERY_STRING'};
@list = split( /\&/, $query);
$checking=0;
my %getRequest=();
foreach (@list) {
    ($var, $val) = split(/=/);
    $val =~ s/\'//g;
    $val =~ s/\+/ /g;
    $val =~ s/%(\w\w)/sprintf("%c", hex($1))/ge;
    $getRequest{$var}=$val;
    if($var eq 'zipcode' || $var eq 'radius')
    {
        $checking++;
    }
}


# html output is stored into a variable named "html" this variable is printed in the end of file
$html="<!DOCTYPE html>";
$html.="<html xmlns='http://www.w3.org/1999/xhtml'>";
$html.="<head>";
$html.="<meta charset='utf-8' />";

# title of the page
$html.="<title>==GOFOOTLIGHTS==</title>";

# css and javascript is comming from a file called files.js

# style sheet path of the page
$html.="<link href='files.cgi?files=css/style.css' rel='stylesheet' type='text/css' />";

#javascript path of the page
$html.="<script type='text/javascript' src='files.cgi?files=js/main.js' ></script>";
$html.="</head>";
$html.="<body>";
$html.="<div class='body_container'>";
$html.='<div class="header_holder">';
$html.='<div class="banner_image_holder">';

# banner image of the page
$html.='<img class="banner_image" src="http://gofootlights.com/wp-content/uploads/2015/08/Footlights-banner-logo-tweaked.jpg">';
$html.='</div>';
$html.='</div>';
$html.='<div class="main_content_holder">';
$html.='<div class="shows_search_form_holder">';
$html.='<form action="" method="get"> ';
$html.='<div class="single_field_holder">';
$html.='<div class="lable_holder f_left">';
$html.='Zip Code :';
$html.='</div>';
$html.='<div class="input_holder f_left">';
$html.='<input type="text" required="required" name="zipcode" value="'.$getRequest{'zipcode'}.'">';
$html.='</div>';
$html.='<div class="clear"></div>';
$html.='</div>';
$html.='<div class="single_field_holder">';
$html.='<div class="lable_holder f_left">';
$html.='Radius :';
$html.='</div>';
$html.='<div class="input_holder f_left">';
$html.='<input type="text" required="required" name="radius" value="'.$getRequest{'radius'}.'" >';
$html.='</div>';
$html.='<div class="clear"></div>';
$html.='</div>';
$html.='<div class="single_field_holder">';
$html.='<div class="submit_button_holder">';
$html.='<input type="submit" name="submit" value="Find Events">';
$html.='</div>';
$html.='</div>';
$html.='</form>';
$html.='</div>';
$html.='<div class="search_results_holder">';
# this is to check if request is made or not
if($checking>=2)
{

    # this is for searching the data from goofootlights api
    use LWP::UserAgent;
    my $ua = new LWP::UserAgent;
    my $response = $ua->get('http://gofootlights.com/ibrahim/?param=events&action=searchEvent&zip='.$getRequest{'zipcode'}.'&radius='.$getRequest{'radius'});
    unless ($response->is_success) {
    }
    my $content = $response->decoded_content();
    if (utf8::is_utf8($content)) {
        binmode STDOUT,':utf8';
    } else {
        binmode STDOUT,':raw';
    }
    # my $result = decode_json($content);
    #print $content;
    # this is to decode the json into array
    my $result = decode_json($content);

    # this is to check if data exists or not
    if($result->{'msg'}>0)
    {
        # this is for running loop of each show
        my @data = @{ $result->{'data'} };
        foreach my $f ( @data ) {
            $html.='<div class="single_search_element_holder">';
            $html.='<div class="image_container f_left">';
            # this is for checking if image exists or not
            my $url = 'http://gofootlights.com/covers/'.$f->{"ProjectID"}.'.jpg';
            if (head($url)) {
                $html.='<img src="'.$url.'">';
            } else {
                $html.='<img src="http://gofootlights.com/covers/default.jpg">';
            }
            $html.='</div>';
            $html.='<div class="show_details_container f_left">';
            $html.='<div class="title_holder">';
            $html.='<h2>';
            #show Title
            $html.=$f->{"Title"};
            $html.='</h2>';
            $html .=  '<div class="show-dates">';
            #opening date of show
            $html .= $f->{'OpeningDate'};
            $html .= ' - ';
            #closing date of show
            $html .=  $f->{'ClosingDate'};
            $html .= '</div>';
            $html.='<div class="description_holder">';
            #show Description
            $html.=$f->{"PlayDescription"};
            $html.='</div>';
            $html.='</div>';
            $html.='</div>';
            $html.='<div class="clear"></div>';
            $html.='</div>';

        }
    }
}



$html.='</div>';
$html.='</div>';
$html.='<div class="fotter_holder">';
$html.='</div>';
$html.='</div>';
$html.='</body>';
$html.='</html>';

print $html;