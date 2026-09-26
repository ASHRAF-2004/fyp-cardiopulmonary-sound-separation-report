// Isolated preparation-HTML smoke check; uses existing project dependencies only.
import assert from 'node:assert/strict';
import { mkdir, writeFile } from 'node:fs/promises';
import { fileURLToPath } from 'node:url';
import { chromium } from '../../implementation/frontend/node_modules/playwright-core/index.mjs';

const output = new URL('./output/playwright/', import.meta.url);
await mkdir(output, { recursive: true });
const browser = await chromium.launch({ executablePath: '/usr/bin/google-chrome', headless: true });
const report = { purpose: 'Preparation HTML only; not academic-layout or application certification', browser: browser.version(), cases: [] };
const expected = ['Introduction', 'Literature Review', 'Requirements Analysis', 'System Design', 'Implementation', 'Testing', 'Conclusion', 'Preparation references'];
try {
  for (const [name, width, height] of [['desktop', 1440, 1000], ['mobile', 360, 800]]) {
    const context = await browser.newContext({ viewport: { width, height }, deviceScaleFactor: 1 });
    const page = await context.newPage();
    const errors = [];
    const networkRequests = [];
    page.on('pageerror', error => errors.push(error.message));
    page.on('console', message => { if (message.type() === 'error') errors.push(message.text()); });
    page.on('request', request => { if (/^https?:/.test(request.url())) networkRequests.push(request.url()); });
    await page.goto(new URL('./_build/fyp2-preparation.html', import.meta.url).href, { waitUntil: 'networkidle' });
    await page.locator('main').waitFor();
    const headings = (await page.locator('main > section.level1 > h1').allTextContents())
      .map(heading => heading.replace(/^\d+\s+/, '').trim());
    assert.deepEqual(headings, expected, `${name}: missing, extra or reordered section heading`);
    const dimensions = await page.evaluate(() => ({ viewport: window.innerWidth, document: document.documentElement.scrollWidth, body: document.body.scrollWidth }));
    assert(dimensions.document <= width, `${name}: horizontal overflow`);
    assert.deepEqual(errors, [], `${name}: browser errors`);
    assert.deepEqual(networkRequests, [], `${name}: unexpected external request`);
    await page.screenshot({ path: fileURLToPath(new URL(`fyp2-${name}.png`, output)), fullPage: true });
    report.cases.push({ name, width, height, dimensions, headingsPresent: expected.length, errors, networkRequests });
    await context.close();
  }
  await writeFile(new URL('fyp2-html-check.json', output), JSON.stringify(report, null, 2) + '\n');
  console.log(JSON.stringify(report, null, 2));
} finally {
  await browser.close();
}
