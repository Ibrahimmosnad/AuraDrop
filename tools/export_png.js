// Renders selected SVG assets to PNG with Playwright: node tools/export_png.js
const {chromium} = require(process.env.PLAYWRIGHT_PATH || 'playwright');
const path = require('path'), fs = require('fs');
const root = path.resolve(__dirname, '..');
const jobs = [
  ['assets/social/og-card.svg', 'assets/social/og-card.png', 1200, 630],
  ['assets/social/banner.svg', 'assets/social/banner.png', 1500, 500],
  ['assets/social/profile.svg', 'assets/social/profile.png', 800, 800],
  ['assets/social/favicon.svg', 'assets/social/favicon-32.png', 32, 32],
  ['assets/social/favicon.svg', 'assets/social/favicon-180.png', 180, 180],
  ['logo/auradrop-app-icon.svg', 'assets/social/app-icon-512.png', 512, 512],
  ['assets/ui/phone-diagnosis.svg', 'assets/ui/phone-diagnosis.png', 600, 1200],
];
(async () => {
  const b = await chromium.launch();
  for (const [src, out, w, h] of jobs) {
    const p = await b.newPage({viewport: {width: w, height: h}});
    const svg = fs.readFileSync(path.join(root, src), 'utf8');
    await p.setContent(`<body style="margin:0;background:transparent"><div style="width:${w}px;height:${h}px;display:flex">${svg.replace('<svg ', '<svg style="width:100%;height:100%" ')}</div>`);
    await p.screenshot({path: path.join(root, out), omitBackground: true});
    await p.close();
  }
  await b.close();
})();
