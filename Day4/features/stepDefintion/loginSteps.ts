import {Given,When,Then} from '@cucumber/cucumber';
import {LoginPage} from '../../pages/LoginPage';
import {CustomWorld} from '../../support/world';
 
let login: LoginPage;
 
Given('the user is on the login page', async function (this : CustomWorld ) {
    login = new LoginPage(this.page);
    await login.openApp();
});
 
When('the user enters valid credentials', async function (this : CustomWorld) {
  await login.fillwithvalidcredential();
});
 
When('clicks the login button', async function (this : CustomWorld) {
    await login.clickloginbutton();
});
 
Then('the user should be redirected to the dashboard', async function (this : CustomWorld) {
  await login.verifySuccesfullogin();
});
 
When('the user enters invalid credentials', async function (this : CustomWorld) {
  await login.fillwithinvalidcredentials('user','sauce');
});
 
Then('the user should see an error message', async function (this : CustomWorld) {
  console.log('Verifying error message');
  await login.Errormessagevisible();
});
When('the user enters {string} and {string}', async  function (string, string2) {
    await login.loginwithmultipleusers(string,string2);          
});