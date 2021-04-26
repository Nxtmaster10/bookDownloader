# Book downloader

This is a script to send E-Books you bought from somewhere else than Amazon to your Kindle.

In order to work properly the script needs to create the 3 folders `input, output` and `drm_removed` on the initial run.

This script needs [Calibre](https://calibre-ebook.com/) to work as it uses the `ebook-convert` command.

Further you need [Adobe Digital Editions](https://www.adobe.com/solutions/ebook/digital-editions/download.html) to
remove the DRM from the book.

# Run the script

If this is the first time you use the script you need to run [adobekey.py](./adobekey.py).

Set your kindle mail in [main.py](./main.py) on line 15. You obtain from this
email [here](https://www.amazon.de/hz/mycd/digital-console/alldevices) by clicking on your device and then on E-Mail.

Please make sure you whitelist your email [here](https://www.amazon.de/hz/mycd/myx#/home/settings) by heading
to `Personal Document Settings` and then click on `Add a new approved e-mail address`

Then you place your ebook in the `input` folder. Run [main.py](./main.py) using the command ```python3 main.py```.

Ths script will open outlook with the converted book attached to a new mail.

