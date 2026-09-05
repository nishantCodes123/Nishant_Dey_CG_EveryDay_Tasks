import { chromium } from '@playwright/test';

async function globalSetup() {

    console.log('Global Setup Started');

    const browser = await chromium.launch();
    const page = await browser.newPage();
    await page.goto('https://www.playwrightpad.in/sandbox/banking');
    await page.fill('input[name="username"]', 'apex_user');
    await page.fill('input[name="password"]', 'Password123!');
    await page.click('button:has-text("LOGIN")');
    await page.context().storageState({
        path: 'auth.json'
    });

    await browser.close();

    console.log('Global Setup Completed');
}

export default globalSetup;