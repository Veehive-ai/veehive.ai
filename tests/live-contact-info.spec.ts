import { test, expect } from '@playwright/test';

const BASE = 'https://veehive.ai';
const PAGES = ['/', '/about.html', '/team.html', '/hivelink.html', '/privacy.html', '/terms.html'];

const NEW_EMAIL = 'contact@veehive.ai';
const NEW_WA_PATH = 'wa.me/971564308275';
const NEW_WA_DISPLAY = '+971 56 430 8275';

const OLD_EMAILS = ['sathish@veehive.ai', 'support@veehive.ai'];
const OLD_WA = ['wa.me/971502753576', '+971502753576', '+971 50 275 3576'];

for (const path of PAGES) {
  test(`live ${path}: new contact info present, old absent`, async ({ page }) => {
    const resp = await page.goto(BASE + path, { waitUntil: 'domcontentloaded' });
    expect(resp?.status(), `HTTP status for ${path}`).toBeLessThan(400);
    const html = await page.content();

    for (const old of OLD_EMAILS) {
      expect(html, `${path} should not contain ${old}`).not.toContain(old);
    }
    for (const old of OLD_WA) {
      expect(html, `${path} should not contain ${old}`).not.toContain(old);
    }

    const pagesWithEmail = ['/', '/about.html', '/team.html', '/hivelink.html', '/privacy.html', '/terms.html'];
    if (pagesWithEmail.includes(path)) {
      expect(html, `${path} should contain ${NEW_EMAIL}`).toContain(NEW_EMAIL);
    }

    const pagesWithWa = ['/', '/about.html', '/hivelink.html', '/privacy.html', '/terms.html'];
    if (pagesWithWa.includes(path)) {
      expect(html, `${path} should contain ${NEW_WA_PATH}`).toContain(NEW_WA_PATH);
    }

    const pagesWithWaDisplay = ['/privacy.html', '/terms.html'];
    if (pagesWithWaDisplay.includes(path)) {
      expect(html, `${path} should contain display ${NEW_WA_DISPLAY}`).toContain(NEW_WA_DISPLAY);
    }
  });
}
