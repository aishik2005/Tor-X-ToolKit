while true
do
    sleep 15m
	echo "Preventing Bot from sleeping due to Inactivity"
    wget -q -O/dev/null $BASE_URL_OF_BOT
done