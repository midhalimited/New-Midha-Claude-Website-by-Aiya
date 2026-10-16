# Getting found on Google

The website is already set up for Google: page titles, Google data on every page, a sitemap, and a page for each main test & tag city. These steps are the parts only you can do.

## 1. Google Search Console (do this first, free)

1. Go to search.google.com/search-console and sign in with midhalimited@gmail.com.
2. Choose **Add property → Domain** and type `midha.co.nz`.
3. Google gives you a TXT record. In Cloudflare, open **midha.co.nz → DNS → Add record**, choose **TXT**, name `@`, paste the value, and save. Back in Search Console, press **Verify**.
4. Open **Sitemaps**, enter `sitemap.xml` and press **Submit**.
5. Use **URL inspection** on your home page and the Test & Tag page and press **Request indexing**.

New pages usually start appearing within days to a few weeks. Ranking higher takes longer and comes from reviews, links and time.

## 2. Google Business Profile (Maps)

1. Go to business.google.com and claim or create **Midha Limited**.
2. Choose that you **deliver services at customers' locations**, and **hide your home address** if customers don't visit you.
3. Add service areas: Google allows up to 20, within about 2 hours' drive of your base. Use Wellington region areas (Wainuiomata, Lower Hutt, Upper Hutt, Wellington, Porirua, Kāpiti Coast and so on).
4. Add your services (Test and tag, Heat pump cleaning, Electrical services), hours, phone, website `https://midha.co.nz` and real job photos.
5. After each job, send customers your Google review link. Reviews are the biggest local ranking factor.

Note: Google Maps results will only show you around Wellington. Other cities are reached through the city pages and Google Ads.

## 3. NZ directories (same name, phone and website everywhere)

List Midha Limited on NoCowboys, Builderscrack, Finda, Yellow and Neighbourly. Use exactly: **Midha Limited · 022 407 8603 · https://midha.co.nz**.

## 4. Google Ads (when you're ready)

1. Create an account at ads.google.com.
2. Create two conversion actions: **Submit lead form** and **Phone call clicks on your website**.
3. Google shows an ID like `AW-123456789` and a label for each conversion. Send them to Claude, or paste them into `site/assets/js/main.js` (`GOOGLE_ADS_ID`, `ADS_LABEL_FORM`, `ADS_LABEL_CALL`).
4. Point city campaigns at the matching city page, for example ads in Christchurch → `https://midha.co.nz/test-and-tag/christchurch/`. Heat pump ads should target the Wellington region only.
