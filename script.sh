#!/bin/bash

# make an executable xhmod +x ./script
# run from windows console: sed -i -e 's/\r$//' script.sh ; ./script.sh

echo "Dir is:"
pwd
echo "User is:"
whoami

user__=$(whoami)
echo "$user__"

prime=$((31))
echo $((prime*3))

number=$((1 + 2 + 3))
echo "$number"

if grep $((user__)) /etc/passwd
then
  echo "The user $user__ exists"
fi

value=128
if [ $value -gt 120 ]
then
  echo "Ya YA valuen greatten"
else
  echo "Nain NAin NAin!!!!!"
fi

s="Wanna hit record!"
t="Hard as a rock!"

if [ "$t" != "$s" ]
then
  if [ "$s" \> "$t" ]
  then
    echo "s > t"
  else
    echo "t > s"
  fi
fi