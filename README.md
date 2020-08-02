# AngryInternetUser

🐦 Angry Internet User tweets if the internet is offline or slower than what you're paying for

## Usage

To get started, you'll need to install this as a Python package. Download the wheel from the [releases tab](https://github.com/gideontong/AngryInternetUser/releases) or run the entry point `python main.py`.

### Installation Steps

You'll need Python to run this project. `AngryInternetUser` supports both Python 2.x and 3.x, but as Python 2.x is out of date, support for Python 2.x is not guaranteed and will work only as long as code changes are backwards-compatible. It is reccomended you install Python 3.7 or later.

After installation, simply clone the repository and run:

```bash
python main.py
```

or run the build script and install the generated wheel:

```bash
./build
pip install bin/angryinternetuser-x.x.x.whl
```

## Premise

Based on the article from 2016 [describing a man's woe with Comcast](https://arstechnica.com/information-technology/2016/02/comcast-customer-made-bot-that-tweets-at-comcast-when-internet-is-slow/). The live Twitter feed is [here](https://twitter.com/A_Comcast_User). Their code was published [here](https://pastebin.com/WMEh802V). Their code was not copied, but is an inspiration for this project.

## Credits

This package is created by [Gideon Tong](https://gideontong.com). Subscribe to updates [here](https://blog.gideontong.com) or check out a directory of projects [here](https://gideontong.me).

## License

MIT License. (c) Copyright Gideon Tong 2020
