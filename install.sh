sudo apt update
wget https://github.com/adafruit/Adafruit_AMG88xx_python/archive/refs/heads/master.zip
unzip master.zip
cd Adafruit_AMG88xx_python-master/
sudo python3 setup.py install
sudo pip3 install scipy
sudo pip3 install colour
sudo apt-get install libatlas-base-dev
wget https://github.com/vshymanskyy/blynk-library-python/archive/master.zip
unzip master.zip 
cd blynk-library-python-master/
sudo python3 setup.py install
cd .local
export PATH="$HOME/bin:$PATH"
