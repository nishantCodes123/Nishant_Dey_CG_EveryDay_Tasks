import { test, expect } from '@playwright/test';
import { loginPage } from '../Pages/loginPage';
import { dashboardPage } from '../Pages/Beneficiary';

test('Verify user can create a new beneficiary', async ({ page }) => {

   
    const lp = new loginPage(page);

    await lp.open();

    await lp.login('apex_user', 'Password123!');

  
    const dp = new dashboardPage(page);

    await dp.transferFunds();

    await dp.addNewBeneficiary();

    await dp.benefit('Nishant', 1234567890);

});