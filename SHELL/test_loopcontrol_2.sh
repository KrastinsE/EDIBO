#!/bin/bash

a=0

while [ $a -lt 100 ]
do
   echo $a
   if [ $a -eq 30 ]
   then
      break
   fi
   a=`expr $a + 1`
done
