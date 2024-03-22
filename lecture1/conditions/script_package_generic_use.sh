#!/bin/sh

package_path='/usr/bin'
package_name='htop'

# if [ ! -f "$package_path/$package_name" ]
if command -v $package_name
then
    echo "command  $package_name available , lets run it ."
else
    echo "command  $package_name isnt available ...."
    apt update && apt install  htop -y
fi

$package_name
