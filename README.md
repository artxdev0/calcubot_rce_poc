
# @calcubot Telegram bot RCE exploit

The exploit and explanation for the RCE and DoS vulnerability
are published here for educational purposes only. If you are
a developer @calcubot, please take a look at the fix I suggested
for your problem.

## Explanation

The bot has its own filter for bad words. Such as os, system,
sys, etc. But no one bothers you to use hex values ​​in
conjunction with globals() and vars() to obtain variables.

The next problem that prevents you from freely running the code
is the telegram limit on the length of the request. To solve
this problem, the following solution was invented:

1. Calculate a maximum size of payload that executes the OS commands. (`ln: 35`)
2. Count bytes per payload (per one request) to transport file data. (`ln: 44`)
3. Read X bytes from step 2 the file with payload. (`ln: 70`)
4. Generate a full payload which executes an OS command to write
payload on target. (`ln: 80`)
5. Repeat step 3 entire payload has been sent to the target.
6. After the payload is delivered to the target, we launch it. (`ln: 98`)

Algorithm is slow, because of telegram queries limit and telegram
limit of queries per second, but delivers files efficiently and
allows to exploit the host machine.

RCE exploit (`exploit.py`):
- This just follows the algorithm: writing `payload.py` to the target
and launch it.

DoS exploit (`dos.py`):
- This only executes the `kill 1` command on the target to shutdown
the host. While I was researching the mechanism of the bot, I received
information that the bot is hosted inside a Docker image. Therefore,
the DoS exploit just destroys the main Docker process.

## Usage

Install Python3 and requirements for it:
```sh
$ pip3 install pyrogram pyrolog
```

Fill `API_ID` and `API_HASH` values. You can get it [here](https://telegram.org).

After, start `nc -nlp 4444` on your computer and fill IP and PORT in `payload.py`.

After, run the exploit:
```sh
$ python exploit.py
```

## Suggested fix of the problem

I also programmed multifunctional calculators (I'm cool) and
encountered a security problem. A great solution was to use `evalidate`.
[See `evalidate` on PyPI.](https://pypi.org/project/evalidate/).

Just limit the use of nodes, add allowed functions and the
problem will be solved!

## Disclaimer

This repository is for educational purposes only. The information provided here is intended to help developers understand the vulnerability and protect their systems. Do not use this exploit maliciously or without permission. Use of this PoC is at your own risk. The author is not responsible for any damages or legal issues that may arise from the use of this information.

## Contact me

[My telegram](https://telegram.org/ftdot).
