docker run -itd --name firefox -p 4445:4444 selenium/standalone-firefox
docker run -itd --name chrome -p 4444:4444 selenium/standalone-chrome
python screenshot.py
echo -e " \n removing containers"
docker rm -f `docker ps -aq`
