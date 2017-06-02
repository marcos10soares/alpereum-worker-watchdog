# alpereum-worker-watchdog
Python watchdog to monitor your workers from ethereum pool Alpereum. Monitor if workers are online, current mining hashrate and receive email notifications if your workers become offline.
If this helps you, feel free to donate to my ETH wallet: 0x6B298eAaB45794A427376F56AD199f00FF3a87d0

# Usage
1. open config.py and fill the fields with your information
2. run alpereum-worker-watchdog_v1.0.py

# Config.py
- Your ethereum wallet to watch:
address = "0x6B298eAaB45794A427376F56AD199f00FF3a87d0"

- Your workers name:
workers = {'WorkerName1', 'WorkerName2', 'WorkerName3'}

- Gmail Account email:
smtpUser = 'youremail@gmail.com'

- Gmail Account password:
smtpPass = 'YourPa$$word'

- To Email - to receive notification:
toEmail = 'destinationemail@gmail.com'

- Subject Text:
subjectText = 'Workers are down: '

- Email Body Text:
body = "Time is money!."
