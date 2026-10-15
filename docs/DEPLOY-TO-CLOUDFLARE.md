# Putting the Midha website live on Cloudflare

The site is plain HTML, CSS and JavaScript, so there's no build step. Cloudflare Pages hosts it for free.

## 1. Upload the site (about 5 minutes)

1. Unzip `midha-website.zip`. You'll get a folder called `site`.
2. Log in to the Cloudflare dashboard and open **Workers & Pages**.
3. Click **Create**, choose the **Pages** tab, then **Upload assets** (Direct Upload).
4. Name the project `midha` and click **Create project**.
5. Drag the **contents of the `site` folder** into the upload box (not the zip itself), then click **Deploy site**.
6. Cloudflare gives you a preview address like `midha.pages.dev`. Open it and check everything looks right.

## 2. Connect midha.co.nz

1. In the Pages project, open **Custom domains** and choose **Set up a custom domain**.
2. Enter `midha.co.nz` and confirm. Because the domain is already in your Cloudflare account, the DNS record is added for you.
3. Repeat for `www.midha.co.nz`.
4. To send `www` to the main address, go to **Rules › Redirect Rules** and redirect `www.midha.co.nz/*` to `https://midha.co.nz/${1}` with a 301.

If an old website is still connected to midha.co.nz (for example, Wix or another host), remove its DNS records first, or Cloudflare will ask you to replace them.

## 3. Make the quote form send to your email

The form works straight away by opening the visitor's email app with their details filled in. To receive enquiries directly in your Gmail instead:

1. Create a free account at formspree.io using **midhalimited@gmail.com**.
2. Create a new form. Formspree gives you an ID such as `xyzabcd` (the last part of `https://formspree.io/f/xyzabcd`).
3. Open `site/assets/js/main.js`, find `var FORMSPREE_ID = '';`, and put your ID between the quotes: `var FORMSPREE_ID = 'xyzabcd';`
4. Upload the site again (Pages project › **Create deployment** › drag the `site` folder contents).

After a successful send, visitors land on the `/thanks/` page.

## 4. Optional extras

- **Visitor stats:** in the Pages project, turn on **Web Analytics**. It's free and doesn't use cookies, which matches the privacy page.
- **Google:** add the site to Google Search Console and submit `https://midha.co.nz/sitemap.xml`. Update your Google Business Profile with the new website address.

## Updating later

Edit the files and upload the `site` folder contents again as a new deployment. Cloudflare keeps every past version, so you can roll back with one click under **Deployments**.

## What's in the folder

| File / folder | What it does |
|---|---|
| `index.html` and each folder's `index.html` | The pages |
| `assets/css/styles.css` | All colours, fonts, spacing (design tokens at the top) |
| `assets/js/main.js` | Menu, form, animations. The Formspree ID goes here |
| `assets/img/` | Your photos and logo, resized for fast loading |
| `_headers` | Cloudflare security and caching rules |
| `_redirects` | Sends old addresses (like `/services`) to the new pages |
| `sitemap.xml`, `robots.txt` | For Google |
| `404.html` | "Page not found" page |
