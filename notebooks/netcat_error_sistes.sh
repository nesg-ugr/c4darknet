#!/bin/bash

for site in `cat site_error.txt`;
do
	bash /usr/bin/ncat -v --proxy localhost:4444 $site &> $site.txt &
done

