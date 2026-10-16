# Midha Limited website

Static website for [midha.co.nz](https://midha.co.nz): test & tag across New Zealand, plus heat pump cleaning and electrical services in Greater Wellington.

- `site/` is the website. Deploy this folder as-is (no build step).
- `build.py` regenerates the HTML pages in `site/` from one place (header, footer, prices, reviews, form). Edit it, then run `python3 build.py`.
- `docs/DEPLOY-TO-CLOUDFLARE.md` explains how to put it live.
- `docs/DESIGN-SPEC.md` is the design specification and build handoff.
- `docs/GOOGLE-SETUP.md` covers Search Console, Google Business Profile, directories and Google Ads.

## Cloudflare (connected to this repo)

The site runs on Cloudflare Workers static assets. `wrangler.jsonc` points Cloudflare at the `site` folder.

| Setting | Value |
|---|---|
| Production branch | `main` |
| Build command | *(leave empty)* |
| Deploy command | `npx wrangler deploy` |
| Root directory | `/` |

Every push to `main` redeploys the site automatically.

If a push doesn't redeploy, open the Worker's **Settings > Builds** in Cloudflare. A banner saying the project is disconnected from your Git account means Cloudflare's GitHub app has lost access: click **Manage**, give the **Cloudflare Workers and Pages** app access to this repo, then push again.

## Test & tag city pages

City pages (`/test-and-tag/<city>/`) are generated from the `CITIES` list in `build.py`. Each city has its own intro, industries, nearby areas and FAQs. Keep them genuinely different: Google treats near-identical city pages as spam.

## Quote form

Set your Formspree form ID in `site/assets/js/main.js` (`FORMSPREE_ID`). Until it is set, the form opens the visitor's email app with their details filled in.

## Google Ads tracking

Set `GOOGLE_ADS_ID`, `ADS_LABEL_FORM` and `ADS_LABEL_CALL` in `site/assets/js/main.js`. Nothing from Google loads while `GOOGLE_ADS_ID` is empty.

## Giveaway

The Facebook post link is `FB_POST` in `build.py`. The "Next draw" date updates itself (end of March, June, September, December).
