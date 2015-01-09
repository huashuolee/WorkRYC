#!/bin/bash

for ((i=0; i<=50; i++));
do
   echo -n $i ' '
   adb shell content insert --uri content://settings/system --bind name:s:user_rotation --bind value:i:1
   sleep 1
   adb shell content insert --uri content://settings/system --bind name:s:user_rotation --bind value:i:0
   sleep 3
done

