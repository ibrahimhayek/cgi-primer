#!/usr/bin/perl

# Sample JSON String
my $content = '[{"name":"Ibrahim", "age":"23"},{"name":"Steve", "age":"46"}]';

# Init array to use later
my @final_final_values;
# Split whole JSON because we know what JSON
# structure looks like
my @array = split(/},{/, $content);

# Loop through this split to continue parsing...
for my $item ( @array ) {
 # continue splitting, now we want each individual
 # item in list of the above split, which is each record
 # in the json
 my @content = split(/,/, $item);
 
 for my $item2 (@content) {
    # split keys and values
    my @values = split(/:/, $item2);
    
    my @final_values;
    # loop through this split to parse strings inside quotes
    for my $val4key (@values) {
        if ($val4key =~ m/"(.*?)"/) {
          push(@final_values, $1);
        }
    }
    for my $ahsdfh (@final_values) {
      # finally, get only values for each key, and not the
      # key names
      if($ahsdfh ne 'name' && $ahsdfh ne 'age') {
        push(@final_final_values, $ahsdfh);
      }
    }
 }
}

my @names;
my @age;
my $counter = 1;
# Loop through final array of strings, and parse
# each value for key, putting in separate arrays,
# since we have predefined JSON and know what
# the structure looks like
for my $fhdsa (@final_final_values) {
    if ($counter % 2 == 0) {
        print ", age: $fhdsa";
        push @age, $fhdsa;
        print "\n";
    } else {
        print "Name: $fhdsa";
        push @names, $fhdsa;      
    }
    $counter = $counter + 1;
}