while true
do
    # res=$(curl localhost:8000/feed | jq .status)
    res=$(curl --silent -X POST -d '{"amount": 1}' -H 'Content-Type:application/json' localhost:8000/feed | jq .status)
    echo "$res"
    if [ $res == "Hungry" ]
    then
        echo -en "\007"
    fi
    sleep 5
done