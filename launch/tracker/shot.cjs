const { chromium } = require('playwright');
(async () => {
  const [file, outDir] = process.argv.slice(2);
  const b = await chromium.launch(); const errors = [];
  for (const [name, w] of [['desk', 1280], ['phone', 400]]) {
    const p = await b.newPage({ viewport: { width: w, height: 900 }, deviceScaleFactor: 1 });
    p.on('pageerror', e => errors.push(String(e))); p.on('console', m => { if (m.type() === 'error') errors.push(m.text()); });
    await p.goto('file://' + file); await p.waitForTimeout(1500);
    console.log(name, 'scrollWidth', await p.evaluate(() => document.documentElement.scrollWidth));
    await p.screenshot({ path: `${outDir}/${name}.png` }); await p.close();
  }
  console.log('errors', JSON.stringify(errors)); await b.close();
})();
