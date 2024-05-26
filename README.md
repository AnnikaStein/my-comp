[![Deploy static content to Pages](https://github.com/AnnikaStein/my-comp/actions/workflows/static.yml/badge.svg)](https://github.com/AnnikaStein/my-comp/actions/workflows/static.yml)

# my-comp

Custom landing page for WCA Competitions, targeted at competitors looking for live results, schedule, more information. To be used at GCA-related competitions with respective QR code (laminated sheets).

Please contact your delegate, or the maintainer Annika Stein directly. (For delegates: please use slack, for organizers: available via whatsapp, best to use the respective competition group chat or DM).

## How does it work

We need the following from you: the `competition-ID`. This will be inserted into the respective links on the landing page.

Therefore, if your comp is upcoming:

1. Login to WCA live.
2. Go to 'My competitions'.
3. From 'Importable competitions' select the respective competition and import it. If there is nothing to import, the URL has been generated already (by you or your co-organizers / co-delegates).
4. Get back to the maintainer (see above) with your `competition-ID` (e.g. "GermanOpen2024").

Your landing page will be updated such that you can use the laminated QR codes sent to you!

### Multiple comps

If there are two competitions happening on the same weekend, so basically in the same time frame, the optional multi-comp feature will be made available to automatically locate users via GPS and select the corresponding competition (fallback solution: manual selection of the competition by the user).

Therefore, nothing special to do from your side, the maintainer keeps an eye on the German Cube Association calendar and toggles the single-dual-competition switch. Just repeat steps 1.-4. for any upcoming competition you are in charge of!

### Series comps

In this case, time-dependent competition switches are implemented utilizing the current UTC date and time. In the manual selection, series comps are treated like different locations, e.g. as individual entries to select from.

## If you want to use the tool for other, non-GCA-related competitions (e.g. different RO)

Of course, the links currently do not point to anything outside GCA-related domains. Second, the QR-code is tightly linked to the present original repo and website / URL.

If you want to use the landing page outside the GCA RO:

1. Fork the repository.
2. Create a GitHub Pages action to deploy the website.
3. Modify all links and containers accordingly. You may want to remove the translation (or modify it), you may want to update the footer with icons and links to your liking.
4. But most importantly, run the QR-code generator again for your own fork / your own instance of the landing page URL! Otherwise, the code will point to _this_ GCA-instance here. An example is given in https://github.com/AnnikaStein/my-comp/blob/master/python/qr_gen.py (software: python3 with package qrcode). If you use this tool, please replace the URL in [Line#13](https://github.com/AnnikaStein/my-comp/blob/master/python/qr_gen.py#L13) accordingly. You can in principle use whatever tool you like - just note that some tools may generate non-permanent codes that expire some day and then you can throw away the sheets (🫠). This tool used here generates a static QR code that does not come with an expiry date, it's just a bit of ink on paper that points to our very own website by construction, without a detour imposed by paid services. 🙂
5. Put the QR-code onto a sheet, print it, (optional: laminate it to reuse across competitions). There is a template (Apple Pages) in this folder: https://github.com/AnnikaStein/my-comp/blob/master/printing .
