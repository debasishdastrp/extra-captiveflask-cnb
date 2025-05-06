#!/bin/bash

echo "Select Template:"
select dir in "templates"/*; do
    if [ -n "$dir" ]; then
        IFS='/'
        read -ra arr <<< $dir

        echo "You Selected: ${arr[1]}"
        if [ -e "plugins/${arr[1]}.py" ]; then
            echo "${arr[1]}.py found"
            echo "Generating Zip....."
            mkdir tmp
            cp -r "templates/${arr[1]}/" tmp/
            cp "plugins/${arr[1]}.py" tmp/
            cd tmp/
            zip -r "${arr[1]}.zip" "${arr[1]}/"
            zip -r "${arr[1]}.zip" "${arr[1]}.py"
            mv "${arr[1]}.zip" ../
            cd ../
            rm -rf tmp/
        else
            echo "${arr[1]}.py not found. Aborted"
        fi
        break
    else
        echo "Invalid selection, please try again."
    fi
done