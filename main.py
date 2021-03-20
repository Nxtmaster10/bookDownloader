import os

import win32com.client as win32

from inepthepub import decryptBook
from convert_to_mobi import convert, get_final_filename


# Opens the mail program on your computer as automatic sending is somehow blocked by amazon


def open_mail(file):
    outlook = win32.Dispatch('outlook.application')
    outlook_mail = outlook.CreateItem(0)
    outlook_mail.To = 'yourkindlemail@kindle.com'  # Kindle-Mail - obtained from
    # https://www.amazon.de/hz/mycd/digital-console/alldevices
    # -> click the device -> E-Mail
    outlook_mail.Subject = 'Book'
    outlook_mail.Attachments.Add(Source=file)
    outlook_mail.Display(True)


if __name__ == '__main__':
    input_folder = os.path.abspath("input")
    to_mail_folder = os.path.abspath("output")
    user_key = open(os.path.abspath("adobekey_1.der"), 'rb').read()  # Adobe key from running adobekey.py
    for filename in os.listdir(input_folder):
        print('### Converting {} ###'.format(filename))
        drm_removed_file = os.path.join(os.path.abspath("drm_removed"), filename)
        output_file = os.path.join(to_mail_folder, get_final_filename(filename))
        book = os.path.normpath(os.path.join(input_folder, filename))

        decryptBook(user_key, book, drm_removed_file)
        print('### Decrypted! ###')

        convert(filename)
        print('### Converted! ###')

        open_mail(output_file)
        print('### Mail sent! ###')

        os.remove(os.path.join(input_folder, filename))
        os.remove(drm_removed_file)
        os.remove(output_file)
