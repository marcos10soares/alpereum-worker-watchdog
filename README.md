# alpereum-worker-watchdog
Python watchdog to monitor your workers from ethereum pool Alpereum. Monitor if workers are online, current mining hashrate and receive email notifications if your workers become offline.<br />
If this helps you, feel free to donate to my ETH wallet: 0x6B298eAaB45794A427376F56AD199f00FF3a87d0

# Usage
1. open config.py and fill the fields with your information
2. run alpereum-worker-watchdog_v1.0.py

# Config.py
- Your ethereum wallet to watch: <br />
address = "0x6B298eAaB45794A427376F56AD199f00FF3a87d0"

- Your workers name:<br />
workers = {'WorkerName1', 'WorkerName2', 'WorkerName3'}

- Gmail Account email:<br />
smtpUser = 'youremail@gmail.com'

- Gmail Account password:<br />
smtpPass = 'YourPa$$word'

- To Email - to receive notification:<br />
toEmail = 'destinationemail@gmail.com'

- Subject Text:<br />
subjectText = 'Workers are down: '

- Email Body Text:<br />
body = "Time is money!."

# Dependencies
Python 2.7.8 <br />
requests 2.11.1 <br />
urllib <br />
