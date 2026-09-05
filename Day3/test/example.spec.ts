import { test } from '@playwright/test';

test('visit Google', async ({ page }) => {
	await page.goto('https://www.google.com');
});
