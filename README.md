# Thoumma Phathavong · Portfolio

A one-page portfolio website that shows my background and five web projects with screenshots.
I made it for job applications, for example the Broadcast Software & Overlay Developer position.

## What is this

The page has three parts:

1. **Profile header**: photo, name, phone / WhatsApp, email, GitHub, Medium, Facebook and Instagram, each with an SVG icon.
2. **Background**:
   - Internship at SVENG IT Solution, with the certificate
   - Education at NUOL and Laotop College
   - SOI Asia network training badges
   - Skills
3. **Projects**, one card each with screenshots, a short description, features and the tech stack:

| # | Project | Link | Stack |
|---|---------|------|-------|
| 01 | The Crimson Vault (live auctions) | in development (local) | Next.js, NestJS, Socket.IO, Prisma, PostgreSQL, Redis |
| 02 | Healthy Cafe POS | https://hcclient.vonthaya.com | SvelteKit, .NET 8, PostgreSQL, React Native, Docker |
| 03 | Y-WEI (waste to rewards) | https://ywei.online | Next.js, React, Google OAuth |
| 04 | Chanthabouly Hotel | https://hotel.ywei.online | Web app, admin dashboard, booking |
| 05 | Tuabaeb School | https://tuabaeb.com | Next.js, Prisma, Tailwind, Cloudflare R2 |

Clicking a screenshot opens it full size. Use ‹ › (arrow keys, or swipe on a phone) to move through the screenshots of that project.

The page is **one self-contained HTML file**. All images are embedded inside it, so it opens offline and can be sent directly on WhatsApp or email. It only needs the internet for the Google Fonts. Without a connection it uses system fonts.

## Files

```
portfolio/
├── template.html      # the page source: edit text, links and layout here
├── build.py           # embeds the screenshots into the template
├── screenshots/       # original PNG screenshots (input for build.py)
│   └── steps/         # section screenshots taken while scrolling
├── images/            # compressed JPG copies (handy for posting separately)
├── portfolio.html     # the built page: open it, send it, deploy it
```

Do not edit `portfolio.html` by hand. It is overwritten on every build.

## Edit and rebuild

Requirements: Python 3 with Pillow (`py -m pip install pillow`).

1. Change text or links in `template.html`.
   Image slots look like `{{hotel_rooms}}`.
2. To change a screenshot, replace the PNG in `screenshots/`, keeping the same name.
   The names are listed in `IMAGES` in `build.py`.
3. Build:

   ```bash
   cd "D:\Sveng Project\portfolio"
   py build.py
   ```

   This writes `portfolio.html`.

**Tuabaeb admin screenshots:** save them as `screenshots/tb-admin.png`, `tb-grades.png`, `tb-attendance.png` and `tb-statistics.png`, then run `py build.py`. They are added under the Tuabaeb card automatically.

## How to deploy

The site is static, with no server or database, so any static host works. You only upload `portfolio.html`.

**Rename it to `index.html` when you upload it.** Web hosts open `index.html` automatically when someone visits your address. With any other name, visitors would have to type `/portfolio.html` at the end of the link.

### Option 1: GitHub Pages (free, `thoumma.github.io`)

1. Create a repo named `thoumma.github.io` on GitHub. You can also use the existing `portfolio` repo, which gives `thoumma.github.io/portfolio`.
2. Copy the page into a deploy folder as `index.html` and push it:

   ```bash
   mkdir "D:\portfolio-site"
   copy "D:\Sveng Project\portfolio\portfolio.html" "D:\portfolio-site\index.html"
   cd "D:\portfolio-site"
   git init
   git add index.html
   git commit -m "Portfolio"
   git branch -M main
   git remote add origin https://github.com/thoumma/thoumma.github.io.git
   git push -u origin main
   ```

3. On GitHub, open **Settings → Pages**. Set **Source: Deploy from a branch** with branch `main` and folder `/ (root)`, then save.
4. After 1–2 minutes the site is live at `https://thoumma.github.io`.

To update: run `py build.py`, copy `portfolio.html` over `D:\portfolio-site\index.html` again, then run `git add index.html`, `git commit -m "Update"` and `git push`.

### Option 2: Hostinger subdomain (e.g. `portfolio.ywei.online`)

`ywei.online` is already on Hostinger.

1. In hPanel, go to **Domains → Subdomains** and create `portfolio` for `ywei.online`.
2. Go to **Files → File Manager** and open the subdomain's folder (for example `public_html/portfolio`).
3. Upload `portfolio.html`, then right-click it and choose **Rename** to `index.html`.
4. Go to **Security → SSL** and turn on SSL for the subdomain.
5. Open `https://portfolio.ywei.online`.

To update: upload the new file and rename it to `index.html` again, replacing the old one.

### Option 3: Netlify Drop (fastest, no account setup needed)

1. Make a folder, put `portfolio.html` in it, and rename the copy to `index.html`.
2. Go to https://app.netlify.com/drop and drag that folder onto the page.
3. You get a link like `https://random-name.netlify.app`. Rename it in **Site settings → Change site name**.

### Option 4: Vercel

Use the same deploy folder as in Option 1 (it holds `index.html`):

```bash
npm i -g vercel
cd "D:\portfolio-site"
vercel --prod
```

## Check before sending

- Open `portfolio.html` in a browser and click through the screenshots.
- Check that the phone number, email and links are correct.
- File size is about 2.5 MB, which is fine for WhatsApp and email attachments.
