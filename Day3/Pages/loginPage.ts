import { Page   } from "@playwright/test";


export class loginPage {

    constructor( private page : Page) {}

    // locators 

    username = 'input[name="username"]';
    password = 'input[name="password"]';
    loginButton = 'button:has-text("LOGIN")';

    // page actions 

    async open(){

          await this.page.goto('https://www.playwrightpad.in/sandbox/banking');
    }

    async login (user : string , pass : string){

        await this.page.fill(this.username,user);
        await this.page.fill(this.password,pass);
        await this.page.click(this.loginButton);
    
    }

}