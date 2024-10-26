[![Deploy static content to Pages](https://github.com/AnnikaStein/my-comp/actions/workflows/static.yml/badge.svg)](https://github.com/AnnikaStein/my-comp/actions/workflows/static.yml)

# my-comp

Custom landing page for WCA Competitions, targeted at competitors looking for live results, schedule, more information. To be used at competitions with respective QR code (laminated sheets).

If you want to use the landing page:

1. Fork the repository.
2. Create a GitHub Pages action to deploy the website.
3. Modify all links and containers accordingly. You may want to remove the translation (or modify it), you may want to update the footer with icons and links to your liking.
4. But most importantly, run the QR-code generator again for your own fork / your own instance of the landing page URL! Otherwise, the code will point to _this_ instance here. An example is given in https://github.com/AnnikaStein/my-comp/blob/master/python/qr_gen.py (software: python3 with package qrcode). If you use this tool, please replace the URL in [Line#13](https://github.com/AnnikaStein/my-comp/blob/master/python/qr_gen.py#L13) accordingly. You can in principle use whatever tool you like - just note that some tools may generate non-permanent codes that expire some day and then you can throw away the sheets (🫠). This tool used here generates a static QR code that does not come with an expiry date, it's just a bit of ink on paper that points to our very own website by construction, without a detour imposed by paid services. 🙂
5. Put the QR-code onto a sheet, print it, (optional: laminate it to reuse across competitions). There is a template (Apple Pages) in this folder: https://github.com/AnnikaStein/my-comp/blob/master/printing .
