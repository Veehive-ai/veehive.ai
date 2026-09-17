import { test, expect } from '@playwright/test';

const BASE = 'https://veehive.ai';
const PAGES_TO_CHECK = ['/', '/about.html', '/team.html', '/privacy.html', '/terms.html'];

test.describe('Veehive Link rename + 301 redirect', () => {
  for (const path of PAGES_TO_CHECK) {
    test(`${path}: contains "Veehive Link" and zero "HiveLink" / hivelink.html refs`, async ({ page }) => {
      const resp = await page.goto(BASE + path, { waitUntil: 'domcontentloaded' });
      expect(resp?.status(), `HTTP for ${path}`).toBeLessThan(400);
      const html = await page.content();

      expect(html, `${path} should contain "Veehive Link"`).toContain('Veehive Link');
      expect(html, `${path} must NOT contain "HiveLink"`).not.toContain('HiveLink');

      // No anchor links to the deleted page. The substring may still appear
      // inside the GA4 click handler matcher — that's intentional legacy support.
      const brokenAnchors = await page.locator('a[href*="hivelink.html"]').count();
      expect(brokenAnchors, `${path} should have no <a href> pointing at hivelink.html`).toBe(0);
    });
  }

  test('homepage: Veehive Link nav, footer, and module card link to veehivelink.com in new tab', async ({ page }) => {
    await page.goto(BASE + '/', { waitUntil: 'domcontentloaded' });

    const links = await page.locator('a[href="https://veehivelink.com"]').all();
    expect(links.length, 'at least one veehivelink.com link on homepage').toBeGreaterThanOrEqual(3);

    for (const link of links) {
      const target = await link.getAttribute('target');
      const rel = await link.getAttribute('rel');
      expect(target, 'target should be _blank').toBe('_blank');
      expect(rel, 'rel should include noopener').toContain('noopener');
    }
  });

  test('301 redirect: /hivelink.html → veehivelink.com', async ({ request }) => {
    const resp = await request.get(BASE + '/hivelink.html', { maxRedirects: 0 });
    expect(resp.status(), 'should be a redirect status').toBe(301);
    const location = resp.headers()['location'];
    expect(location, 'redirect target').toBe('https://veehivelink.com');
  });

  test('homepage schema.org JSON-LD names "Veehive Link" with veehivelink.com URL', async ({ page }) => {
    await page.goto(BASE + '/', { waitUntil: 'domcontentloaded' });
    const blocks = await page.locator('script[type="application/ld+json"]').allTextContents();
    const joined = blocks.join('\n');

    expect(joined).toContain('"Veehive Link"');
    expect(joined).toContain('https://veehivelink.com');
    expect(joined).not.toContain('community.veehive.ai');
    expect(joined).not.toMatch(/"name":\s*"HiveLink"/);
  });

  test('sitemap.xml has no /hivelink.html entry', async ({ request }) => {
    const resp = await request.get(BASE + '/sitemap.xml');
    expect(resp.status()).toBe(200);
    const body = await resp.text();
    expect(body).not.toContain('/hivelink.html');
  });
});
