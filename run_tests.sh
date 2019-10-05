#! /usr/bin/env sh

echo "########################"
echo "## Testing myfind.py ###"
echo "########################"

count=0  # number of test cases run so far

for t in test/*.in; do
	name=$(basename $t .in)
	output=test/$name.out
    
    text=$(cat $t)
    readarray args <<< "$text"
    # echo ${args[*]}
    
	if ./myfind.py ${args[*]} | sort - | diff - $output ; then
        echo "Test $name: Succeeded"
    else
        echo "Test $name: Failed"
    fi
	count=$((count + 1))
    echo -------------------------------------------------------
done

echo "Done!"
echo "Finished running $count tests!"