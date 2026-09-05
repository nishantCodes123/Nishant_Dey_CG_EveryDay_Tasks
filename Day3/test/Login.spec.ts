import { test, expect } from '@playwright/test';
import { loginPage } from '../Pages/loginPage';
import fs from 'fs';
import path from 'path';



const filePath = path.join(__dirname, '../testData/LoginData.csv');

const csvData = fs.readFileSync(filePath, 'utf-8');



const testData = csvData
    .trim()
    .split('\n')
    .slice(1)
    .map(row => {
        const [username, password] = row.split(',');

        return {
            username: username.trim(),
            password: password.trim()
        };
    });



for (const data of testData) {

    test(`Verify login with username: ${data.username}`, async ({ page }) => {

        const lp = new loginPage(page);

        await lp.open();

        await lp.login(data.username, data.password);
        

    });

}