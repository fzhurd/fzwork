#!/bin/bash

#replace the "" with NA
sed "s/\"\"/NA/g" tcsv1.txt >tcsv2.txt

#replace the "" with empty space
sed "s/\"\"//g" tcsv1.txt >tcsv2b.txt



# $ cat pets.txt
# This is my cat
#   my cat's name is betty
# This is my dog
#   my dog's name is frank
# This is my fish
#   my fish's name is george
# This is my goat
#   my goat's name is adam

$ sed "3s/my/your/g" pets.txt
# This is my cat
#   my cat's name is betty
# This is your dog
#   my dog's name is frank
# This is my fish
#   my fish's name is george
# This is my goat
#   my goat's name is adam