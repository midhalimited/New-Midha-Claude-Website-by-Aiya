# Midha Limited website

Static website for [midha.co.nz](https://midha.co.nz): test & tag, heat pump cleaning and electrical services across Greater Wellington.

- `site/` is the website. Deploy this folder as-is (no build step).
- `build.py` regenerates the HTML pages in `site/` from one place (header, footer, prices, reviews, form). Edit it, then run `python3 build.py`.
- `docs/DEPLOY-TO-CLOUDFLARE.md` explains how to put it live.
- `docs/DESIGN-SPEC.md` is the design specification and build handoff.

## Cloudflare Pages (connected to this repo)

| Setting | Value |
|---|---|
| Framework preset | None |
| Build command | *(leave empty)* |
| Build output directory | `site` |

Every push to `main` then redeploys the site automatically.

## Quote form

Set your Formspree form ID in `site/assets/js/main.js` (`FORMSPREE_ID`). Until it is set, the form opens the visitor's email app with their details filled in.
